import streamlit as st

# 웹페이지의 제목을 설정합니다.
st.title("🎉 드디어 성공! 나의 첫 웹페이지!")

# 텍스트를 작성합니다.
st.header("Streamlit에 오신 것을 환영합니다.")
st.write("파이썬으로 정말 쉽게 웹을 만들 수 있네요!")
st.write("오류도 잘 해결했습니다. 😎")

# 버튼을 만들어 봅니다.
if st.button("이 버튼을 눌러보세요"):
    # 버튼이 눌리면 이모지를 뿌려줍니다.
    st.balloons()
    st.success("버튼 누르기 성공!")