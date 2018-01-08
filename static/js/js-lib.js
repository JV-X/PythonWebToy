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
