import browser
from browser import document, window, aio


def module_init(_id, module_name):
    import sys
    sys.modules[module_name] = sys.modules[_id]
    return window.console.log, print


print, pyprint = module_init(__name__, "judge.judge")
browser.__dict__['module_init'] = module_init


cached_width = 0


def embed_resizer(e=None):
    global cached_width

    if cached_width >= document.body.offsetWidth:
        return

    cached_width = document.body.offsetWidth

    footer_height = 0
    footer = document.getElementById('footer')
    if footer:
        footer_height = footer.offsetHeight

    # iframe 높이 조정
    if 'judge_iframe' in document:
        iframe = document['judge_iframe']
        sc_height = iframe.contentWindow.document.body.scrollHeight
        iframe.style.height = f"calc(100vh + {sc_height}px - {footer_height}px - {footer_height}px)"
        print(iframe.style.height)


async def insert_template(template_path: str, parent, index: int = -1, oncomplete=lambda: None):
    result = await window.fetch("/dist/res/templates/"+template_path)

    insert_element(await result.text(), parent, index)

    window.addEventListener('resize', embed_resizer)
    embed_resizer()

    oncomplete()


def insert_element(htmlstr: str, parent, index: int = -1):
    if parent.childNodes.length < index:
        index = parent.childNodes.length
    parent.insertBefore(parse_html(htmlstr), parent.childNodes[index])


def parse_html(htmlstr: str):
    template = document.createElement('template')
    template.innerHTML = htmlstr
    return template.content


def add_to_home():
    if 'org-logo-to-main-page' in document:
        def event_handler(_):
            window.location.href = "/"
        document['org-logo-to-main-page'].addEventListener('click', event_handler)


# Insert Templates
aio.run(insert_template("footer.html", document.body, -1, add_to_home))

'''
# Iframe url change listener
if 'judge_iframe' in document:
    print("hello")
    def pop_handler(event):
        print("hello3")
        iframe_url = event.newURL
        root_url = event.target.root_url
        print("NEW:", iframe_url)
        src_url = "/judge/" + iframe_url.replace(root_url, "?")

        # Adds a new entry to the history and changes the url in the browser.
        window.history.pushState(src_url)

    print("hello2")
    document['judge_iframe'].contentWindow.history.popState(pop_handler)
'''