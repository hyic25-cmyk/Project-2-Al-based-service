import streamlit as st

# --- Page Configuration (페이지 상단 탭 설정) ---
st.set_page_config(
    page_title="Team Project Log",
    page_icon="🚀"
)

# --- Main Content (메인 콘텐츠) ---
st.title("🚀 Project Activity Log")

# (나중에 여기에 팀 주제를 적으세요)
st.subheader("Project Theme: [Finding Emotional Highlights Using Heart Rate and Facial Expressions]")
st.write("This page tracks our team's weekly progress.")
st.divider() # 구분선

# --- Week 1 ---
st.header("Week 8: Planning & Setup")
st.markdown("""
* **Key Activities:**
    * Initial idea brainstorming.
    * Successfully set up the Streamlit environment.
    * Deployed the first version of this web app!
* **Challenges:**
    * (Enter any challenges faced, e.g., "Python version conflicts")
* **Next Steps:**
    * (Enter plans for Week 2)
""")

# --- Week 2 ---
st.header("Week 9: [Your Title for Week 2]")
st.markdown("""
* **Key Activities:**
    * (Waiting for log update...)
* **Notes:**
    * (Waiting for log update...)
""")

# --- Week 3 (Template) ---
st.header("Week 10: [Your Title for Week 3]")
st.markdown("""
* (Waiting for log update...)
""")


# --- Footer (꼬리말) ---
st.divider()
st.caption("ACDT Group 38")