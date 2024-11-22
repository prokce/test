import streamlit as st
import random
import time

# 실험용 문장 데이터
sentences = {
    "active": [
        "The dog chased the cat.",
        "She is reading a book.",
        "He solved the problem."
    ],
    "passive": [
        "The cat was chased by the dog.",
        "A book is being read by her.",
        "The problem was solved by him."
    ]
}

# 타이틀
st.title("수동태/능동태 반응 체크 실험")

# 사용자 입력 초기화
if "results" not in st.session_state:
    st.session_state.results = []
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# 실험 설명
st.write("""
이 실험은 문장이 능동태인지 수동태인지 빠르게 판단하는 테스트입니다.
화면에 문장이 나타나면 아래 버튼 중 하나를 클릭하세요.
""")

# 문장 표시 및 반응 체크
if st.button("문장 생성"):
    sentence_type = random.choice(["active", "passive"])
    sentence = random.choice(sentences[sentence_type])
    st.session_state.start_time = time.time()
    st.session_state.current_sentence = sentence
    st.session_state.current_type = sentence_type

if "current_sentence" in st.session_state:
    st.subheader("문장을 확인하고 선택하세요:")
    st.write(f"**{st.session_state.current_sentence}**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("능동태"):
            reaction_time = time.time() - st.session_state.start_time
            st.session_state.results.append(("active", reaction_time, st.session_state.current_type))
            del st.session_state.current_sentence
    with col2:
        if st.button("수동태"):
            reaction_time = time.time() - st.session_state.start_time
            st.session_state.results.append(("passive", reaction_time, st.session_state.current_type))
            del st.session_state.current_sentence

# 결과 요약
if st.session_state.results:
    st.subheader("실험 결과 요약")
    for idx, (response, time_taken, actual_type) in enumerate(st.session_state.results, 1):
        correctness = "정답" if response == actual_type else "오답"
        st.write(f"문제 {idx}: {correctness} ({actual_type} 문장) - 반응 시간: {time_taken:.2f}초")

# 초기화 버튼
if st.button("결과 초기화"):
    st.session_state.results = []
    st.write("결과가 초기화되었습니다.")
