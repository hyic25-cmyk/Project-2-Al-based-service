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
    default_index=1,  # <-- 1번 (Step 1) 페이지이므로 1로 설정
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
if selected == "Step 2":
    st.switch_page("pages/2_Step_2.py")
if selected == "Step 3":
    st.switch_page("pages/3_Step_3.py")
if selected == "Step 4":
    st.switch_page("pages/4_Step_4.py")
# (Step 1은 현재 페이지이므로 이동 로직 없음)


# --- Step 1 페이지 내용 (이 부분은 파일마다 다르게 수정하세요) ---
st.title("1. Initial Concept ")
st.subheader(""" \
(Week 8~9)
""")
st.header(""" \
Emotion Balancing Lamp - AI Based Emotion Recognition and Mood Feedback System
""")

st.subheader("Problem Context / Background")
st.markdown("""
Our team began with a simple question: “How can we use AI to solve everyday discomforts?”

Many students and office workers struggle with emotional fluctuations while studying or working.
They often experience stress, lethargy, or irritability, and these emotional shifts have a direct impact on concentration and productivity.
However, most people aren’t fully aware of what they’re feeling, nor do they have effective strategies to regulate those emotions.

From this problem, we concluded that there is a need for a system that can automatically detect emotions and provide immediate environmental feedback through lighting and background sound.

<br>

""",unsafe_allow_html=True )

st.subheader("Initial Topic Overview")
st.markdown("""
The Emotion Balancing Lamp recognizes the user’s emotional state using facial expressions and pulse signals, then automatically adjusts the lighting color and background music to help stabilize emotions and improve focus. In short, it is an AI-driven emotional feedback environment.

1️⃣ Input:
            
* Webcam → captures facial expressions
            
* Pulse sensor → collects real-time heart-rate data

2️⃣ Processing:
            
* A TensorFlow/Keras model classifies facial emotions
            
* Heart-rate changes (compared to baseline) are used to refine tension or relaxation levels

3️⃣ Output:
            
* LED color changes based on the detected emotion
            
* Background music that matches emotional state
<br><br>
            
**"This device essentially “visualizes emotions through the environment.”**

<br>
            
""",unsafe_allow_html=True)

st.subheader("Emotion Classification Logic")
st.markdown("""
Instead of classifying every possible emotion, we focused on five that frequently appear during studying or working.

<br>
            
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd  # Pandas 라이브러리를 import

# 1. 샘플 데이터 만들기 (Python 딕셔너리 -> Pandas DataFrame)
data = {
    'Emotion': ['Happy', 'Calm', 'Sad', 'Tense', 'Angry'],
    'Facial Cues': ['Smile, bright eyes', 'Relaxed face', 'Drooped eyes/mouth', 'Frown, focused eyes', 'Furrowed brow'],
    'Heart-Rate Shift': ['Slight ↑', 'Baseline', '↓', '↑', '↑↑'],
    'LED Feedback': ['Scene Warm yellow', 'Sky-blue or white', 'Warm orange', 'Green or blue', 'Red → gradually white'],
    'Music Feedback': ['Light pop or soft jazz', 'Soft piano, nature sounds','Gentle, comforting melodies', 'Slow-tempo, grounding music','Relaxing piano or lo-fi']
}
df = pd.DataFrame(data)

# 2. Streamlit에 표 표시하기
st.markdown("Analysis Data (DataFrame)")
st.dataframe(df, use_container_width=True)

st.markdown("""
The aim is not just recognizing emotions, but helping users notice their emotional state and gently regulate it.

<br>
            
""",unsafe_allow_html=True)

st.subheader("Data Collection & Dataset Preparation")
st.markdown("""
To train the initial model, we needed real facial expression data, so we used the FER-2013 dataset from Kaggle.


* Base dataset: **FER-2013 (Kaggle)**
            
     https://www.kaggle.com/datasets/msambare/fer2013?resource=download")
<br><br>
Our custom 5-class mapping:   
""",unsafe_allow_html=True)
data = {
    'Final Emotion Class': ['Happy', 'Calm', 'Sad', 'Tense', 'Angry'],
    'FER2013 Label': ['happy', 'neutral', 'sad', 'fear', 'angry'],
}

# 2. Streamlit에 표 표시하기
st.dataframe(df, use_container_width=True)

st.markdown("""
Because FER-2013 doesn’t have “Calm” or “Tense,” we used the neutral class for Calm and the fear class for Tense, based on their closest visual patterns.

<br>
            
""",unsafe_allow_html=True)


st.subheader("Data Processing & Cleaning")
st.markdown("""
**Colab preprocessing code:**
            
https://colab.research.google.com/drive/1Clcku-QXBowvr5hw9nE-NOjjkgo_-Wq0?usp=sharing
<br><br>  
            
Since inconsistent image quality directly affects accuracy, we standardized the dataset by removing images that were too dark, too bright, low resolution, or poorly aligned.

* Pre-cleaning actions:
            
  * Used OpenCV-based auto-filtering in Colab
            
  * Removed images with average brightness <25 or >235
            
  * Removed images with resolution under 40 px on either side
            
* Additional processing:
  * Excluded images with blurry or unrecognizable faces
  * Balanced all classes (train: 3,800 per class, test: 800 per class)
  * Standardized filenames to the format emotion_0001.jpg (e.g., happy_0321.jpg)

<br>
            
**Pre-cleaning dataset (v0):**

https://drive.google.com/drive/folders/1Ec3N-PEq-S3eUkJkM35BqooNmESihJ9z?usp=sharing

<br>
            
**Post-cleaning dataset (v1):**
            
https://drive.google.com/drive/folders/1fkepGrkezfcocTwNGEiz48dDEIOpn3W-?usp=sharing
            
<br><br>
            
""", unsafe_allow_html=True)

st.subheader("Insight")
st.markdown("""
* Emotions strongly influence concentration, productivity, and learning ability.
* AI can recognize emotions, and environmental elements like lighting and music can guide emotional regulation.

"The goal is a system that helps users manage their emotions instead of being overwhelmed by them."
<br><br>
**This initial idea eventually evolved into a more dynamic scenario (such as detecting surprise, lie-related tension, etc.) based on the professor’s feedback.**
            """, unsafe_allow_html=True)
