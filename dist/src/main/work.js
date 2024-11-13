// 이름순으로 정렬 함수
function sortByName() {
    const gallery = document.getElementById('gallery');
    if (gallery) {
        const items = Array.from(gallery.children);
        // gallery-item의 student-name 텍스트 기준으로 정렬
        items.sort((a, b) => {
            const nameA = a.querySelector('.student-name').textContent.trim().toLowerCase();
            const nameB = b.querySelector('.student-name').textContent.trim().toLowerCase();
            return nameA.localeCompare(nameB);
        });
        // 기존 내용을 지우고 정렬된 순서대로 다시 추가
        gallery.innerHTML = '';
        items.forEach(item => gallery.appendChild(item));
    }
}

// sort-by-name 버튼 클릭 이벤트 핸들러 등록
const sortButton = document.getElementById('sort-by-name');
if (sortButton) {
    sortButton.addEventListener('click', sortByName);
}
