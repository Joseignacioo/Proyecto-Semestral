//para login
function validar()
{
    var usuario = document.getElementById("user").value;
    var password = document.getElementById("pass").value;
                            
    if(usuario == "administrador" && password =="admin1234")
    {
        alert("Ingreso correctamente a su cuenta precione aceptar para terminar");
        window.location="admin.html";
        return false;
    }
    if(usuario == "usuario1@gmail.com" && password == "user1234")
    {
        alert("Ingreso correctamente precione aceptar para terminar");
        window.location="user.html";
        return false;
    }
    else
    {
    alert("Verifique sus datos");
    }
}
// para  registrar
function registrar()
{
    var nombre = document.getElementById("name").value;
    var correo = document.getElementById("email").value;
    var contraseña = document.getElementById("pass1").value;
    var condiciones = document.getElementById("check2").checked;

    if(nombre && correo && contraseña){
        if(nombre.length>=6){
            if(correo.includes("@gmail")||correo.includes("@hotmail")||correo.includes("@outlook")){
                if(contraseña.length>=6){
                    if(condiciones){
                        alert("Registrado correctamente");
                        window.location="user.html";
                        return false;
                    }
                    else{
                        alert("Debe aceptar terminos y condiciones")
                    }
                }
                else{
                    alert("La contraseña debe contener al menos 6 caracteres")
                }
            }
            else{
                alert("falta el domino de correo")
            }
        }
        else{
            alert("El nombre debe contener al menos 6 caracteres")
        }
    }
    else{
        alert("Le falta rellenar algunos campo");
    }
}
