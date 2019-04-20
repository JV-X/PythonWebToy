function markPV(title) {
    var url = "http://jsonip.com?callback=?"

    $.getJSON(url, function (data) {
        doUploadPV(title, data.ip)
    })
}

function doUploadPV(title, ip) {
    var path = '/pv'
    var form = {}
    var date = Date.now()
    form['time'] = time(date)
    form['ip'] = ip
    form['title'] = title

    ajax("POST", 'application/json', path, form, function (r) {
        log(r)
    })
}

function renderMarkdown() {
    var t = element('#id-journal-title')
    var c = element('#id-journal-content')
    var mt = marked(t.innerHTML)
    var mc = marked(c.innerHTML)

    t.innerHTML = mt
    c.innerHTML = mc

    markPV(t.innerHTML)
}

function __main() {
    renderMarkdown()
}

__main()
