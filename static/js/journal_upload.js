var apiUpload = function(form, callback) {
    var path = '/api/upload'
    ajax('POST','application/json', path, form, callback)
}

var bindEventFileSelect = function() {
    var onFileSelected = function() {
        var f = this.files[0]
        var formData = new FormData();
        formData.append('files[]', f, f.name);
        apiUpload(formData, function(r) {
            log("uploaded")
        })
    }
    var p = element('#id-upload-journal')
    p.addEventListener('change', onFileSelected, false)
}

var bindEvent = function() {
    bindEventFileSelect()
}

var __main = function() {
    bindEvent()
}

__main()