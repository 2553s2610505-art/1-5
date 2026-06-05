import streamlit as st
from google import genai

# -------------------
# 페이지 설정
# -------------------
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💕",
    layout="centered"
)

# -------------------
# Gemini 설정
# -------------------
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# -------------------
# 시스템 프롬프트
# -------------------
SYSTEM_PROMPT = """
당신은 전문적인 연애상담 챗봇입니다.

규칙:
1. 항상 한국어로 답변합니다.
2. 사용자의 감정을 존중합니다.
3. 현실적이고 구체적인 조언을 제공합니다.
4. 일방적인 단정은 하지 않습니다.
5. 상대방의 입장도 함께 고려합니다.
6. 폭력, 스토킹, 협박, 자해 관련 내용은 안전을 우선 안내합니다.
7. 답변은 읽기 쉽게 적절히 줄바꿈합니다.
"""

# -------------------
# 제목
# -------------------
st.title("💕 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# -------------------
# 채팅 기록
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요 😊 연애 고민을 편하게 이야기해주세요."
        }
    ]

# 기존 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------
# 사용자 입력
# -------------------
prompt = st.chat_input("연애 고민을 입력하세요...")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 대화 이력 구성
        conversation = SYSTEM_PROMPT + "\n\n"

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                conversation += f"사용자: {msg['content']}\n"
            else:
                conversation += f"상담사: {msg['content']}\n"

        # Gemini 호출
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=conversation
        )

        answer = response.text

    except Exception as e:
        answer = f"⚠️ 오류가 발생했습니다.\n\n{str(e)}"

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# -------------------
# 사이드바
# -------------------
with st.sidebar:
    st.header("설정")

    if st.button("채팅 초기화"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "안녕하세요 😊 연애 고민을 편하게 이야기해주세요."
            }
        ]
        st.rerun()

    st.markdown("---")
    st.write("모델: Gemini 2.5 Flash Lite")
