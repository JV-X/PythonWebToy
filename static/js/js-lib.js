var log = function() {
    console.log.apply(console, arguments)
}

var element = function(sel) {
    return document.querySelector(sel)
}

var time = function(timestamp) {
    var d = new Date(timestamp*1000)
    return d.toLocaleString()
}

var ajax = function(method, type, path, data, responseCallback) {
    var r = new XMLHttpRequest()

    r.open(method, path, true)
    r.setRequestHeader('Content-Type', type)
    r.onreadystatechange = function() {
        if(r.readyState === 4) {
            responseCallback(r.response)
        }
    }
    data = JSON.stringify(data)

    r.send(data)
}

var replaceNewLineCharacter = function(s) {
    return replaceAll(replaceAll(replaceAll(s,"\r\n","<br>"),"\n","<br>"),"\r","<br>")
}

var replaceAll = function(s, search, replacement) {
    return s.replace(new RegExp(search, 'g'), replacement)
}
