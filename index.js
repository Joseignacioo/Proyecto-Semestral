//para login
function validar()
{
    var usuario = document.getElementById("user").value;
    var password = document.getElementById("pass").value;
                            
    if(usuario == "administrador" && password =="admin1234")
    {
        // alert("Ingreso correctamente precione aceptar para terminar");
        window.location="admin.html";
        return false;
    }
    if(usuario == "usuario1@gmail.com" && password == "user1234")
    {
        // alert("Ingreso correctamente precione aceptar para terminar");
        window.location="user.html";
        return false;
    }
    else
    {
    alert("Verifique sus datos");
    }
}
