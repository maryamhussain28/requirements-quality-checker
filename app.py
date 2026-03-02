import streamlit as st
from checker import check_requirement
import plotly.graph_objects as go

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(page_title="ReqQuality Pro", layout="wide")

# --------------------------------------------------
# SESSION STATE (History)
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("ReqQuality Pro")

dark_mode = st.sidebar.toggle("🌙 Dark Mode")

st.sidebar.divider()

st.sidebar.title("Analysis Settings")
sensitivity = st.sidebar.slider("Strictness Level", 1, 5, 3)

st.sidebar.divider()

st.sidebar.title("📜 History")

if st.session_state.history:
    for item in st.session_state.history[-5:]:
        st.sidebar.write(f"• {item[:40]}...")
else:
    st.sidebar.write("No previous analyses.")

st.sidebar.divider()

st.sidebar.markdown("### 🚀 Upgrade to Pro")
st.sidebar.info("""
Pro version includes:
- AI-powered rewriting
- Batch document analysis
- Exportable PDF reports
- Advanced semantic clustering
""")

st.sidebar.button("Upgrade Now")

# --------------------------------------------------
# THEME STYLING
# --------------------------------------------------

if dark_mode:
    bg_color = "#0f172a"
    text_color = "#f1f5f9"
    card_color = "#1e293b"
else:
    bg_color = "#f8fafc"
    text_color = "#0f172a"
    card_color = "#ffffff"

st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
    color: {text_color};
}}
.big-title {{
    font-size: 40px;
    font-weight: 700;
}}
.section {{
    padding: 20px;
    border-radius: 12px;
    background-color: {card_color};
    margin-bottom: 20px;
}}
.badge {{
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown('<div class="big-title">ReqQuality Pro</div>', unsafe_allow_html=True)
st.caption("AI-Enhanced Requirements Quality Evaluation Platform")

st.markdown("---")

# --------------------------------------------------
# INPUT
# --------------------------------------------------

st.markdown("### Requirement Input")
requirement = st.text_area("", height=150)

analyze = st.button("Run Analysis")

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if analyze:

    if requirement.strip() == "":
        st.warning("Please enter a requirement statement.")
    else:

        results, suggestions, score = check_requirement(requirement)

        st.session_state.history.append(requirement)

        st.markdown("## 📊 Quality Analysis")

        cols = st.columns(2)

        for i, (category, issues) in enumerate(results.items()):
            with cols[i % 2]:
                st.markdown(f"### {category}")
                if issues:
                    for issue in issues:
                        st.error(issue)
                else:
                    st.success("No major issues detected.")

        st.markdown("---")

        # ---------------- SCORE METER ----------------

        st.markdown("## 📈 Overall Quality Score")

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

        confidence = 80 + score
        if confidence > 95:
            badge_color = "#10b981"
        elif confidence > 85:
            badge_color = "#f59e0b"
        else:
            badge_color = "#ef4444"

        st.markdown(
            f'<div class="badge" style="background-color:{badge_color};color:white;">AI Confidence: {confidence}%</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        # ---------------- IEEE GRID ----------------

        st.markdown("## 📘 IEEE 29148 Quality Mapping")

        ieee_cols = st.columns(4)
        attributes = ["Clarity", "Unambiguity", "Verifiability", "Atomicity"]

        for i, attr in enumerate(attributes):
            if results[attr]:
                ieee_cols[i].error(attr)
            else:
                ieee_cols[i].success(attr)

        st.markdown("---")

        # ---------------- SUGGESTIONS ----------------

        st.markdown("## 💡 Improvement Suggestions")

        if suggestions:
            for s in suggestions:
                st.info(s)
        else:
            st.success("Requirement satisfies evaluated quality attributes.")

# --------------------------------------------------
# RESEARCH PANEL
# --------------------------------------------------

st.markdown("---")
st.markdown("### 📚 Research Context")

st.info("""
This prototype draws inspiration from IEEE 29148 standard for
requirements specification quality attributes and explores
hybrid rule-based and AI-assisted evaluation techniques
within Software Engineering for AI research.
""")

st.markdown("---")
st.caption("ReqQuality Pro v2.0 | Research Prototype | Software Engineering & AI Systems")