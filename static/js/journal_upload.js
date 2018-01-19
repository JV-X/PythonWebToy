var apiUpload = function(form, callback) {
    var path = '/api/upload'
    ajax('POST','application/json', path, form, callback)
}
var parse_file = function(f) {
    var raw =  f.target.result.split("<Separator1>")
    var config = raw[0]
    var cs = config.split("<Separator2>")
    var form = {
       content: replaceNewLineCharacter(raw[1])
    }

    for(var i = 0; i < cs.length; i++) {
        var e = cs[i].split("|")
        form[e[0]] = e[1]
    }

    return form
}

var doUploadFile = function(fileContent) {
    var form = parse_file(fileContent)

    apiUpload(form, function(p) {
        log("uploaded")
    })
}

var bindEventFileSelect = function() {
    var onFileSelected = function() {
        var f = this.files[0]
        var r = new FileReader();
        r.onload = doUploadFile
        r.readAsText(f);
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