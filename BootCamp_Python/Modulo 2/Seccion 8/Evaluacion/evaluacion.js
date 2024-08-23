// Definiendo los distintos clientes
var cliente1 = {
    id: 1523,
    password:'jon123',
    namecliente: 'Jon Snow',
    saldo: 100000,
};
console.log(cliente1);

var cliente2 = {
    id: 1524,
    password:'rob123',
    namecliente: 'Rob Stark',
    saldo: 80000,
};
console.log(cliente2);

var cliente3 = {
    id: 1525,
    password:'ned123',
    namecliente: 'Ned Stark',
    saldo: 5000000,
};
console.log(cliente3);

alert("Bienvenido a Banco en Linea");

let n = parseInt(prompt("Introduzca su ID "));

let p = prompt("Introduzca su contraseña");

if(n == cliente1.id && p == cliente1.password || n == cliente2.id && p == cliente2.password || n == cliente3.id && p == cliente3.password){
    
    let a = (n == cliente1.id && p == cliente1.password);
    let b = (n == cliente2.id && p == cliente2.password);
    let c = (n == cliente3.id && p == cliente3.password);
    
    var opcion;
    if(a == true){
        opcion = 1;
        alert("Bienvenido " + cliente1.namecliente);
    }else if(b == true){
        opcion = 2;
        alert("Bienvenido " + cliente2.namecliente);
    }else if (c== true){
        opcion = 3;
        alert("Bienvenido " + cliente3.namecliente);
    }else{
        console.log("no se ha encontrado cliente ");
    }

    switch (opcion){
        case 1:
            do{
                var select = parseInt(prompt("Selecciona que desea hacer:  \n1 Ver Saldo \n2 Realizar giro \n3 Realizar deposito \n4 Salir"));
                switch(select){
                    case 1:
                        alert("Su saldo actual es: " + cliente1.saldo);
                        break;
    
                    case 2:
                        var giro = parseInt(prompt("Su saldo actual es: " + cliente1.saldo + "\n ingrese el saldo que desea girar"));
                        if (cliente1.saldo<giro){
                            alert("La cantidad excede el monto maximo");
                        }else{
                            cliente1.saldo = cliente1.saldo - giro;
                            alert("Giro realizado. Su nuevo saldo es: "+ (cliente1.saldo));
                        }
                        break;
                    
                    case 3:
                        var deposito = parseInt(prompt("Su saldo actual es: "+ cliente1.saldo + "\n Ingrese el monto a depositar "));
                        cliente1.saldo = cliente1.saldo + deposito;
                        alert("Su nuevo saldo es: " + cliente1.saldo);
                        break;

                    default:
                        break;

                }
            }
            while(select != 4);

            break;
        
        case 2:
            do{
                var select = parseInt(prompt("Selecciona que desea hacer:  \n1 Ver Saldo \n2 Realizar giro \n3 Realizar deposito \n4 Salir"));
                switch(select){
                    case 1:
                        alert("Su saldo actual es: " + cliente2.saldo);
                        break;
    
                    case 2:
                        var giro = parseInt(prompt("Su saldo actual es: " + cliente2.saldo + "\n ingrese el saldo que desea girar"));
                        if (cliente2.saldo<giro){
                            alert("La cantidad excede el monto maximo");
                        }else{
                            cliente2.saldo = cliente2.saldo - giro;
                            alert("Giro realizado. Su nuevo saldo es: "+ (cliente2.saldo));
                        }
                        break;
                    
                    case 3:
                        var deposito = parseInt(prompt("Su saldo actual es: "+ cliente2.saldo + "\n Ingrese el monto a depositar "));
                        cliente2.saldo = cliente2.saldo + deposito;
                        alert("Su nuevo saldo es: " + cliente2.saldo);
                        break;
                }
                        
            }while(select != 4);
            
            break;
        
        case 3:
            do{
                var select = parseInt(prompt("Selecciona que desea hacer:  \n1 Ver Saldo \n2 Realizar giro \n3 Realizar deposito \n4 Salir"));
                switch(select){
                    case 1:
                        alert("Su saldo actual es: " + cliente3.saldo);
                        break;
    
                    case 2:
                        var giro = parseInt(prompt("Su saldo actual es: " + cliente3.saldo + "\n ingrese el saldo que desea girar"));
                        if (cliente3.saldo<giro){
                            alert("La cantidad excede el monto maximo");
                        }else{
                            cliente3.saldo = cliente3.saldo - giro;
                            alert("Giro realizado. Su nuevo saldo es: "+ (cliente3.saldo));
                        }
                        break;
                    
                    case 3:
                        var deposito = parseInt(prompt("Su saldo actual es: "+ cliente3.saldo + "\n Ingrese el monto a depositar "));
                        cliente3.saldo = cliente3.saldo + deposito;
                        alert("Su nuevo saldo es: " + cliente3.saldo);
                        break;
                }
                        
            }while(select != 4);
            
            break;

}

}else{
    alert("Los datos ingressados no son valido intente nuevamenete...");
}
