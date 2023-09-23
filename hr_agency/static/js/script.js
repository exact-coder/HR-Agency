
$(document).ready(function() {
    $(".phone").inputmask("(+999) 999999-99999", {"onincomplete": function() {
        $(".phone").val("");
        swal("Opss!","Incomplete phone. Please review !", "info");
        return false;
    }});
});