var log = function() {
    console.log.apply(console, arguments)
}

var element = function(sel) {
    return document.querySelector(sel)
}

var timeString = function(timestamp) {
    var d = new Date(timestamp*1000)
    return d.toLocaleString()
}

var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()

    r.open(method, path, true)
    r.setRequestHeader('Content-Type', 'application/json')
    r.onreadystatechange = function() {
        if(r.readyState === 4) {
            responseCallback(r.response)
        }
    }
    data = JSON.stringify(data)

    r.send(data)
}
