import streamlit as st

st.set_page_config(page_title="My App", page_icon="🚀")

st.title("첫 번째 스트림릿 앱")
st.write("GitHub + Streamlit 배포 성공!")
git init
git add .
git commit -m "first app"
git branch -M main
git remote add origin https://github.com/아이디/레포이름.git
git push -u origin main
