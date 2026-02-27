import streamlit as st
from checker import check_requirement

st.set_page_config(page_title="Academic Requirements Quality Analyzer")

st.title("📘 Automated Requirements Quality Assessment Tool")

st.markdown("""
This research prototype evaluates software requirements according to
quality attributes inspired by IEEE 29148 standard:

- Clarity
- Unambiguity
- Verifiability
- Atomicity
""")

requirement = st.text_area("Enter Requirement Statement")

if st.button("Analyze Requirement"):

    if requirement.strip() == "":
        st.warning("Please enter a requirement statement.")
    else:
        results, suggestions, score = check_requirement(requirement)

        st.subheader("📊 Quality Attribute Evaluation")

        for category, issues in results.items():
            with st.expander(category):
                if issues:
                    for issue in issues:
                        st.error(issue)
                else:
                    st.success("No major issues detected.")

        st.subheader("📈 Overall Quality Score")

        # Better visualization
        if score >= 8:
            st.success(f"High Quality Requirement ({score}/10)")
        elif score >= 5:
            st.warning(f"Moderate Quality Requirement ({score}/10)")
        else:
            st.error(f"Low Quality Requirement ({score}/10)")

        st.progress(score / 10)

        st.subheader("💡 Improvement Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.info(suggestion)
        else:
            st.success("No improvement suggestions needed.")

st.markdown("---")
st.markdown("Prototype developed for research exploration in Software Requirements Engineering.")