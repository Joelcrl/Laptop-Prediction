import streamlit as st


def render():
    # ── Hero ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding: 3rem 0 2rem;">
        <h1 style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:clamp(36px,5vw,56px);
                   line-height:1.05; letter-spacing:-0.03em; color:#e5e2e1; margin-bottom:1.5rem;">
            ALGORITHMIC <br/>
            PRICE <span style="background: linear-gradient(90deg, #00e5ff, #b0c6ff);
                               -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                               background-clip:text;">PREDICTION</span>
        </h1>
        <p style="font-family:'Inter',sans-serif; font-size:17px; line-height:1.7;
                  color:#bac9cc; max-width:600px; margin-bottom:2.5rem;">
            Solving market asymmetry through real-time scraping and ensemble-based regressive
            modeling. Transparent pricing for the hardware ecosystem.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        if st.button("RUN PREDICTOR", key="hero_predict"):
            st.session_state.page = "predictor"
            st.rerun()
    with col2:
        if st.button("VIEW TECHNICALS", key="hero_tech"):
            st.session_state.page = "technicals"
            st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Bento stats row ───────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;
                letter-spacing:0.15em; margin-bottom:1rem;">// SYSTEM_METRICS</div>
    """, unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("ENTRIES_SCRAPED", "583")
    with m2:
        st.metric("MODEL_R2", "0.9129")
    with m3:
        st.metric("MODEL_MAE", "Rp 1,220,121.1845")

    m4, m5, m6 = st.columns(3)
    with m4:
        st.metric("MODEL_RMSE", "Rp 2,120,463.7924 ")
    with m5:
        st.metric("MODEL_MAPE", "8.46% ")
    with m6:
        st.metric("LATENCY", "~65-75ms")

    st.markdown("<br/>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Feature cards ─────────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #00e5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; color:#00e5ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">visibility</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    Mission: Predictability
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc;">
                    Laptop pricing is incredibly hard to predict, especially in a competitive market. 
                Retailers use dynamic pricing that fluctuates, depending on discount, policies, etc.
                This app normalizes market data and empowers consumers with raw and unbiased price predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; color:#b0c6ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">terminal</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    BS4+Playwright Data Ingestion
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc;">
                Using <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">BeautifulSoup4 + Playwright</span>,
                we scrape live inventory from 'Agres'. The pipeline processes thousands of DOM elements
                daily to extract CPU, GPU, RAM, and localized price indices.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%; position:relative; overflow:hidden;">
            <div style="position:absolute; right:-2rem; top:-2rem; width:6rem; height:6rem;
                        background:rgba(0,229,255,0.05); border-radius:50%; filter:blur(20px);"></div>
            <div style="display:flex; align-items:center; gap:8px; color:#c3f5ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">neurology</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    Ensemble Architecture
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1rem;">
                Using ensemble learning method, stacking XGBoost, CatBoost, and LightGBM as the base regressor and RidgeCV as the Meta-Learner.
                Hyperparameters optimized using <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">Optuna</span> to minimize MAPE.
            </p>
            <div style="background:rgba(2,8,20,0.5); padding:0.75rem; border:1px solid rgba(0,229,255,0.2); border-radius:4px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">MODEL_R2</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">0.9413</span>
                </div>
                <div style="background:#0f172a; height:4px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:94.13%; height:100%;
                                box-shadow:0 0 8px rgba(0,229,255,0.6);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/><br/>", unsafe_allow_html=True)

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
