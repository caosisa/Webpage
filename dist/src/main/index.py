from browser import document, window, aio, module_init

# 초기 설정
print, pyprint = module_init(__name__, "index.index")
currentIndex = 0
slider_wrapper = document["slider-wrapper"]
total_items = len(slider_wrapper.children)
items_per_slide = 3  # 한 번에 보이는 슬라이더 아이템 수
item_width = 410  # 슬라이더 아이템 너비 (400px + margin-right 10px)

# 슬라이드 이동 함수
def move_slide():
    global currentIndex
    offset = currentIndex * item_width  # 이동할 너비 계산
    slider_wrapper.style.transform = f"translateX(-{offset}px)"

# 터치 이벤트 변수 초기화
start_x = 0
end_x = 0

# 터치 시작 이벤트 핸들러
def touch_start(event):
    global start_x
    start_x = event.touches[0].clientX  # 터치 시작 시의 x 좌표 저장

# 터치 이동 이벤트 핸들러 (이벤트 처리 중 필요에 따라 사용)
def touch_move(event):
    # 여기에 터치 이동 시의 추가 효과를 줄 수 있음 (예: 부드러운 이동 애니메이션)
    pass

# 터치 종료 이벤트 핸들러
def touch_end(event):
    global currentIndex, start_x, end_x
    end_x = event.changedTouches[0].clientX  # 터치 종료 시의 x 좌표 저장

    # 스와이프 거리 계산
    swipe_distance = end_x - start_x

    # 스와이프 기준에 따른 슬라이드 이동 (오른쪽으로 스와이프한 경우 이전 슬라이드, 왼쪽으로 스와이프한 경우 다음 슬라이드)
    if swipe_distance > 50:  # 오른쪽으로 스와이프 (50px 이상 움직였을 때)
        if currentIndex > 0:
            currentIndex -= 1
    elif swipe_distance < -50:  # 왼쪽으로 스와이프 (50px 이상 움직였을 때)
        if currentIndex < total_items - items_per_slide:
            currentIndex += 1

    # 슬라이드 이동
    move_slide()

# 슬라이더에 터치 이벤트 등록 (모바일 환경에서만 적용)
if window.innerWidth < 768:
    slider_wrapper.bind("touchstart", touch_start)
    slider_wrapper.bind("touchmove", touch_move)
    slider_wrapper.bind("touchend", touch_end)

# 자동 슬라이드 함수
def auto_slide(*args):
    global currentIndex
    if currentIndex < total_items - items_per_slide:
        currentIndex += 1
    else:
        currentIndex = 0  # 마지막 슬라이드에 도달하면 처음으로 돌아감
    move_slide()

# 모바일 화면 너비일 때만 자동 슬라이드 실행
if window.innerWidth < 768:
    # 슬라이드를 자동으로 넘기기 위한 타이머 설정 (예: 3초마다)
    window.setInterval(auto_slide, 3000)  # 3000ms = 3초

# 이전 슬라이드 버튼 클릭 이벤트 핸들러
def prev_slide(event):
    global currentIndex
    if currentIndex > 0:
        currentIndex -= 1
    move_slide()

# 다음 슬라이드 버튼 클릭 이벤트 핸들러
def next_slide(event):
    global currentIndex
    if currentIndex < total_items - items_per_slide:
        currentIndex += 1
    move_slide()

# 화살표 버튼 이벤트 리스너 등록 (웹 환경에서만 적용)
if window.innerWidth >= 768:
    document["nextBtn"].bind("click", next_slide)
    document["prevBtn"].bind("click", prev_slide)
