import streamlit as st
from streamlit_option_menu import option_menu  # <-- 이 줄을 추가하세요!

# --- Lato 폰트 + 사이드바 숨기기 + 너비 95% 강제 설정 ---
st.markdown("""
<style>
    /* 1. Google Font @import (Lato) */
    @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

    /* 2. 전체 폰트 적용 (Lato) */
    html, body, [class*="st-"], [class*="css-"], h1, h2, h3, h4, h5, h6 { 
        font-family: "Lato", serif !important;
        font-weight: 400;
        font-style: normal;
    }

    /* 3. 기존의 사이드바 숨기기 코드 */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    button[title="Open navigation"] {
        display: none;
    }

    /* 4. (중요) 메인 콘텐츠 블록 최대 너비 80%로 강제 */
    div[data-testid="stBlock"] {
        max-width: 80vw !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 가로 내비게이션 바 ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Step 1", "Step 2", "Step 3", "Step 4"],
    menu_icon="cast",
    default_index=4,  # <-- 1번 (Step 1) 페이지이므로 1로 설정
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#E0E7E9"},
        "nav-link": {
            "font-family": "Lato, sans-serif",
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#A3C6C4"},
    }
)

# --- 페이지 이동 로직 ---
if selected == "Home":
    st.switch_page("Home.py")
if selected == "Step 1":
    st.switch_page("pages/1_Step_1.py")
if selected == "Step 2":
    st.switch_page("pages/2_Step_2.py")
if selected == "Step 3":
    st.switch_page("pages/3_Step_3.py")



# --- Step 4 페이지 내용 (이 부분은 파일마다 다르게 수정하세요) ---
st.title("1. Initial Concept ")
st.subheader(""" \
(Week 8~9)
""")
st.subheader(""" \
Emotion Balancing Lamp - AI Based Emotion Recognition and Mood Feedback System
""")

st.markdown("""
* (Log your activities here)
* (Log your activities here)
""")

st.header("Challenges")
st.markdown("""
* (Log your challenges here)
""")

st.header("Next Steps")
st.markdown("""
* (Log your plans here)
""")