$(document).ready(function(){

    $('.text2').hide();
    $(".text1").mouseenter(function() {
        $('.text2').show();
    });

    // Habilidades
    $("#img1").click(function() {
        var idBoton = $("#img1").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img2").click(function() {
        var idBoton = $("#img2").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img3").click(function() {
        var idBoton = $("#img3").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img4").click(function() {
        var idBoton = $("#img4").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img5").click(function() {
        var idBoton = $("#img5").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img6").click(function() {
        var idBoton = $("#img6").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img7").click(function() {
        var idBoton = $("#img7").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });
    $("#img8").click(function() {
        var idBoton = $("#img8").attr("id");
        console.log(idBoton);
        $("#detalles_" + idBoton).toggle();
    });

    $(".btn-close").click(function() {
        $(".detalles").fadeOut();
    });


    // Proyectos;
    $(".pag_1").click(function() {
        $('.pag1').show();
        $('.pag2').hide();
        $('.pag3').hide();
        $('.pag4').hide();
    });
    $(".pag_2").click(function() {
        $('.pag1').hide();
        $('.pag2').show();
        $('.pag3').hide();
        $('.pag4').hide();
    });
    $(".pag_3").click(function() {
        $('.pag1').hide();
        $('.pag2').hide();
        $('.pag3').show();
        $('.pag4').hide();
    });
    $(".pag_4").click(function() {
        $('.pag1').hide();
        $('.pag2').hide();
        $('.pag3').hide();
        $('.pag4').show();
    });
    
    var a = $(".nombre").val();
    console.log(a);
    var b = $(".apellido").val();
    console.log(b);
    var c = $(".correo").val();
    console.log(c);
    var d = $(".numero").val();
    console.log(d);
    var e = $(".mensaje").val();
    console.log(e);

    $("#buttom_enviar").click(function(){
        alert("Hola! " + a +" "+ b + "\nTu solicitud: " +"\'" + e + "\' " + "a  sido ingresada. \nTe contactare ya sea a tu correo: " + c + "\no a tu teléfono: " + d + "\nQue tenga un gran dia!");
    })
    
})