from browser import document, window

# 교수님 메시지 데이터를 딕셔너리로 저장
professor_messages = {
    "professor1": {
        "question": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer": "A. 학생들 각자가 자기 테마에 맞춰 열심히 하는 모습을 보며 저도 많은 것을 보며 배웠습니다...",
        "image": "/dist/res/images/professor1.jpg"
    },
    "professor2": {
        "question": "Q. 졸업 후 사회로 나갈 학생들에게 해주고 싶은 말",
        "answer": "A. 사회는 학생 때와 전혀 다릅니다... 졸업 후에 AS가 가능하니 늘 학교에 오시길 바랍니다...",
        "image": "/dist/res/images/professor2.jpg"
    },
    "professor3": {
        "question": "Q. 학생들의 창의적인 작업에 대한 의견",
        "answer": "A. 여러분의 창의적인 작업과 열정적인 태도는 매우 감명 깊었습니다. 계속해서 자신의 길을 개척하세요."
    },
    "professor4": {
        "question": "Q. 디자인의 중요성에 대해",
        "answer": "A. 디자인은 단순한 시각적 아름다움이 아니라 문제 해결의 도구입니다. 졸업 후에도 이 점을 잊지 마세요."
    },
    "professor5": {
        "question": "Q. 여러분의 미래를 응원합니다",
        "answer": "A. 졸업을 축하합니다! 여러분의 밝은 미래를 응원합니다. 언제든 도움이나 조언이 필요하면 찾아오세요."
    },
    "professor6": {
        "question": "Q. 여러분의 미래를 응원합니다",
        "answer": "A. 졸업을 축하합니다! 여러분의 밝은 미래를 응원합니다. 언제든 도움이나 조언이 필요하면 찾아오세요."
    }
}

# 버튼 클릭 이벤트 핸들러
def show_message(event):
    professor_id = event.target.id

    # 모든 버튼의 색상을 기본값으로 초기화
    for button in document.getElementsByClassName("professor-button"):
        button.classList.remove("selected")

    # 선택된 버튼의 색상을 변경
    event.target.classList.add("selected")

    # 메시지 가져오기
    message = professor_messages.get(professor_id, {})
    if message:
        document["professorQuestion"].text = message["question"]
        document["professorAnswer"].text = message["answer"]

        # 교수님 1, 2의 경우 이미지를 추가
        if "image" in message:
            document["professorImage"].attrs["src"] = message["image"]
            document["professorImage"].style.display = "block"
        else:
            document["professorImage"].style.display = "none"

# 각 교수님 버튼에 클릭 이벤트 연결
def bind_buttons():
    for professor_id in professor_messages:
        document[professor_id].bind("click", show_message)

# HTML 문서가 완전히 로드된 후 실행될 수 있도록 설정
window.onload = bind_buttons
