var apiDoAuth = function(form, callback) {
    var path = '/api/auth'
    ajax('POST', path, form, callback)
}

var doAuthByKeyFile = function(f) {
    var form = {
       key: f.target.result,
    }

    apiDoAuth(form, function(r) {
        document.documentElement.innerHTML = r
    })
}

var bindEventKeyFileSelect = function() {
    var onKeyFileSelected = function() {
        var f = this.files[0]
        var r = new FileReader();
        r.onload = doAuthByKeyFile
        r.readAsText(f);
    }
    var p = element('#id-praetorian')

    p.addEventListener('change', onKeyFileSelected, false)
}

var bindEvent = function() {
    bindEventKeyFileSelect()
}

var __main = function() {
    bindEvent()
}

__main()