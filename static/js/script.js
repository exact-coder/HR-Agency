/* --------------------
FULL VALIDATION FORM Using INPUTMASK
-----------------------*/

// (1) Inputmask (Phone)
$(document).ready(function() {
    $(".phone").inputmask("(+999) 999999-99999", {"onincomplete": function() {
        $(".phone").val("");
        swal("Opss!","Incomplete Phone. Please review !", "info");
        return false;
    }});
});

// (2) Input Validation
function validateEmail(email){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateForm() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const experience = document.getElementById("experience").value;
    const skills = document.getElementById("skills").value;
    const file = document.getElementById("file").value;

    if(name == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Name field cannot be empty.","error");
        return false;
    }
    else if(name.split(' ').length < 2){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Your Fullname is required.","info");
        return false;
    }
    else if(age == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Age field cannot be empty.","error");
        return false;
    }
    else if(email == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Email field cannot be empty.","error");
        return false;
    }
    else if(!(validateEmail(email))){
        document.getElementById('email').value="";
        swal("Opss !","Please enter a valid email.","error");
        return false;
    }
    else if(phone == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Phone field cannot be empty.","error");
        return false;
    }
    else if(address == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Address cannot be empty.","error");
        return false;
    }
    else if(experience == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Experience cannot be empty.","error");
        return false;
    }
    else if(skills == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","Skills cannot be empty.","error");
        return false;
    }
    else if(file == ""){
        document.getElementById("bg-spinner").style.display = "none";
        swal("Opss !","File cannot be empty.","error");
        return false;
    }
    else{
        return true;
    }
}
// (2) Clear the form (inside the modal) when the modal is closed.
$("#frontendModel,#backendModel,#fullstackModel").on("hidden.bs.modal", function(){
    $('#frontendModel form')[0].reset();
    $('#backendModel form')[0].reset();
    $('#fullstackModel form')[0].reset();
});


// (3) Maximum allowed upload size 
$(document).ready(function() {
    $("#file").bind("change",function() {
        let a = (this.files[0].size);

        if(a > 2 * 1048576){
            swal("Attention !", "Maximum allowed size is 2mb.","info");
            this.value = "";
        };    
    });    
});

// (4) Allow only letters in Name
$(".name").keyup(function() {
    if (!/^[a-zA-Z _]*$/.test(this.value)){
        this.value = this.value.split(/[^a-zA-Z _]/).join('');
    }
});

// (5) Prevent more than 2 white spaces inside the input name
$(".name").on('keydown', function() {
    let $this =$(this);
    $(this).val($this.val().replace(/(\s{2,})|[^a-zA-Z0-9_']/g, ' ').replace(/^\s*/,''));
});

// (6) Prevent starting with space in all inputs (including textarea)
$("input[type='text'], textarea").on("keypress", function(e) {
    if(e.which == 32 && ! this.value.length)
    e.preventDefault();
});

// (7) Allow only numbers in Age
$(".age").keyup(function() {
    if(!/^[0-9]*$/.test(this.value)){
        this.value = this.value.split(/[^0-9]/).join('');
    }
});

// (8) Script to Lowercase input email
$(document).ready(function() {
    $(".email").keyup(function() {
        this.value = this.value.toLowerCase();
    });
});




/*
1) Email:
regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

2) Only letters (name): /^[a-zA-Z _]*$/

3) Prevent more than 2 white spaces inside the input NAME: (/(\s{2,})|[^a-zA-Z0-9_']/g, ' ')

4) Only numbers (age): !/^[0-9]*$/
*/


// Typed Effect Control
let typed = new Typed('#homeTitle', {
    strings: [
        'are working for you.',
        'offer you the best job.',
        'work with world class IT institution.',
        'are happy to see you.',
    ],    
    typeSpeed:150,
    backSpeed: 100,
    backDelay: 3000,
    loop: true,
})    

