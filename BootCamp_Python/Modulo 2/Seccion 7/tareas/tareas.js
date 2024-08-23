"use strict";

console.log("----------------------------------------------------");
// Ejercicio 1
var calificacion = parseInt(prompt("Ingrese la calificación"));

if (calificacion>=0 && calificacion<60){
    console.log("Su calificacion es: F");
}else if(calificacion<70){
    console.log("Su calificacion es: D");
}else if(calificacion<80){
    console.log("Su calificacion es: C");
}else if (calificacion<90){
    console.log("Su calificacion es: B");
}if (calificacion<101){
    if(calificacion = 100){
        console.log("Su calificacion es: A, ha obtenido la EXCELENCIA");
    }else{
        console.log("Su calificacion es: A");
    }
}else{
    console.log("La calificacion ingresada no es valida");45
}

console.log("----------------------------------------------------");
// Ejercicio 2
for(let i=0; i<11; i++){
    console.log("Tabla del: " + i);
    for(let y=0;y<11;y++){
        let mult= i*y;
        console.log(i +"x" + y + " = " + mult);
    }
}

// Ejercicio 3
console.log("----------------------------------------------------");
for(let i=1; i<101; i++){
    if( i%2 == 0){
        console.log("El valor: "+ i +" es par");
        if(i%5 == 0){
            console.log(" y es multiplo de 5");
        }

    }else{
        console.log("El valor: "+ i + " es impar ");
        if(i%5 == 0){
            console.log(" y es multiplo de 5");
        }

    }
}

console.log("----------------------------------------------------");

