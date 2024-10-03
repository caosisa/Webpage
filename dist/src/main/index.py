from browser import document, window, aio, module_init
print, pyprint = module_init(__name__, "index.index")


########################################################################################################################
# AOS Animation
########################################################################################################################
window.AOS.init()


########################################################################################################################
# Programs List
########################################################################################################################
def enable_isotope():
    programs_container = document.getElementById('programs_container')
    if programs_container:
        window.programs_isotope = window.Isotope.new(programs_container, {
            'itemSelector': ".programs-item",
            'layoutMode': "masonry"
        })
        window.AOS.refresh()


def flag_selected_tag(selected):
    for li in document.getElementById('programs_filter').getElementsByClassName('filter-active'):
        li.classList.remove('filter-active')
    selected.classList.add('filter-active')


def change_filter(event):
    programs_filter = document.getElementById('programs_filter').children
    filter_value = event.currentTarget.dataset.filter
    window.programs_isotope.arrange({'filter': filter_value})
    window.programs_isotope.on('arrangeComplete', lambda _: window.AOS.refresh())
    if 'program-type' in event.currentTarget.classList:
        for fil in programs_filter:
            if filter_value == fil.attributes['data-filter'].nodeValue:
                flag_selected_tag(fil)
                break
    else:
        flag_selected_tag(event.currentTarget)


def setup_programs_filter():
    enable_isotope()
    programs_filter = document.getElementById('programs_filter').children
    for el in programs_filter + list(document.getElementsByClassName('program-type')):
        el.onclick = change_filter

from browser import document, window

# 슬라이더 초기 설정
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

# 다음 버튼 클릭
def next_slide(event):
    global currentIndex
    if currentIndex < total_items - items_per_slide:
        currentIndex += 1
    move_slide()

# 이전 버튼 클릭
def prev_slide(event):
    global currentIndex
    if currentIndex > 0:
        currentIndex -= 1
    move_slide()

# 이벤트 리스너 등록
document["nextBtn"].bind("click", next_slide)
document["prevBtn"].bind("click", prev_slide)



