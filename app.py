import streamlit as st

st.set_page_config(page_title="CI/CD App", page_icon="🚀", layout="centered")

st.title("🚀 GitHub Actions + Hugging Face Spaces CI/CD")
st.write("GitHub에 코드를 푸시하면 Hugging Face Space에 Streamlit 앱이 자동으로 배포됩니다.")

st.divider()

# 사용자 입력 영역
name = st.text_input("이름을 입력하세요:", "심종현")
student_id = st.text_input("학번을 입력하세요:", "2355008")

if st.button("인사하기 및 확인"):
    st.success(f"안녕하세요, {name}님 (학번: {student_id})! CI/CD 파이프라인 구축 및 Streamlit 배포에 성공하셨습니다.")
    st.balloons()
