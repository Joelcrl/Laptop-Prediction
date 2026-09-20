import streamlit as st

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "page" not in st.session_state:
    st.session_state.page = "overview"

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>

<style>
html, body, [data-testid="stApp"] {
    background-color: #131313 !important;
    background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'Inter', sans-serif;
    color: #e5e2e1;
}
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stSidebarNav"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
.stDeployButton { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
div[data-testid="stToolbar"] { display: none !important; }

[data-testid="stSidebar"] {
    background: rgba(2, 8, 20, 0.95) !important;
    border-right: 1px solid rgba(0,229,255,0.2) !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
}

/* Sidebar buttons - transparent ghost style */
/* Sidebar buttons - Smaller by default */
[data-testid="stSidebar"] [data-testid="stButton"] > button {
    background: transparent !important;
    color: #849396 !important;
    border: 1px solid transparent !important;
    border-radius: 4px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 11px !important; /* Slightly smaller font */
    font-weight: 400 !important;
    padding: 0.3rem 0.8rem !important; /* Reduced padding */
    width: 100% !important;
    transition: all 0.2s ease; /* Smooth transition */
}
[data-testid="stSidebar"] [data-testid="stButton"] > button:hover {
    background: rgba(0,229,255,0.06) !important;
    color: #67e8f9 !important;
    border-color: rgba(0,229,255,0.15) !important;
    transform: none !important;
    filter: none !important;
}

.block-container { padding: 1.5rem 2rem 2rem 2rem !important; max-width: 100% !important; }

.glass-panel {
    background: rgba(22, 32, 49, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0,229,255,0.2);
    border-radius: 0.5rem;
}

[data-testid="stSelectbox"] > div > div,
[data-testid="stMultiSelect"] > div > div {
    background: #0f172a !important;
    border: 1px solid rgba(0,229,255,0.25) !important;
    border-radius: 4px !important;
    color: #e5e2e1 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
}
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input {
    background: #0f172a !important;
    border: 1px solid rgba(0,229,255,0.25) !important;
    border-radius: 4px !important;
    color: #e5e2e1 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
}
[data-testid="stCheckbox"] label {
    color: #bac9cc !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
}

/* Main area buttons - cyan filled */
[data-testid="stMain"] [data-testid="stButton"] > button {
    background: #00e5ff !important;
    color: #00363d !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    font-size: 13px !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.75rem 2rem !important;
    box-shadow: 0 0 20px rgba(0,229,255,0.3);
    width: 100%;
}
[data-testid="stMain"] [data-testid="stButton"] > button:hover {
    filter: brightness(1.1) !important;
    transform: scale(1.01) !important;
}

hr { border-color: rgba(0,229,255,0.1) !important; }
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: rgba(0,0,0,0.2); }
::-webkit-scrollbar-thumb { background: #00e5ff; border-radius: 2px; }

[data-testid="stWidgetLabel"] p, label {
    color: #849396 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}

[data-testid="stMetric"] {
    background: rgba(22,32,49,0.7);
    border: 1px solid rgba(0,229,255,0.2);
    border-radius: 4px;
    padding: 1rem;
}
[data-testid="stMetricLabel"] {
    color: #849396 !important;
    font-size: 10px !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    font-family: 'JetBrains Mono', monospace !important;
}
[data-testid="stMetricValue"] {
    color: #00e5ff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 26px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.25rem 1.25rem 0.75rem; border-bottom:1px solid rgba(0,229,255,0.15); margin-bottom:0.75rem;">
        <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px;
                    color:#00e5ff; text-shadow:0 0 8px rgba(0,229,255,0.4); letter-spacing:-0.02em;">
            Laptop Price Prediction
        </div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;
                    letter-spacing:0.12em; margin-top:3px;">Ensemble Learning: Stacking with XGBoost, LGBM, CATBoost -> RidgeCV</div>
    </div>
    <div style="padding:0 1.25rem 0.5rem; font-family:'JetBrains Mono',monospace; font-size:9px;
                color:#3b494c; letter-spacing:0.12em;">NAVIGATION</div>
    """, unsafe_allow_html=True)

    pages = [
        ("overview",   "Overview"),
        ("technicals", "Technicals"),
        ("predictor",  "Predictor"),
    ]

    for key, label in pages:
        is_active = st.session_state.page == key
        if is_active:
            # Active: styled div, no button (no click needed - already here)
            st.markdown(f"""
            <div style="padding:0.7rem 1rem; margin:0 0.5rem 6px;
                        background:rgba(0,229,255,0.15); border:1px solid rgba(0,229,255,0.4);
                        border-radius:6px; font-family:'Space Grotesk',sans-serif;
                        font-size:14px; font-weight:700; color:#00e5ff; 
                        letter-spacing:0.02em; text-align: center;
                        box-shadow: 0 0 15px rgba(0,229,255,0.1);">
                {label}
            </div>""", unsafe_allow_html=True)        
        else:
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()

    st.markdown("""
    <div style="margin-top:2rem; padding:1rem 1.25rem 0; border-top:1px solid rgba(0,229,255,0.1);">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; line-height:1.8;">
            By:<br/>
            Stefano B. - 2802402464<br/>
            M. Alvin - 2802402501<br/>
            Joel C. - 2802404450
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Page routing ──────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "overview":
    from pages import overview
    overview.render()
elif page == "technicals":
    from pages import technicals
    technicals.render()
elif page == "predictor":
    from pages import predictor
    predictor.render()
