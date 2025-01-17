from browser import document, window
# 교수님 메시지 데이터를 딕셔너리로 저장
professor_messages = {
    "professor1": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 학생들 각자가 자기 테마에 맞춰 열심히 하는 모습을 보며 저도 많은 것을 보며 배웠습니다. 휴일이나, 저녁 밤 늦게까지 과실에 불이 켜져 있고 열심히 고뇌하는 모습에서 장래에 좋은 디자이너들이 될 것이라고 확신하였습니다.",
        "question2": "Q. 졸업 후 사회로 나갈 학생들에게 해주고 싶은 말",
        "answer2": "A. 사회는 학생 때와 전혀 다릅니다. 그리고 졸업과 동시에 여러분들은 사회의 일원으로서 무언가를 사회에 기여해야 합니다. 그러기 위해서는 남은 기간에 열심히 자신의 부족한 점을 채워나가야 합니다. 디자인이 무엇인가에 대하여 다시 한 번 곱씹어보고 늘! 기본에 충실하기를 바랍니다. 특히 아이디어를 잘 내는 디자이너로 성장하는 것이 중요합니다. 졸업 후에 AS가 가능하니 늘 학교에 오시길 바랍니다. 후배들을 위해서 가끔 놀러오세요. 제가 학식은 늘 사주겠습니다...oh,,!",
        "image": "https://cnudesign2024.com/dist/res/image/professor1.webp"
    },
    "professor2": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 포기하지 않고 끝까지 하려는 모습이 인상깊었습니다.",
        "question2": "Q. 졸업 후 사회로 나갈 학생들에게 해주고 싶은 말",
        "answer2": "A. 졸업전시 끝난 후 취업을 위한 개인별 노력을 당부하며 관련 프로그램도 제공하도록 교수로서 노력하겠습니다.",
        "image": "https://cnudesign2024.com/dist/res/image/professor2.webp"
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
        "answer1": "A. 모두 작지만 소소한 꿈을 갖도록 합시다. 자신의 꿈을 가지지 않으면 결국 타인의 꿈을 쫓게 될 것입니다. 꿈은 변화 되어도 좋으니, 자신만의 목표를 세워 진정한 행복을 찾는 것이 즐거운 인생이 아닐까 생각 합니다."
    },
    "professor6": {
        "question1": "Q. 2024년도 졸업 지도를 하면서 인상 깊었던 점",
        "answer1": "A. 저는 여행을 더 많이 다니고 싶었어요. 내가 사랑하는 일 하는 것도 행복했지만 사람을 많이 만나면서 느끼는 경험들이 값지다는걸 몰랐어요. 하고싶은건 다 도전 해 보세요. 막상 해보면 별거 아닙니다."
    }
}
print("Brython is running")

# 버튼 클릭 이벤트 핸들러
# 버튼 클릭 이벤트 핸들러
def show_message(event):
    print("show_message called")
    professor_id = None
    # 이벤트 객체가 유효한지 확인
    if hasattr(event, "target") and hasattr(event.target, "id"):
        professor_id = event.target.id
    elif isinstance(event, dict) and "target" in event:
        professor_id = event["target"].id
    else:
        print("Invalid event or target")
        return

    print(f"Processing professor_id: {professor_id}")

    # 버튼 스타일 초기화
    for button in document.select(".professor-button"):
        button.style.backgroundColor = "#162A3F"
        button.style.color = "#FFFFFF"

    # 선택된 버튼 스타일 설정
    selected_button = document.getElementById(professor_id)
    if selected_button:
        selected_button.style.backgroundColor = "#FFCEDE"
        selected_button.style.color = "#162A3F"
        selected_button.style.fontWeight = "bold"

    # 메시지 가져오기
    message = professor_messages.get(professor_id, {})
    if message:
        document["professorQuestion1"].text = message.get("question1", "")
        document["professorAnswer1"].text = message.get("answer1", "")
        document["professorQuestion2"].text = message.get("question2", "")
        document["professorAnswer2"].text = message.get("answer2", "")

        # 이미지 설정
        image_element = document["professorImage"]
        if "image" in message:
            image_element.attrs["src"] = message["image"]
            image_element.style.display = "block"
        else:
            image_element.style.display = "none"

        # 상세 박스 표시
        document["professorDetailBox"].style.display = "block"
    else:
        print(f"No message found for professor_id: {professor_id}")

# 각 버튼에 클릭 이벤트 핸들러 연결
def bind_buttons():
    print("bind_buttons called")
    try:
        for professor_id in professor_messages:
            button = document.getElementById(professor_id)
            if button:
                button.bind("click", show_message)
                print(f"Button {professor_id} bound successfully")
            else:
                print(f"Button {professor_id} not found")

        # 기본 선택 버튼 설정
        first_button_id = "professor1"
        first_button = document.getElementById(first_button_id)
        if first_button:
            first_button.style.backgroundColor = "#FFCEDE"
            first_button.style.color = "#162A3F"
            show_message({"target": first_button})  # 이벤트 객체 모방
        else:
            print(f"First button {first_button_id} not found")
    except Exception as e:
        print(f"Error in bind_buttons: {e}")

# Brython 네임스페이스에 함수 등록
window.bind_buttons = bind_buttons
window.show_message = show_message
bind_buttons()