function renderMarkdown () {
    var t = element('#id-journal-title')
    var c = element('#id-journal-content')
    var mt = marked(t.innerHTML)
    var mc = marked(c.innerHTML)

    t.innerHTML = mt
    c.innerHTML = mc
}

function __main() {
    renderMarkdown()
}

__main()