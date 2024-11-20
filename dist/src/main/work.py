from browser import document, window

def sort_by_name(event=None):  # event를 기본값 None으로 설정
    print("눌렸음")
    gallery = document["gallery"]
    items = list(gallery.children)

    # gallery-item의 student-name 텍스트 기준으로 정렬
    items.sort(key=lambda item: item.select(".student-name")[0].text)

    # 기존 내용을 지우고 정렬된 순서대로 다시 추가
    gallery.clear()
    for item in items:
        gallery <= item

    # 버튼 이미지 교체 로직
    button_image = document.select(".sort-button img")[0]  # 버튼 내 이미지 요소 찾기
    current_src = button_image.attrs["src"]

    # 이미지 파일 이름 변경
    if "filter.svg" in current_src:
        button_image.attrs["src"] = "https://cnudesign2024.com/dist/res/image/filter2.svg"
    else:
        button_image.attrs["src"] = "https://cnudesign2024.com/dist/res/image/filter.svg"

# 전역 함수로 등록
window.sort_by_name = sort_by_name
