/* jshint esversion: 6 */

// AOS Animation 초기화
window.AOS.init();

// Isotope 활성화 함수
function enableIsotope() {
    const programsContainer = document.getElementById('programs_container');
    if (programsContainer) {
        window.programsIsotope = new Isotope(programsContainer, {
            itemSelector: '.programs-item',
            layoutMode: 'masonry'
        });
        window.AOS.refresh();
    }
}

// 선택된 태그 강조 표시
function flagSelectedTag(selected) {
    document.querySelectorAll('#programs_filter .filter-active').forEach((li) => {
        li.classList.remove('filter-active');
    });
    selected.classList.add('filter-active');
}

// 필터 변경 함수
function changeFilter(event) {
    const filterValue = event.currentTarget.dataset.filter;
    window.programsIsotope.arrange({ filter: filterValue });
    window.programsIsotope.on('arrangeComplete', () => window.AOS.refresh());
    if (event.currentTarget.classList.contains('program-type')) {
        document.querySelectorAll('#programs_filter > *').forEach((fil) => {
            if (filterValue === fil.getAttribute('data-filter')) {
                flagSelectedTag(fil);
            }
        });
    } else {
        flagSelectedTag(event.currentTarget);
    }
}

// 프로그램 필터 설정
function setupProgramsFilter() {
    enableIsotope();
    const programsFilter = document.getElementById('programs_filter').children;
    [...programsFilter, ...document.getElementsByClassName('program-type')].forEach((el) => {
        el.onclick = changeFilter;
    });
}

// 슬라이더 초기 설정
let currentIndex = 0;
const sliderWrapper = document.getElementById('slider-wrapper');
const totalItems = sliderWrapper ? sliderWrapper.children.length : 0;
const itemsPerSlide = 3; // 한 번에 보이는 슬라이더 아이템 수
const itemWidth = 410; // 슬라이더 아이템 너비 (400px + margin-right 10px)

// 슬라이드 이동 함수
function moveSlide() {
    const offset = currentIndex * itemWidth;
    sliderWrapper.style.transform = `translateX(-${offset}px)`;
}

// 다음 슬라이드로 자동 이동
function autoSlide() {
    if (currentIndex < totalItems - itemsPerSlide) {
        currentIndex += 1;
    } else {
        currentIndex = 0; // 마지막 슬라이드에 도달하면 처음으로 돌아감
    }
    moveSlide();
}

// 이전 슬라이드로 이동
function prevSlide() {
    if (currentIndex > 0) {
        currentIndex -= 1;
    }
    moveSlide();
}

// 이벤트 리스너 등록
if (document.getElementById('nextBtn') && document.getElementById('prevBtn')) {
    document.getElementById('nextBtn').addEventListener('click', autoSlide);
    document.getElementById('prevBtn').addEventListener('click', prevSlide);
}

// 슬라이드를 자동으로 넘기기 위한 타이머 설정 (3초마다)
window.setInterval(autoSlide, 3000);
