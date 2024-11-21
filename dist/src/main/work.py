from browser import document, window

def sort_by_name(event=None):  # event를 기본값 None으로 설정
    print("눌렸음")
    gallery = document["gallery"]
    items = list(gallery.children)

    # 버튼 이미지 찾기
    button_image = document.select(".sort-button img")[0]  # 버튼 내 이미지 요소 찾기
    current_src = button_image.attrs["src"]

    # 정렬 방식 결정
    if "filter1.webp" in current_src:  # 정렬 기준: 이름순
        items.sort(key=lambda item: item.select(".student-name")[0].text)
        # 버튼 이미지 변경
        button_image.attrs["src"] = "https://cnudesign2024.com/dist/res/image/filter2.webp"
    else:  # 정렬 기준: 이름 역순
        items.sort(key=lambda item: item.select(".student-name")[0].text, reverse=True)
        # 버튼 이미지 변경
        button_image.attrs["src"] = "https://cnudesign2024.com/dist/res/image/filter1.webp"

    # 기존 내용을 지우고 정렬된 순서대로 다시 추가
    gallery.clear()
    for item in items:
        gallery <= item

# 전역 함수로 등록
window.sort_by_name = sort_by_name
