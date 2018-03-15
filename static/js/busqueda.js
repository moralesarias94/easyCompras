$("#boton-busqueda").click(function(event){
    event.preventDefault()
    var buscar = $("#busqueda").val();
    console.log(buscar)
    if (buscar != ""){
        var getUrl = window.location;
        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/";
        window.location.href = baseUrl + "inicio/" + buscar;
    }
});
