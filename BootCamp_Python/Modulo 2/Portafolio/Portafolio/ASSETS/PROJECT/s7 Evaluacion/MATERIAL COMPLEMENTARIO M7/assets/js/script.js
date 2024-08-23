var opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas");
var opcion = parseInt(opcion);


//FUNCIONES

switch (opcion){
    case 1:
        caso = parseInt(prompt("Seleccione una opción \n1 Ver Boleta  \n2 Pagar Cuenta"));
        if (caso = 1){
            alert("Haga clic aquí para descargar su boleta");
        }else{
            alert("Usted esta siendo transferido. Espere por favor...");
        }
        break;
    case 2:
        caso = prompt("Seleccione una opción \n1 Problemas de señal  \n2 Problemas con las llamadas");
        if (caso == 1 || caso == 2){
            solicitud = prompt("A continuacion escriba su solicitud");
            alert("Estimado usuario su solicitud: " + solicitud + " Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
        }
        break;

    case 3:
        caso = prompt("¡Mentel tiene una oferta comercial acorde a tus necesidades! \n para conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamara. De lo contrario ingrese 'NO'");

        if (caso == 'SI' || caso == 'si'){
            alert("Un ejecutivo contactará con usted");
        }else if (caso == 'NO' || caso == 'no'){
            alert("Gracias por preferir nuestros servicios");
        }else{
            alert("La opcion ingresada no es valida");
        }
        break;
    case 4:
        caso = prompt("A continuación escriba su consulta")
        alert("Estimado usuario, su consulta: " + caso + " Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
        break;

    default:
        alert("La opcion ingresada no es válida. Gracias por preferir nuestros servicios");
        break;
}