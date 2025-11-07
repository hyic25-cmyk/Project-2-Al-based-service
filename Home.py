import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu  # <-- 이 줄을 추가하세요!

# --- 페이지 설정 ---
st.set_page_config(
    page_title="Project: Fear Detection",
    page_icon="",
    layout="wide"
)

# --- (st.set_page_config 다음 줄에 넣으세요) ---

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

    /* 4. (중요) 메인 콘텐츠 블록 최대 너비 95%로 강제 */
    div[data-testid="stBlock"] {
        max-width: 80vw !important;
    }
</style>
""", unsafe_allow_html=True)

# --- (↓↓↓ 2. 이 부분을 통째로 추가하세요 ↓↓↓) ---
# --- 가로 내비게이션 바 ---
selected = option_menu(
    menu_title=None,  # 메뉴 제목 (필수) - None으로 하면 안보임
    options=["Home", "Step 1", "Step 2", "Step 3", "Step 4"],  # 메뉴 항목
    menu_icon="cast",  # 메뉴 아이콘 (선택)
    default_index=0,  # 기본으로 선택될 항목 (0=Home)
    orientation="horizontal", # "horizontal" 또는 "vertical"
    styles={
        "container": {"padding": "0!important", "background-color": "#E0E7E9"},
        "nav-link": {
            "font-family": "Lato, sans-serif",
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#A3C6C4"}, # (이 색깔은 맘대로 바꾸세요)
    }
)

# --- 페이지 이동 로직 ---
if selected == "Step 1":
    st.switch_page("pages/1_Step_1.py")
if selected == "Step 2":
    st.switch_page("pages/2_Step_2.py")
if selected == "Step 3":
    st.switch_page("pages/3_Step_3.py")
if selected == "Step 4":
    st.switch_page("pages/4_Step_4.py")

# "Home"이 선택되면 (default_index=0),
# st.switch_page가 실행되지 않고, 그냥 이 파일의 나머지 코드가 실행됩니다.

# --- (↑↑↑ 여기까지 추가 ↑↑↑) ---

# --- (이 아래에 st.title, st.header 등이 이어집니다) ---


# --- 홈 화면 내용 ---
st.title("Project: Finding the 'Scariest Scene'")
st.header("Using Heart Rate and Facial Expression")

st.write("""
Welcome to our project!
Our goal is to find the most surprising or scary moments in a video 
by analyzing a user's real-time biometric data.
""")

st.subheader("How it works:")
st.markdown("""
1.  **Heart Rate Sensing:** We track changes in heart rate.
2.  **Facial Expression Detection:** We analyze facial cues for surprise or fear.
3.  **Data Synchronization:** We pinpoint the exact timestamp in the video when these reactions occur.
""")
