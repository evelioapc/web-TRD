function validateUser(){
    var nombre = document.getElementById("nombre");
    var apellidos = document.getElementById("apellidos");
    var ci = document.getElementById("ci");
    var alertDiv = document.getElementById("alertDiv");
    var alertLabel = document.getElementById("alertText");

    if (nombre.value === "" || apellidos.value === "" || ci.value === ""){
        alertLabel.textContent= "Debe llenar todos los campos";
        alertDiv.classList.remove("hide");
        alertDiv.classList.add("show");
        return false;
    }
    else if (ci.value.length !== 11){
        alertLabel.textContent= "El campo ci debe tener 11 dígitos";
        alertDiv.classList.remove("hide");
        alertDiv.classList.add("show");
        return false;
    }

    return true;
}

function validateAccount(){
    var user = document.getElementById("username");
    var password = document.getElementById("password");
    var passwordConfirm = document.getElementById("passwordConfirm");
    var alertDiv = document.getElementById("alertDiv");
    var alertLabel = document.getElementById("alertText");

    if (user.value === "" || password.value === "" || passwordConfirm.value === ""){
        alertLabel.textContent= "Debe llenar todos los campos";
        alertDiv.classList.remove("hide");
        alertDiv.classList.add("show");
        return false;
    }
    else if(password.value !== passwordConfirm.value){
        alertLabel.textContent= "Las contraseñas no coinciden";
        alertDiv.classList.remove("hide");
        alertDiv.classList.add("show");
        return false;
    }

    return true;
}

function hideAlert(){
    var alertLabel = document.getElementById("alertText");
    var alertDiv = document.getElementById("alertDiv");
    alertDiv.classList.remove("show");
    alertDiv.classList.add("hide");
    alertLabel.textContent = "";
}