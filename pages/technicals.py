import streamlit as st


def render():
    st.markdown("""
    <div style="padding: 2rem 0 1.5rem;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                    letter-spacing:0.15em; margin-bottom:0.75rem; opacity:0.7;">PIPELINE_ARCHITECTURE // V3.2.1</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:38px;
                   letter-spacing:-0.02em; color:#e5e2e1; margin-bottom:0.5rem;">
            TECHNICAL_DEEP_DIVE
        </h1>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#bac9cc; max-width:600px;">
            Six-stage ML pipeline from raw DOM scraping to validated ensemble predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 01 + 02
    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #00e5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">01</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Web Scraping
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Asynchronous scraper built with <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">BeautifulSoup4</span>
                + <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">httpx</span>.
                Extracts structured laptop data from 'Agres' marketplace with rate-limiting and retry logic.
            </p>
            <div>
                <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace;
                            font-size:9px; color:#00e5ff; margin-bottom:4px;">
                    <span>COLLECTION_RATE</span><span>98.7%</span>
                </div>
                <div style="background:#0f172a; height:3px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:98.7%; height:100%; box-shadow:0 0 6px rgba(0,229,255,0.5);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">02</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Data Normalization
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Manual remap of ambiguous product strings. Normalization of SKU variants across
                multiple vendor formats using a canonical hardware taxonomy.
            </p>
            <div>
                <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace;
                            font-size:9px; color:#00e5ff; margin-bottom:4px;">
                    <span>REMAP_ACCURACY</span><span>92.4%</span>
                </div>
                <div style="background:#0f172a; height:3px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:92.4%; height:100%; box-shadow:0 0 6px rgba(0,229,255,0.5);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 03 + 04 — same row
    c3, c4 = st.columns(2, gap="medium")

    with c3:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">03</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Smart Imputation
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Hybrid imputation strategy using statistical distribution for non-critical features
                and algorithm-driven filling for high-variance dimensions.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                <div style="padding:1rem; border:1px solid rgba(0,229,255,0.2); background:rgba(0,229,255,0.05);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff; margin-bottom:4px;">GENERAL</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:20px; color:#e5e2e1;">MEDIAN</div>
                </div>
                <div style="padding:1rem; border:1px solid rgba(0,104,237,0.2); background:rgba(0,104,237,0.05);">
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:16px; color:#e5e2e1; line-height:1.5; margin-bottom:6px;">weight_kg<br/>battery_wh</div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#b0c6ff;">KNN · n_neighbors=5</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #c3f5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">04</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Ensemble Learning
                </span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.75rem; margin-bottom:1.5rem;">
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0; margin-bottom:4px;">BASE_01</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">CatBoost</div>
                </div>
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0; margin-bottom:4px;">BASE_02</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">XGBoost</div>
                </div>
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0; margin-bottom:4px;">BASE_03</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">LightGBM</div>
                </div>
            </div>
            <div style="background:rgba(0,229,255,0.08); padding:1rem; border:1px solid rgba(0,229,255,0.3);
                        border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff; opacity:0.6; margin-bottom:4px;">META_LEARNER</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:22px; color:#c3f5ff;">RIDGECV</div>
                </div>
                <span class="material-symbols-outlined" style="color:#00e5ff; font-size:2rem;">account_tree</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 05 — Optuna full-width
    # FIX: removed blank lines inside the HTML string — Streamlit's Markdown parser
    # exits "HTML block" mode at blank lines, causing indented content after them
    # to be rendered as a code block instead of HTML.
    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-bottom:0.5rem;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">05</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Optuna Tuning
                </span>
            </div>
            <div style="display:flex; gap:1.5rem; flex-wrap:wrap;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">SAMPLER: TPE_Sampler(seed=42)</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">DIRECTION: minimize</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">TARGET: MAPE</span>
            </div>
        </div>
        <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem; max-width:800px;">
            Automated Bayesian optimization via TPE sampler, independently tuning each base learner.
            Each study minimizes cross-validated MAPE using a <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">KFold(n_splits=5)</span>
            pipeline wrapped in <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">TransformedTargetRegressor(log1p / expm1)</span>.
        </p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem;">
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">XGBoost</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">50 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">n_estimators</span><span style="color:#bac9cc;">300 – 3000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">learning_rate</span><span style="color:#bac9cc;">1e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">max_depth</span><span style="color:#bac9cc;">3 – 8</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">subsample</span><span style="color:#bac9cc;">0.6 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">colsample_bytree</span><span style="color:#bac9cc;">0.5 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">reg_alpha</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">reg_lambda</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">min_child_weight</span><span style="color:#bac9cc;">1 – 10</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">gamma</span><span style="color:#bac9cc;">0.0 – 1.0</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0;">
                    device=cuda &nbsp;·&nbsp; tree_method=hist &nbsp;·&nbsp; random_state=42
                </div>
            </div>
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">LightGBM</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">50 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">n_estimators</span><span style="color:#bac9cc;">300 – 3000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">learning_rate</span><span style="color:#bac9cc;">1e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">max_depth</span><span style="color:#bac9cc;">3 – 8</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">num_leaves</span><span style="color:#bac9cc;">15 – 127</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">min_child_samples</span><span style="color:#bac9cc;">5 – 50</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">subsample</span><span style="color:#bac9cc;">0.6 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">colsample_bytree</span><span style="color:#bac9cc;">0.5 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">reg_alpha</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">reg_lambda</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0;">
                    device=gpu &nbsp;·&nbsp; deterministic=True &nbsp;·&nbsp; importance_type=gain
                </div>
            </div>
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">CatBoost</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">30 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">iterations</span><span style="color:#bac9cc;">300 – 1500</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">learning_rate</span><span style="color:#bac9cc;">5e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">depth</span><span style="color:#bac9cc;">4 – 10</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">l2_leaf_reg</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">bagging_temperature</span><span style="color:#bac9cc;">0.0 – 2.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">random_strength</span><span style="color:#bac9cc;">0.0 – 3.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">min_data_in_leaf</span><span style="color:#bac9cc;">1 – 30</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#8ea8b0;">border_count</span><span style="color:#bac9cc;">32 – 255</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#8ea8b0;">
                    loss=RMSE &nbsp;·&nbsp; eval=MAPE &nbsp;·&nbsp; bootstrap=Bayesian &nbsp;·&nbsp; grow=SymmetricTree &nbsp;·&nbsp; task=GPU
                </div>
            </div>
        </div>
        <div style="margin-top:1rem; padding:0.75rem 1rem; background:rgba(0,229,255,0.04);
                    border:1px solid rgba(0,229,255,0.15); display:flex; gap:2rem; flex-wrap:wrap;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#8ea8b0;">CV_STRATEGY</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">KFold(n_splits=5, shuffle=True, random_state=42)</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#8ea8b0;">LOG_TRANSFORM</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">np.log1p → np.expm1</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#8ea8b0;">META_ALPHAS</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">RidgeCV([0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#8ea8b0;">PASSTHROUGH</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">True</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 06 - Results Comparison
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np
    import pandas as pd

    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem; flex-wrap:wrap; gap:1rem;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">06</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Results Comparison
                </span>
            </div>
            <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#00e5ff;">ENSEMBLE vs SOLO MODELS — 5-FOLD CV</span>
        </div>
        <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem; max-width:800px;">
            The stacking ensemble consistently outperforms every solo base learner across all evaluation metrics.
            Error bars show mean ± std across 5 CV folds — a tighter spread indicates more stable generalization.
            Lower error on <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">MAE · MAPE · RMSE · RMSLE</span>
            and highest <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">R²</span> confirms
            the meta-learner successfully exploits complementary strengths of CatBoost, XGBoost, and LightGBM.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Colour palette ────────────────────────────────────────────────────────
    ENSEMBLE_CLR = "#00e5ff"
    LGBM_CLR     = "#3b82f6"
    XGB_CLR      = "#6366f1"
    CAT_CLR      = "#22d3ee"
    PLOT_BG      = "rgba(0,0,0,0)"
    PAPER_BG     = "rgba(0,0,0,0)"
    GRID_CLR     = "rgba(0,229,255,0.08)"
    TICK_CLR     = "#3b494c"
    FONT_FAMILY  = "JetBrains Mono, monospace"

    base_layout = dict(
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(family=FONT_FAMILY, color="#94bac4", size=11),
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
    )

    axis_style = dict(
        gridcolor=GRID_CLR,
        linecolor="rgba(0,229,255,0.15)",
        tickfont=dict(color="#94bac4", size=10),  # was #3b494c
        zerolinecolor=GRID_CLR,
    )

    # ── CV data — update these values after each tuner run ───────────────────
    cv_data = pd.DataFrame([
        {"Model": "ensemble", "MAPE": 0.0846, "MAPE_Std": 0.0020, "MAE": 1220121.0, "MAE_Std": 60000.0,  "RMSE": 2120464.0, "RMSE_Std": 120000.0, "RMSLE": 0.1212, "RMSLE_Std": 0.008, "R2": 0.9129, "R2_Std": 0.018},
        {"Model": "lgbm",     "MAPE": 0.0860, "MAPE_Std": 0.0079, "MAE": 1220346.0, "MAE_Std": 117643.0, "RMSE": 2127470.0, "RMSE_Std": 289035.0, "RMSLE": 0.1233, "RMSLE_Std": 0.015, "R2": 0.9110, "R2_Std": 0.030},
        {"Model": "xgb",      "MAPE": 0.0891, "MAPE_Std": 0.0036, "MAE": 1280820.0, "MAE_Std": 75424.0,  "RMSE": 2212282.0, "RMSE_Std": 260908.0, "RMSLE": 0.1313, "RMSLE_Std": 0.018, "R2": 0.9052, "R2_Std": 0.027},
        {"Model": "catboost", "MAPE": 0.0931, "MAPE_Std": 0.0069, "MAE": 1311112.0, "MAE_Std": 125828.0, "RMSE": 2248026.0, "RMSE_Std": 387212.0, "RMSLE": 0.1335, "RMSLE_Std": 0.020, "R2": 0.9022, "R2_Std": 0.036},
    ])

    MODEL_COLORS = {
        "ensemble": ENSEMBLE_CLR,
        "lgbm":     LGBM_CLR,
        "xgb":      XGB_CLR,
        "catboost": CAT_CLR,
    }

    # ── Helper: one error-bar chart ───────────────────────────────────────────
    def make_errbar_fig(metric, title, ylabel, fmt, ascending=True):
        df = cv_data.sort_values(by=metric, ascending=ascending).reset_index(drop=True)
        std_col = f"{metric}_Std"
        fig = go.Figure()

        for _, row in df.iterrows():
            m    = row["Model"]
            mean = row[metric]
            std  = row[std_col]
            c    = MODEL_COLORS[m]
            is_ens = (m == "ensemble")

            fig.add_trace(go.Scatter(
                x=[m.upper(), m.upper(), m.upper()],
                y=[mean - std, mean, mean + std],
                mode="lines",
                line=dict(color=c, width=2 if is_ens else 1),
                showlegend=False,
                hoverinfo="skip",
            ))
            fig.add_trace(go.Scatter(
                x=[m.upper()], y=[mean + std],
                mode="markers",
                marker=dict(symbol="line-ew", size=10, color=c, line=dict(color=c, width=2)),
                showlegend=False,
                hoverinfo="skip",
            ))
            fig.add_trace(go.Scatter(
                x=[m.upper()], y=[mean - std],
                mode="markers",
                marker=dict(symbol="line-ew", size=10, color=c, line=dict(color=c, width=2)),
                showlegend=False,
                hoverinfo="skip",
            ))
            fig.add_trace(go.Scatter(
                x=[m.upper()], y=[mean],
                mode="markers",
                marker=dict(size=14 if is_ens else 10, color=c, line=dict(color="#0a0f1e", width=2)),
                name=m,
                customdata=[[mean, std]],
                hovertemplate=f"<b>{m.upper()}</b><br>Mean: %{{customdata[0]:{fmt}}}<br>±Std: %{{customdata[1]:{fmt}}}<extra></extra>",
            ))

        max_top = (df[metric] + df[std_col]).max()
        min_bot = (df[metric] - df[std_col]).min()
        spread  = max_top - min_bot or max_top * 0.1
        fig.update_layout(
            **base_layout,
            height=300,
            title=dict(text=title, font=dict(family=FONT_FAMILY, color="#00e5ff", size=12), x=0.01, xanchor="left"),
            xaxis=dict(**axis_style, categoryorder="array", categoryarray=[r["Model"].upper() for _, r in df.iterrows()]),
            yaxis=dict(**axis_style, title=dict(text=ylabel, font=dict(color=TICK_CLR, size=10)),
                    range=[min_bot - spread * 0.3, max_top + spread * 0.3]),
        )
        return fig

    # ── Row 1: MAPE + MAE ────────────────────────────────────────────────────
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    with col1:
        st.plotly_chart(
            make_errbar_fig("MAPE",  "MAPE  ↓",  "CV MAPE",  ".4f"),
            use_container_width=True, config={"displayModeBar": False},
        )
    with col2:
        st.plotly_chart(
            make_errbar_fig("MAE",   "MAE  ↓",   "CV MAE",   ",.0f"),
            use_container_width=True, config={"displayModeBar": False},
        )
    with col3:
        st.plotly_chart(
            make_errbar_fig("RMSE",  "RMSE  ↓",  "CV RMSE",  ",.0f"),
            use_container_width=True, config={"displayModeBar": False},
        )
    with col4:
        st.plotly_chart(
            make_errbar_fig("RMSLE", "RMSLE  ↓", "CV RMSLE", ".4f"),
            use_container_width=True, config={"displayModeBar": False},
        )
    with col5:
        st.plotly_chart(
            make_errbar_fig("R2", "R²  ↑", "CV R²", ".4f", ascending=False),
            use_container_width=True, config={"displayModeBar": False},
        )

    # ── Verdict badges — dynamic ──────────────────────────────────────────────
    best = {
        "BEST_MAE":   cv_data.loc[cv_data["MAE"].idxmin(),   "Model"].upper(),
        "BEST_MAPE":  cv_data.loc[cv_data["MAPE"].idxmin(),  "Model"].upper(),
        "BEST_RMSE":  cv_data.loc[cv_data["RMSE"].idxmin(),  "Model"].upper(),
        "BEST_RMSLE": cv_data.loc[cv_data["RMSLE"].idxmin(), "Model"].upper(),
        "BEST_R2":    cv_data.loc[cv_data["R2"].idxmax(),    "Model"].upper(),
    }
    ens_mape     = cv_data.loc[cv_data["Model"] == "ensemble", "MAPE"].values[0]
    ens_mape_std = cv_data.loc[cv_data["Model"] == "ensemble", "MAPE_Std"].values[0]

    badges_html = "".join([
        f'''<div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4); background:rgba(0,229,255,0.06);">
            <span style="font-family:JetBrains Mono,monospace; font-size:9px; color:#cccccc; display:block; margin-bottom:2px;">{k}</span>
            <span style="font-family:Space Grotesk,sans-serif; font-weight:700; color:#00e5ff;">{v}</span>
        </div>'''
        for k, v in best.items()
    ])
    badges_html += f'''<div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4); background:rgba(0,229,255,0.06);">
        <span style="font-family:JetBrains Mono,monospace; font-size:9px; color:#cccccc; display:block; margin-bottom:2px;">LOWEST_CV_MAPE</span>
        <span style="font-family:Space Grotesk,sans-serif; font-weight:700; color:#00e5ff;">{ens_mape:.4f} ± {ens_mape_std:.4f}</span>
    </div>'''

    st.markdown(
        f'<div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:0.5rem;">{badges_html}</div>',
        unsafe_allow_html=True,
    )

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border-top:1px solid rgba(0,229,255,0.1); padding-top:1.5rem;
                display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <span style="font-family:'JetBrains Mono',monospace; font-weight:700; font-size:10px; color:#00e5ff;">
            © Machine Learning AOL (Assurance of Learning) Project | Stefano, Alvin, Joel.
        </span>
        <div style="display:flex; gap:2rem;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#cccccc;">WebScrapping</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#cccccc;">Ensemble</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#cccccc;">Optuna</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
