/* --------------------
FULL VALIDATION FORM
-----------------------*/

// (1) Inputmask (Phone)
$(document).ready(function() {
    $(".phone").inputmask("(+999) 999999-99999", {"onincomplete": function() {
        $(".phone").val("");
        swal("Opss!","Incomplete phone. Please review !", "info");
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
        swal("Opss !","Name field cannot be empty.","error");
        return false;
    }
    else if(age == ""){
        swal("Opss !","Age field cannot be empty.","error");
        return false;
    }
    else if(email == ""){
        swal("Opss !","Email field cannot be empty.","error");
        return false;
    }
    else if(phone == ""){
        swal("Opss !","Phone field cannot be empty.","error");
        return false;
    }
    else if(address == ""){
        swal("Opss !","Address cannot be empty.","error");
        return false;
    }
    else if(experience == ""){
        swal("Opss !","Experience cannot be empty.","error");
        return false;
    }
    else if(skills == ""){
        swal("Opss !","Skills cannot be empty.","error");
        return false;
    }
    else if(file == ""){
        swal("Opss !","File cannot be empty.","error");
        return false;
    }
    else{
        return true;
    }
}

/*
1) Email:
regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

2) Only letters (name): /^[a-zA-Z _]*$/

3) Prevent more than 2 white spaces inside the input NAME: (/(\s{2,})|[^a-zA-Z0-9_']/g, ' ')

4) Only numbers (age): !/^[0-9]*$/
*/