function sub(){
    var correo = document.getElementById("correo2").value;
    if(correo){
        if(correo.includes("@gmail")||correo.includes("@hotmail")||correo.includes("@outlook")){
            alert("Gracias por ser parte de la Fundacion")
        }
        else{
            alert("falta el domino de correo")
        }
    }
    else{
        alert("Le falta rellenar algunos campo");
    }
}