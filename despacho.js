// para  registrar
function envio()
{
    var nombre = document.getElementById("name").value
    var correo = document.getElementById("email").value
    var fono = document.getElementById("fono").value
    var direccion = document.getElementById("direccion").value

    if(nombre && correo && fono && direccion){
        if(nombre.length>=6){
            if(correo.includes("@gmail")||correo.includes("@hotmail")||correo.includes("@outlook")){
                if(fono.length>=9){
                    alert("ENVIO CORRECTAMENTE DEL PRODUCTO");
                    window.location="index.html";
                    return false;
                }
                else{
                    alert("El telefono no tiene el rango")
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




