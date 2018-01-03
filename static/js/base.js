var bindEventKeyFileSelect = function() {
    var onKeyFileSelected = function() {
        var f = this.files[0]
        var r = new FileReader();
        r.onload = function(e) {
             log(e.target.result)
        }

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