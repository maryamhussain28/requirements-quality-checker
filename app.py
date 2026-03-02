import streamlit as st
from checker import check_requirement
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ReqQuality Pro",
    layout="wide",
    page_icon="📘"
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
.block-container {
    padding-top: 2rem;
}
.big-title {
    font-size: 38px;
    font-weight: 700;
    color: #0f172a;
}
.subtitle {
    font-size: 18px;
    color: #475569;
}
.section-header {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
}
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR (AUTH + SETTINGS)
# --------------------------------------------------

st.sidebar.title("🔐 Account")

auth_option = st.sidebar.radio("Access", ["Sign In", "Sign Up"])

if auth_option == "Sign In":
    st.sidebar.text_input("Email")
    st.sidebar.text_input("Password", type="password")
    st.sidebar.button("Login")
else:
    st.sidebar.text_input("Full Name")
    st.sidebar.text_input("Email")
    st.sidebar.text_input("Password", type="password")
    st.sidebar.button("Create Account")

st.sidebar.divider()

st.sidebar.title("⚙️ Analysis Settings")

clarity_weight = st.sidebar.slider("Clarity Weight", 0.5, 2.0, 1.0)
ambiguity_weight = st.sidebar.slider("Unambiguity Weight", 0.5, 2.0, 1.0)
verifiability_weight = st.sidebar.slider("Verifiability Weight", 0.5, 2.0, 1.0)
atomicity_weight = st.sidebar.slider("Atomicity Weight", 0.5, 2.0, 1.0)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown('<div class="big-title">ReqQuality Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Enhanced Requirements Quality Evaluation Platform</div>', unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown('<div class="section-header">Requirement Input</div>', unsafe_allow_html=True)

requirement = st.text_area(
    "",
    height=150,
    placeholder="Enter your software requirement statement here..."
)

analyze_button = st.button("🚀 Run Quality Analysis")

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if analyze_button:

    if requirement.strip() == "":
        st.warning("Please enter a requirement statement before analysis.")
    else:
        results, suggestions, score = check_requirement(requirement)

        st.markdown("---")
        st.markdown('<div class="section-header">Quality Attribute Breakdown</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        for idx, (category, issues) in enumerate(results.items()):
            column = col1 if idx % 2 == 0 else col2
            with column:
                st.markdown(f"**{category}**")
                if issues:
                    for issue in issues:
                        st.error(issue)
                else:
                    st.success("No major issues detected.")

        st.markdown("---")

        # --------------------------------------------------
        # SCORE VISUALIZATION
        # --------------------------------------------------

        st.markdown('<div class="section-header">Overall Quality Score</div>', unsafe_allow_html=True)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score * 10,
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2563eb"},
                'steps': [
                    {'range': [0, 40], 'color': "#fee2e2"},
                    {'range': [40, 70], 'color': "#fef3c7"},
                    {'range': [70, 100], 'color': "#dcfce7"},
                ],
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------------------------------
        # SUGGESTIONS
        # --------------------------------------------------

        st.markdown('<div class="section-header">Improvement Recommendations</div>', unsafe_allow_html=True)

        if suggestions:
            for suggestion in suggestions:
                st.info(suggestion)
        else:
            st.success("Requirement meets all evaluated quality attributes.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.markdown(
    '<div class="footer">ReqQuality Pro v1.0 | Research Prototype | Software Engineering for AI</div>',
    unsafe_allow_html=True
)