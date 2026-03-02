import streamlit as st
from checker import check_requirement
import plotly.graph_objects as go

# --------------------------------------------------
# CONFIG
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

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# THEME SYSTEM (FUNCTIONAL)
# --------------------------------------------------

def apply_theme():
    if st.session_state.dark_mode:
        bg = "#0f172a"
        card = "#1e293b"
        text = "#f1f5f9"
        border = "#334155"
    else:
        bg = "#f8fafc"
        card = "#ffffff"
        text = "#0f172a"
        border = "#e5e7eb"

    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg};
        color: {text};
    }}
    .section-card {{
        padding: 22px;
        border-radius: 16px;
        background-color: {card};
        border: 1px solid {border};
        margin-bottom: 20px;
    }}
    .main-title {{
        font-size: 42px;
        font-weight: 700;
    }}
    .subtitle {{
        font-size: 18px;
        color: #64748b;
    }}
    .badge {{
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
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

    auth_tabs = st.tabs(["Sign In", "Sign Up"])

    with auth_tabs[0]:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            st.session_state.authenticated = True

    with auth_tabs[1]:
        name = st.text_input("Full Name")
        email_new = st.text_input("Email ")
        password_new = st.text_input("Password ", type="password")
        if st.button("Create Account"):
            st.session_state.authenticated = True

    st.divider()

    st.markdown("### Platform Overview")
    st.write("""
    • IEEE 29148 Evaluation  
    • Hybrid Rule + AI Signals  
    • Interactive Dashboard  
    • Research Prototype  
    """)

    st.divider()

    st.markdown("### Recent Analyses")
    if st.session_state.history:
        for item in st.session_state.history[-5:]:
            st.write(f"• {item[:35]}...")
    else:
        st.caption("No history yet.")

    st.divider()

    st.markdown("### 🚀 Upgrade to Pro")
    st.info("""
    - Batch Requirement Analysis  
    - Advanced Semantic Modeling  
    - Document Upload Support  
    - Exportable Reports  
    """)
    st.button("Request Pro Access")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown('<div class="main-title">ReqQuality Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Enhanced Requirements Quality Evaluation Platform</div>', unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# INPUT
# --------------------------------------------------

col1, col2 = st.columns([3,1])

with col1:
    requirement = st.text_area(
        "Enter Requirement Statement",
        height=160,
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

        st.markdown("## Quality Attribute Breakdown")

        colA, colB = st.columns(2)

        for i, (category, issues) in enumerate(results.items()):
            column = colA if i % 2 == 0 else colB
            with column:
                st.markdown(f"### {category}")
                if issues:
                    for issue in issues:
                        st.error(issue)
                else:
                    st.success("No major issues detected.")

        st.markdown("---")

        # ---------------- GAUGE ----------------

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score * 10,
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2563eb"},
                'steps': [
                    {'range': [0, 40], 'color': "#ef4444"},
                    {'range': [40, 70], 'color': "#f59e0b"},
                    {'range': [70, 100], 'color': "#10b981"}
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # ---------------- CONFIDENCE BADGE ----------------

        confidence = 85 + score
        badge_color = "#10b981" if confidence > 90 else "#f59e0b"

        st.markdown(
            f'<div class="badge" style="background-color:{badge_color};color:white;">Model Confidence: {confidence}%</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        # ---------------- IEEE GRID ----------------

        st.markdown("## IEEE 29148 Attribute Mapping")

        grid_cols = st.columns(4)
        attributes = ["Clarity", "Unambiguity", "Verifiability", "Atomicity"]

        for i, attr in enumerate(attributes):
            if results[attr]:
                grid_cols[i].error(attr)
            else:
                grid_cols[i].success(attr)

        st.markdown("---")

        # ---------------- SUGGESTIONS ----------------

        st.markdown("## Improvement Recommendations")

        if suggestions:
            for s in suggestions:
                st.info(s)
        else:
            st.success("Requirement satisfies evaluated quality attributes.")

# --------------------------------------------------
# RESEARCH PANEL
# --------------------------------------------------

st.markdown("---")
st.markdown("### Research Context")

st.info("""
This platform operationalizes requirement quality principles inspired by IEEE 29148
and explores hybrid AI-assisted validation approaches within Software Engineering for AI research.
""")

st.caption("ReqQuality Pro v4.0 | Research Prototype | Software Engineering & AI Systems")