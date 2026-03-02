import streamlit as st
from checker import check_requirement
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ReqQuality Pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# THEME ENGINE
# --------------------------------------------------

def apply_theme():
    if st.session_state.dark_mode:
        bg = "#0b1120"
        card = "rgba(30, 41, 59, 0.65)"
        border = "#334155"
        hero_gradient = "linear-gradient(90deg,#0f172a,#1e293b)"
        text_color = "#f1f5f9"
    else:
        bg = "#f8fafc"
        card = "rgba(255,255,255,0.85)"
        border = "#e2e8f0"
        hero_gradient = "linear-gradient(90deg,#2563eb,#1d4ed8)"
        text_color = "#0f172a"

    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg};
        color: {text_color};
    }}

    .hero {{
        padding: 50px;
        border-radius: 18px;
        background: {hero_gradient};
        color: white;
        margin-bottom: 30px;
    }}

    .glass-card {{
        padding: 25px;
        border-radius: 18px;
        background: {card};
        border: 1px solid {border};
        margin-bottom: 25px;
    }}

    .main-title {{
        font-size: 42px;
        font-weight: 700;
    }}

    .subtitle {{
        font-size: 18px;
        opacity: 0.9;
    }}

    .badge {{
        padding: 8px 18px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 14px;
        display: inline-block;
    }}
    </style>
    """, unsafe_allow_html=True)

apply_theme()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## ReqQuality Pro")
    st.toggle("🌙 Dark Mode", key="dark_mode")

    st.divider()

    st.markdown("### Platform Overview")
    st.write("""
    • IEEE 29148 Inspired Quality Mapping  
    • Rule-Based Validation  
    • Executive Decision Engine  
    • Interactive Visualization  
    """)

    st.divider()

    st.markdown("### Recent Analyses")

    if st.session_state.history:
        for item in st.session_state.history[-5:]:
            st.write(f"• {item[:40]}...")
    else:
        st.caption("No analyses yet.")

    st.divider()
    st.caption("Version 7.0 | Research Prototype")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="main-title">ReqQuality Pro</div>
    <div class="subtitle">
        Enterprise Requirements Quality Evaluation & Decision Support Platform
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

col1, col2 = st.columns([3,1])

with col1:
    requirement = st.text_area(
        "Enter Requirement Statement",
        height=150,
        placeholder="The system shall respond within 2 seconds to login requests."
    )

with col2:
    strictness = st.slider("Evaluation Strictness", 1, 5, 3)
    run = st.button("Run Analysis", use_container_width=True)

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if run:

    if not requirement.strip():
        st.warning("Please enter a requirement statement.")
    else:

        results, suggestions, score = check_requirement(requirement)
        st.session_state.history.append(requirement)

        # --------------------------------------------------
        # EXECUTIVE DECISION ENGINE
        # --------------------------------------------------

        if score >= 8:
            classification = "Production-Ready"
            risk = "Low"
            recommendation = "Approve"
            risk_color = "#22c55e"
        elif score >= 5:
            classification = "Acceptable with Revisions"
            risk = "Medium"
            recommendation = "Revise Before Approval"
            risk_color = "#f59e0b"
        else:
            classification = "High Risk Requirement"
            risk = "High"
            recommendation = "Reject"
            risk_color = "#ef4444"

        ieee_compliance = int((score / 10) * 100)

        st.markdown("### Executive Evaluation Summary")

        card_bg = "rgba(255,255,255,0.06)" if st.session_state.dark_mode else "rgba(0,0,0,0.04)"

        st.markdown(f"""
        <div style="
            display:flex;
            gap:20px;
            margin-top:15px;
            flex-wrap:wrap;
        ">

            <div style="flex:1; min-width:220px; padding:22px; border-radius:16px; background:{card_bg};">
                <div style="font-size:12px; opacity:0.65;">Quality Classification</div>
                <div style="font-size:18px; font-weight:600; margin-top:6px;">
                    {classification}
                </div>
            </div>

            <div style="flex:1; min-width:220px; padding:22px; border-radius:16px; background:{card_bg};">
                <div style="font-size:12px; opacity:0.65;">Risk Level</div>
                <div style="font-size:18px; font-weight:600; margin-top:6px;">
                    {risk}
                </div>
            </div>

            <div style="flex:1; min-width:220px; padding:22px; border-radius:16px; background:{card_bg};">
                <div style="font-size:12px; opacity:0.65;">IEEE Compliance</div>
                <div style="font-size:18px; font-weight:600; margin-top:6px;">
                    {ieee_compliance}%
                </div>
            </div>

            <div style="flex:1; min-width:220px; padding:22px; border-radius:16px; background:{card_bg};">
                <div style="font-size:12px; opacity:0.65;">Recommendation</div>
                <div style="font-size:18px; font-weight:600; margin-top:6px;">
                    {recommendation}
                </div>
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                margin-top:18px;
                padding:10px 20px;
                border-radius:30px;
                background-color:{risk_color};
                color:white;
                font-weight:600;
                display:inline-block;">
                Overall Risk Level: {risk}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # --------------------------------------------------
        # QUALITY BREAKDOWN
        # --------------------------------------------------

        st.markdown("### Quality Attribute Breakdown")

        col1, col2 = st.columns(2)

        for i, (category, issues) in enumerate(results.items()):
            column = col1 if i % 2 == 0 else col2
            with column:
                st.markdown(f"**{category}**")
                if issues:
                    for issue in issues:
                        st.error(issue)
                else:
                    st.success("No major issues detected.")

        st.markdown("---")

        # --------------------------------------------------
        # SCORE GAUGE
        # --------------------------------------------------

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score * 10,
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#22c55e"},
                'steps': [
                    {'range': [0, 40], 'color': "#ef4444"},
                    {'range': [40, 70], 'color': "#f59e0b"},
                    {'range': [70, 100], 'color': "#22c55e"}
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------------------------------
        # CONFIDENCE BADGE
        # --------------------------------------------------

        confidence = 85 + score
        badge_color = "#22c55e" if confidence > 90 else "#f59e0b"

        st.markdown(
            f'<div class="badge" style="background-color:{badge_color};color:white;">Model Confidence: {confidence}%</div>',
            unsafe_allow_html=True
        )

        st.markdown("### Improvement Recommendations")

        if suggestions:
            for s in suggestions:
                st.info(s)
        else:
            st.success("Requirement satisfies evaluated quality attributes.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.caption("ReqQuality Pro | Enterprise Requirements Decision Support Interface")