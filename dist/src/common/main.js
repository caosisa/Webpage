// Import 관련 부분은 JavaScript에서 각각 해당 모듈을 직접 로드하는 것으로 대체합니다.

// 현재 연도 가져오기
const currentYear = new Date().getFullYear();

// 템플릿 삽입 함수
async function insertTemplate(templatePath, parent, index = -1, oncomplete = () => {}) {
    const basePath = window.location.pathname;
    let result;
    if (basePath.startsWith("/Webpage/about") || basePath.startsWith("/Webpage/work")) {
        result = await fetch("/dist/res/templates/" + templatePath);
    } else {
        result = await fetch("/dist/res/templates/" + templatePath);
    }

    const htmlStr = await result.text();
    insertElement(htmlStr, parent, index);
    oncomplete();
}

// HTML 요소 삽입
function insertElement(htmlStr, parent, index = -1) {
    if (parent.childNodes.length < index) {
        index = parent.childNodes.length;
    }
    const element = parseHTML(htmlStr.replace("{CURRENT_YEAR}", `${currentYear}`));
    parent.insertBefore(element, parent.childNodes[index]);
}

// HTML 파싱 함수
function parseHTML(htmlStr) {
    const template = document.createElement('template');
    template.innerHTML = htmlStr;
    return template.content;
}

// 네비게이션 활성화 함수
function enableNavigation() {
    const navigation = document.getElementsByClassName('nav-link');
    const navigationMenus = Array.from(navigation).reduce((acc, nav) => {
        acc[nav.getAttribute('href').split('#').pop()] = nav;
        return acc;
    }, {});
    const header = document.getElementById('header');
    const navbar = document.getElementById('navbar');
    const mobileToggles = document.getElementsByClassName('mobile-nav-toggle');

    function scrollTo(section) {
        const offset = header.offsetHeight;
        if (section) {
            const sectionElement = document.getElementById(section.split('#').pop());
            if (sectionElement) {
                const pos = sectionElement.offsetTop;
                window.scrollTo({ top: pos - offset, behavior: "smooth" });
            }
        }
    }

    function navbarClick(event) {
        event.preventDefault();
        if (navbar.classList.contains('navbar-mobile')) {
            navbar.classList.remove('navbar-mobile');
            mobileToggles[0].classList.toggle('hidden');
            mobileToggles[1].classList.toggle('hidden');
        }
        scrollTo(event.target.hash);
    }

    function toggleMenuIcon() {
        navbar.classList.toggle('navbar-mobile');
        mobileToggles[0].classList.toggle('hidden');
        mobileToggles[1].classList.toggle('hidden');
    }

    function enableMobileDropdown(event) {
        if (navbar.classList.contains('navbar-mobile')) {
            event.preventDefault();
            event.target.nextElementSibling.classList.toggle('dropdown-active');
        }
    }

    function traceCurrentScroll() {
        const pos = window.scrollY;
        if (pos > 100) {
            header.classList.add('header-scrolled');
        } else {
            header.classList.remove('header-scrolled');
        }
        const sections = document.getElementsByTagName('section');
        Array.from(sections).forEach((sec) => {
            const menu = navigationMenus[sec.id];
            if (menu) {
                if (sec.offsetTop <= pos + 200 && pos + 200 <= sec.offsetTop + sec.offsetHeight) {
                    menu.classList.add('active');
                } else {
                    menu.classList.remove('active');
                }
            }
        });
    }

    scrollTo(window.location.hash);
    if (window.location.pathname === "/" || window.location.pathname === "/index.html") {
        if (navigationMenus['front']) {
            navigationMenus['front'].classList.add('active');
        }
        Array.from(document.getElementsByClassName('scrollto')).forEach((scrll) => {
            scrll.onclick = navbarClick;
        });
    } else {
        if (!document.getElementById('disable_inner_page_header')) {
            header.classList.add('header-inner-pages');
        }
    }
    traceCurrentScroll();
    window.addEventListener('scroll', traceCurrentScroll);
    Array.from(mobileToggles).forEach((toggle) => {
        toggle.onclick = toggleMenuIcon;
    });
}

// Back to Top 버튼 활성화
function enableBackToTop() {
    const backToTop = document.getElementById('btn-back-to-top');

    function showBackToTopButton() {
        if (backToTop) {
            if (window.scrollY > 100) {
                backToTop.classList.add('active');
            } else {
                backToTop.classList.remove('active');
            }
        }
    }

    showBackToTopButton();
    window.addEventListener('scroll', showBackToTopButton);
    addToHome();
}

// 로고 클릭 시 홈으로 이동
function addToHome() {
    const orgLogo = document.getElementById('org-logo-to-main-page');
    if (orgLogo) {
        orgLogo.addEventListener('click', () => {
            window.location.href = "/";
        });
    }
}

// 템플릿 삽입 및 네비게이션 활성화 실행
insertTemplate("header.html", document.body, 0, enableNavigation);
insertTemplate("footer.html", document.body, -1, enableBackToTop);

// 네비게이션 토글 기능 구현
function toggleNav(event) {
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    const navbar = document.getElementById('navbar').getElementsByTagName('ul')[0];

    if (navbar.classList.contains('active')) {
        navbar.classList.remove('active');
        menuIcon.classList.remove('hidden');
        closeIcon.classList.add('hidden');
    } else {
        navbar.classList.add('active');
        menuIcon.classList.add('hidden');
        closeIcon.classList.remove('hidden');
    }
}

// 모바일 아이콘 이벤트 바인딩
const menuIcon = document.getElementById('menu-icon');
const closeIcon = document.getElementById('close-icon');
if (menuIcon && closeIcon) {
    menuIcon.addEventListener('click', toggleNav);
    closeIcon.addEventListener('click', toggleNav);
}
