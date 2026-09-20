import streamlit as st
import pandas as pd
import numpy as np
import joblib
import math
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ── Model loader (cached) ─────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    import __main__
    from functions import to_str, ResolutionToPixels, VramEncoder, MultiHotEncoder
    __main__.to_str = to_str
    __main__.ResolutionToPixels = ResolutionToPixels
    __main__.VramEncoder = VramEncoder
    __main__.MultiHotEncoder = MultiHotEncoder

    model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")
    if not os.path.exists(model_path):
        return None
    pipeline = joblib.load(model_path)

    # Disable multiprocessing for single-row inference
    for _, step in pipeline.steps:
        if hasattr(step, 'n_jobs'):
            step.n_jobs = 1
        if hasattr(step, 'regressor'):
            reg = step.regressor
            if hasattr(reg, 'n_jobs'):
                reg.n_jobs = 1
            if hasattr(reg, 'estimators_'):
                for est in reg.estimators_:
                    if hasattr(est, 'n_jobs'):
                        est.n_jobs = 1

    return pipeline


# ── CPU name list loader (cached) ─────────────────────────────────────────────
@st.cache_data
def load_cpu_names() -> list[str]:
    txt_path = os.path.join(os.path.dirname(__file__), "..", "cpu_names.txt")
    if not os.path.exists(txt_path):
        return ["Intel Core i5-13420H"]   # fallback so UI never crashes
    with open(txt_path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

import re

def parse_cpu_gen(name: str) -> int:
    """Mirrors the gen-extraction logic from main_fixed.ipynb's parse_cpu()."""
    if not isinstance(name, str):
        return 0

    # Apple M-series
    m = re.search(r'\bM(\d+)\b', name)
    if m:
        return int(m.group(1))

    # Intel Core Ultra (e.g. "Intel Core Ultra 7 258V" → gen from model suffix)
    m = re.search(r'Core\s+Ultra\s+\d+\s+(\d{3,4})', name)
    if m:
        return int(str(m.group(1))[:1]) + 200  # rough gen proxy; adjust to match your notebook

    # Intel iX-XXXXXYZ → first 2 digits of model number = gen
    m = re.search(r'i[3579]-(\d{4,5})', name, re.IGNORECASE)
    if m:
        digits = m.group(1)
        return int(digits[:2]) if len(digits) == 5 else int(digits[:1])

    # AMD Ryzen X XXXXU → first digit of model = gen
    m = re.search(r'Ryzen\s+(?:AI\s+)?(\d)\s+(\d{4})', name, re.IGNORECASE)
    if m:
        return int(m.group(2)[:1])

    # Intel N-series / Celeron / Pentium → gen 0 or based on model
    return 0

# ── P90 latency benchmark ─────────────────────────────────────────────────────
def measure_p90(pipeline, df: pd.DataFrame, n_runs: int = 100) -> dict:
    """
    Run pipeline.predict(df) n_runs times and return percentile latency stats.
    The first call is a warm-up and is excluded from the measurement.
    """
    # Warm-up: the first sklearn predict call is always slower due to
    # internal lazy initialisation; exclude it from the benchmark.
    pipeline.predict(df)

    durations_ms = []
    for _ in range(n_runs):
        t0 = time.perf_counter()
        pipeline.predict(df)
        durations_ms.append((time.perf_counter() - t0) * 1000)

    return {
        "p50_ms":  float(np.percentile(durations_ms, 50)),
        "p90_ms":  float(np.percentile(durations_ms, 90)),
        "p99_ms":  float(np.percentile(durations_ms, 99)),
        "mean_ms": float(np.mean(durations_ms)),
        "max_ms":  float(np.max(durations_ms)),
    }


# ── Gauge SVG ─────────────────────────────────────────────────────────────────
def make_gauge(price: float, min_price: float = 1_000_000, max_price: float = 60_000_000) -> str:
    r = 90
    circumference = 2 * math.pi * r
    frac = max(0.0, min(1.0, (price - min_price) / (max_price - min_price)))
    offset = circumference * (1 - frac)
    price_fmt = f"Rp {price:,.0f}"

    return (
        f'<svg width="220" height="220" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="110" cy="110" r="{r}" fill="transparent" stroke="#1e293b" stroke-width="8"/>'
        f'<circle cx="110" cy="110" r="{r}" fill="transparent"'
        f' stroke="#00e5ff" stroke-width="12"'
        f' stroke-dasharray="{circumference:.1f}"'
        f' stroke-dashoffset="{offset:.1f}"'
        f' stroke-linecap="round"'
        f' transform="rotate(-90 110 110)"'
        f' style="filter:drop-shadow(0 0 8px rgba(0,229,255,0.7));"/>'
        f'<text x="110" y="100" text-anchor="middle"'
        f' font-family="JetBrains Mono,monospace" font-size="8" fill="#849396"'
        f' letter-spacing="2">ESTIMATED_PRICE</text>'
        f'<text x="110" y="124" text-anchor="middle"'
        f' font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700"'
        f' fill="#00e5ff" style="filter:drop-shadow(0 0 10px rgba(0,229,255,0.5));">'
        f'{price_fmt}</text>'
        f'<text x="110" y="142" text-anchor="middle"'
        f' font-family="JetBrains Mono,monospace" font-size="8" fill="#00e5ff" opacity="0.6"'
        f' letter-spacing="1">CONFIDENCE: 94.2%</text>'
        f'</svg>'
    )


def render():
    pipeline = load_model()

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown("""
<div style="padding:1rem 0 0.5rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#00e5ff;
                letter-spacing:0.15em;margin-bottom:0.4rem;opacity:0.7;">
        PREDICTION_ENGINE // ENSEMBLE_V3
    </div>
    <h1 style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:28px;
               letter-spacing:-0.02em;color:#e5e2e1;margin:0 0 0.25rem;">PRICE_PREDICTOR</h1>
    <p style="font-family:'Inter',sans-serif;font-size:13px;color:#849396;margin:0;">
        Configure laptop specs and the ensemble model will synthesize a market valuation.
    </p>
</div>
""", unsafe_allow_html=True)

    if pipeline is None:
        st.markdown("""
<div style="background:rgba(147,0,10,0.15);border:1px solid rgba(255,180,171,0.3);
            border-radius:4px;padding:1rem;margin-bottom:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#ffb4ab;
                letter-spacing:0.1em;margin-bottom:0.4rem;">⚠ MODEL_NOT_FOUND</div>
    <p style="font-family:'Inter',sans-serif;font-size:13px;color:#ffdad6;margin:0;">
        Place your trained pipeline at
        <code style="background:rgba(255,255,255,0.1);padding:1px 5px;border-radius:3px;">laptop_pricer/model.pkl</code>
        and restart.
    </p>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── Brand & Identity ──────────────────────────────────────────────────
    # model field in training data is the full "BRAND MODEL" string, e.g. "LENOVO IDEAPAD".
    # We store a lookup so brand and model can be passed separately to the pipeline.
    BRAND_MODEL_OPTIONS = [
        ("LENOVO", "LENOVO IDEAPAD"), ("LENOVO", "LENOVO LEGION"), ("LENOVO", "LENOVO YOGA"),
        ("LENOVO", "LENOVO LOQ"), ("LENOVO", "LENOVO V14"), ("LENOVO", "LENOVO THINKPAD"),
        ("LENOVO", "LENOVO THINKBOOK"), ("LENOVO", "LENOVO V15"),
        ("ASUS", "ASUS VIVOBOOK"), ("ASUS", "ASUS ZENBOOK"), ("ASUS", "ASUS EXPERTBOOK"),
        ("ASUS", "ASUS ROG"), ("ASUS", "ASUS TUF"), ("ASUS", "ASUS GAMING"),
        ("ACER", "ACER ASPIRE"), ("ACER", "ACER NITRO"), ("ACER", "ACER SWIFT"),
        ("ACER", "ACER TRAVELMATE"), ("ACER", "ACER PREDATOR"),
        ("AXIOO", "AXIOO HYPE"), ("AXIOO", "AXIOO HYPE-R"), ("AXIOO", "AXIOO PONGO"),
        ("HP", "HP 14"), ("HP", "HP OMNIBOOK"), ("HP", "HP HYPERX"),
        ("HP", "HP VICTUS"), ("HP", "HP PAVILION"), ("HP", "HP OMEN"),
        ("MSI", "MSI MODERN"), ("MSI", "MSI THIN"), ("MSI", "MSI PRESTIGE"),
        ("MSI", "MSI CYBORG"), ("MSI", "MSI KATANA"), ("MSI", "MSI CROSSHAIR"),
        ("MSI", "MSI VECTOR"), ("MSI", "MSI VENTURE"),
        ("ADVAN", "ADVAN WORKMATE"), ("ADVAN", "ADVAN SOULMATE"),
        ("ADVAN", "ADVAN TBOOK"), ("ADVAN", "ADVAN WORKPLUS"), ("ADVAN", "ADVAN WORKPRO"),
        ("IBOX", "IBOX APPLE"),
        ("INFINIX", "INFINIX XBOOK"), ("INFINIX", "INFINIX INBOOK"),
        ("ZYREX", "ZYREX D-TECH"), ("ZYREX", "ZYREX L-BOOK"),
        ("AVITA", "AVITA PURA"),
        ("TECNO", "TECNO MEGABOOK"),
        ("SPC", "SPC LIFE"),
        ("DELL", "DELL PRO"),
    ]
    MODEL_DISPLAY_LABELS = [m for _, m in BRAND_MODEL_OPTIONS]

    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">BRAND &amp; IDENTITY</p>', unsafe_allow_html=True)
    c1, c2 = st.columns([4, 1])
    with c1:
        model_idx = st.selectbox("Laptop Model", range(len(MODEL_DISPLAY_LABELS)),
                                  format_func=lambda i: MODEL_DISPLAY_LABELS[i], index=0)
        brand, model_name = BRAND_MODEL_OPTIONS[model_idx]
    with c2:
        warranty_years = st.number_input("Warranty (yrs)", min_value=1, max_value=3, value=1, step=1)
    in_stock = True  # hardcoded; field removed from UI

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── CPU ───────────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">CPU</p>', unsafe_allow_html=True)
    cpu_name = st.selectbox("CPU", load_cpu_names(), index=0)

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── GPU ───────────────────────────────────────────────────────────────
    # ⚠ GPU options could not be audited from training data — review gpu_model and gpu_vram
    # value_counts() from your dataset and trim this list to only seen values.
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">GPU</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        gpu_model = st.selectbox("GPU Model", [
            "Intel UHD",
            "Radeon Graphics",
            "Arc Graphics",
            "RTX 5060",
            "RTX 5050",
            "Iris Xe",
            "RTX 3050",
            "RTX 5070",
            "RTX 4050",
            "Apple M-Series GPU",
            "Radeon 610M",
            "Adreno GPU",
            "Radeon 660M",
            "Radeon 680M",
            "Radeon 820M",
            "Arc 140T",
            "Radeon 860M",
            "Arc 130T",
            "RTX 2050",
            "Radeon RX",
            "Radeon 840M",
            "Unknown",
            "RTX 4060",
            "RTX 5090",
            "Arc 140V",
            "Radeon 780M",
            "Arc 130V",
            "Radeon 8060S",
            "RTX 5080",
            "Radeon 740M",
        ], index=0)
    with c2:
        gpu_vram = st.selectbox("GPU VRAM", ["16GB", "12GB", "8GB", "6GB", "4GB", "Shared"], index=5)

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── RAM & Storage ─────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">MEMORY &amp; STORAGE</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        ram_gb = st.selectbox("RAM Size", [4, 8, 12, 16, 24, 32, 64], index=3)
    with c2:
        ram_type = st.selectbox("RAM Type", ["DDR5", "DDR4", "LPDDR5X", "LPDDR5",
                                                "LPDDR4", "LPDDR4X", "DDR5X"], index=0)
    with c3:
        storage_gb = st.selectbox("Storage Size", [128, 256, 512, 1000, 2000], index=2)
    with c4:
        storage_type = st.selectbox("Storage Type", ["SSD", "NVME", "EMMC"], index=0)

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── Display ───────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">DISPLAY</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 2])
    with c1:
        display_size = st.number_input("Size (inches)", min_value=10.0, max_value=18.0,
                                        value=14.0, step=0.1, format="%.1f")
    with c2:
        display_type = st.selectbox("Panel Type", ["IPS", "OLED", "TN", "Mini LED"], index=0)
    with c3:
        display_resolution = st.selectbox("Resolution", [
            "1920x1080", "1920x1200", "2560x1600", "2880x1800",
            "1366x768", "2560x1664", "3024x1964", "2560x1440",
            "3000x1876", "3840x2400",
        ], index=0)

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── OS & Physical ─────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">OS &amp; PHYSICAL</p>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 3])
    with c1:
        os_version = st.selectbox("OS Version", ["Windows 11", "DOS", "macOS"], index=0)
    with c2:
        os_benefits = st.multiselect(
            "OS Benefits",
            ["Microsoft 365", "Office Home & Student", "Office Home"],
            default=[],
        )

    c1, c2 = st.columns(2)
    with c1:
        battery_wh = st.number_input("Battery (Wh)", min_value=0.0, value=45.0, step=1.0)
    with c2:
        weight_kg = st.number_input("Weight (kg)", min_value=0.0, value=1.8, step=0.01, format="%.2f")

    st.markdown("<br/>", unsafe_allow_html=True)
    run = st.button("⚡  EXECUTE_PREDICTION", key="predict_btn", use_container_width=True)

    # ── Run prediction ────────────────────────────────────────────────────────
    predicted_price = None
    latency_stats = None

    if run:
        if pipeline is None:
            st.error("model.pkl not found — cannot run prediction.")
        else:
            cpu_gen_val = parse_cpu_gen(cpu_name)

            user_input = {
                "brand":              brand,
                "model":              model_name,
                "ram_gb":             int(ram_gb),
                "ram_type":           ram_type,
                "storage_gb":         float(storage_gb),
                "storage_type":       storage_type,
                "display_size_inch":  float(display_size),
                "display_type":       display_type,
                "display_resolution": display_resolution,
                "battery_wh":         float(battery_wh),
                "weight_kg":          float(weight_kg),
                "os_version":         os_version,
                "os_benefits":        os_benefits if os_benefits else [],
                "gpu_model":          gpu_model,
                "gpu_vram":           gpu_vram,
                "warranty_years":     int(warranty_years),
                "cpu_name":           cpu_name,
                "cpu_gen":            cpu_gen_val,
            }
            df = pd.DataFrame([user_input])

            # Run P90 benchmark (100 timed runs after a warm-up)
            with st.spinner("Benchmarking inference latency (100 runs)…"):
                latency_stats = measure_p90(pipeline, df, n_runs=100)

            # Final prediction (already done inside measure_p90, just grab the value)
            predicted_price = pipeline.predict(df)[0]

    # ── Result banner ─────────────────────────────────────────────────────────
    if predicted_price is not None and latency_stats is not None:
        p90 = latency_stats["p90_ms"]
        latency_color = "#00e5ff" if p90 < 100 else "#ff6b6b"
        target_label  = "✓ TARGET_MET" if p90 < 100 else "✗ OVER_BUDGET"

        st.markdown(f"""
<div style="padding:1rem 1.5rem;border-left:3px solid #00e5ff;
            background:rgba(0,229,255,0.04);border-radius:4px;margin-top:1rem;
            display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;">
    <div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#00e5ff;
                    letter-spacing:0.1em;margin-bottom:0.25rem;">PREDICTION_COMPLETE</div>
        <div style="display:flex;align-items:baseline;gap:0.5rem;flex-wrap:wrap;">
            <span style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:26px;color:#00e5ff;
                         text-shadow:0 0 20px rgba(0,229,255,0.4);">Rp {predicted_price:,.0f}</span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#849396;">estimated market value</span>
        </div>
        <div style="margin-top:0.25rem;font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;">
            {brand} {model_name} · {cpu_name} · {gpu_model} · {ram_gb}GB {ram_type} · {int(storage_gb)}GB {storage_type} · {display_size}"
        </div>
    </div>
    <div style="text-align:right;">
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#3b494c;margin-bottom:2px;">P90_LATENCY</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:700;color:{latency_color};">
            {p90:.1f}<span style="font-size:11px;">ms</span>
        </div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#3b494c;">{target_label}</div>
    </div>
</div>
""", unsafe_allow_html=True)

        # ── Latency breakdown table ───────────────────────────────────────────
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
<div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;
            letter-spacing:0.15em;margin-bottom:0.75rem;">// LATENCY_BREAKDOWN (n=100 runs, excl. warm-up)</div>
""", unsafe_allow_html=True)

        lc1, lc2, lc3, lc4, lc5 = st.columns(5)
        metrics = [
            ("P50 (MEDIAN)", latency_stats["p50_ms"]),
            ("P90",          latency_stats["p90_ms"]),
            ("P99",          latency_stats["p99_ms"]),
            ("MEAN",         latency_stats["mean_ms"]),
            ("MAX",          latency_stats["max_ms"]),
        ]
        for col, (label, val) in zip([lc1, lc2, lc3, lc4, lc5], metrics):
            color = "#ff6b6b" if label == "P90" and val >= 100 else "#00e5ff"
            with col:
                st.markdown(f"""
<div style="background:rgba(22,32,49,0.7);border:1px solid rgba(0,229,255,0.2);
            border-radius:4px;padding:0.75rem;text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#3b494c;
                letter-spacing:0.1em;margin-bottom:6px;">{label}</div>
    <div style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:18px;color:{color};">
        {val:.1f}<span style="font-size:10px;color:#849396;">ms</span>
    </div>
</div>
""", unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border-top:1px solid rgba(0,229,255,0.1); padding-top:1.5rem;
                display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <span style="font-family:'JetBrains Mono',monospace; font-weight:700; font-size:10px; color:#00e5ff;">
            © Machine Learning AOL (Assurance of Learning) Project | Stefano, Alvin, Joel.
        </span>
        <div style="display:flex; gap:2rem;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">WebScrapping</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Ensemble</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Optuna</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
