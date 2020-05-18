function login() {
    var form = $("[id=loginForm]").filter(":visible");
    let data = form.serialize();
    $.post('/login/', data, function (response, status) {
        if (response) {
            let errorsAreas = jQuery('[id=errorsArea]');
            for(let i=0;i<errorsAreas.length; i++) {
                errorsAreas[i].innerText=response;
            }
        } else {
            location.reload()
        }
    });
}
