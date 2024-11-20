from browser import document, window

def sort_by_name(event):
    gallery = document["gallery"]
    items = list(gallery.children)

    # gallery-item의 student-name 텍스트 기준으로 정렬
    items.sort(key=lambda item: item.select(".student-name")[0].text)

    # 기존 내용을 지우고 정렬된 순서대로 다시 추가
    gallery.clear()
    for item in items:
        gallery <= item

# 전역 함수로 등록
window.sort_by_name = sort_by_name
