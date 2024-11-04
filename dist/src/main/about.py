from browser import document, window

# 교수님 메시지 데이터를 딕셔너리로 저장
professor_messages = {
    "professor1": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 학생들 각자가 자기 테마에 맞춰 열심히 하는 모습을 보며 저도 많은 것을 보며 배웠습니다. 휴일이나, 저녁 밤 늦게까지 과실에 불이 켜져 있고 열심히 고뇌하는 모습에서 장래에 좋은 디자이너들이 될 것이라고 확신하였습니다.",
        "question2": "Q. 졸업 후 사회로 나갈 학생들에게 해주고 싶은 말",
        "answer2": "A. 사회는 학생 때와 전혀 다릅니다. 그리고 졸업과 동시에 여러분들은 사회의 일원으로서 무언가를 사회에 기여해야 합니다. 그러기 위해서는 남은 기간에 열심히 자신의 부족한 점을 채워나가야 합니다. 디자인이 무엇인가에 대하여 다시 한 번 곱씹어보고 늘! 기본에 충실하기를 바랍니다. 특히 아이디어를 잘 내는 디자이너로 성장하는 것이 중요합니다. 졸업 후에 AS가 가능하니 늘 학교에 오시길 바랍니다. 후배들을 위해서 가끔 놀러오세요. 제가 학식은 늘 사주겠습니다...oh,,!",
        "image": "/dist/res/images/professor1.svg"
    },
    "professor2": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 포기하지 않고 끝까지 하려는 모습이 인상깊었습니다.",
        "question2": "Q. 졸업 후 사회로 나갈 학생들에게 해주고 싶은 말",
        "answer2": "A. 졸업전시 끝난 후 취업을 위한 개인별 노력을 당부하며 관련 프로그램도 제공하도록 교수로서 노력하겠습니다.",
        "image": "/dist/res/images/professor2.svg"
    },
    "professor3": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 다른 졸업학년들보다 다들 열심히 했다는 점이 인상이 깊었습니다. 어떻게 보면 이번 4학년 모든 학생들이 빠지지 않고, 열심히 따라와주어서 저에게는 감동이었습니다.",
    },
    "professor4": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 저는 뭐ㅎㅎ 생각보다 조급해지지 않고, 인생은 마라톤같은 것이기 때문에 꾸준히 내가 하고 싶은 것을 하면 훨씬 큰 보상이 되어 돌아올 것입니다. 살아보니까 거기에 가장 큰 원동력은 된다는 긍정의 힘이 중요합니다."
    },
    "professor5": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 저는 여행을 더 많이 다니고 싶었어요. 내가 사랑하는 일 하는 것도 행복했지만 사람을 많이 만나면서 느끼는 경험들이 값지다는걸 몰랐어요. 하고싶은건 다 도전 해 보세요. 막상 해보면 별거 아닙니다."
    },
    "professor6": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 학생들 각자가 자기 테마에 맞춰 열심히 하는 모습을 보며 저도 많은 것을 보며 배웠습니다...",
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
        document["professorQuestion"].text = message["question1"]
        document["professorAnswer"].text = message["answer1"]
        document["professorQuestion"].text = message["question2"]
        document["professorAnswer"].text = message["answer2"]

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
