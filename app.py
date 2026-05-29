import streamlit as st

st.set_page_config(
    page_title="면접 코칭 앱",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 AI 면접 코칭 앱")

st.write("면접 질문에 답변하면 피드백을 제공합니다.")

# 질문 선택
question = st.selectbox(
    "면접 질문 선택",
    [
        "자기소개를 해보세요.",
        "지원 동기를 말씀해주세요.",
        "본인의 장점과 단점은 무엇인가요?",
        "협업 경험을 설명해주세요.",
        "갈등을 해결한 경험이 있나요?"
    ]
)

st.subheader("면접 질문")
st.info(question)

# 답변 입력
answer = st.text_area(
    "답변 작성",
    height=200,
    placeholder="여기에 답변을 입력하세요..."
)

# 피드백 버튼
if st.button("피드백 받기"):

    if answer.strip() == "":
        st.warning("답변을 입력해주세요.")
    else:
        st.subheader("📋 피드백")

        feedback = []

        # 길이 체크
        if len(answer) < 30:
            feedback.append("답변이 너무 짧습니다. 조금 더 구체적으로 작성해보세요.")
        else:
            feedback.append("답변 길이가 적절합니다.")

        # 자신감 표현 체크
        confidence_words = ["잘", "성장", "경험", "해결", "노력", "성과"]

        if any(word in answer for word in confidence_words):
            feedback.append("긍정적이고 자신감 있는 표현이 포함되어 있습니다.")
        else:
            feedback.append("경험이나 성과를 강조하면 더 좋습니다.")

        # STAR 방식 힌트
        if len(answer) > 80:
            feedback.append("상황(Situation) - 행동(Action) - 결과(Result) 구조가 보이면 더 좋습니다.")

        for item in feedback:
            st.success(item)

        st.subheader("⭐ 총평")

        if len(answer) > 100:
            st.write("전반적으로 좋은 답변입니다. 구체적인 사례를 추가하면 더 강력해집니다.")
        else:
            st.write("조금 더 자세한 경험과 결과를 포함해보세요.")
