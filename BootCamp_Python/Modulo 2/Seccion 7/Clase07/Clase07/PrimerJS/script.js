"use strict";
// Hola Mundo
console.log("Hola, Mundo!");

// Realizando operaciones matemáticas
var a = 10;
var b = 5;

let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;

console.log("Suma: " + suma);
console.log("Resta: " + resta);
console.log("Multiplicación: " + multiplicacion);
console.log("División: " + division);

// Función para realizar operaciones aritméticas
function realizarOperaciones(a, b) {
    let suma = a + b;
    let resta = a - b;
    let multiplicacion = a * b;
    let division = a / b;

    console.log("Suma: " + suma);
    console.log("Resta: " + resta);
    console.log("Multiplicación: " + multiplicacion);
    console.log("División: " + division);
}

realizarOperaciones(10, 5);

// Trabajando con condicionales
let numero = 10;

if (numero > 0) {
    console.log("El número es positivo.");
} else if (numero < 0) {
    console.log("El número es negativo.");
} else {
    console.log("El número es cero.");
}

let edad = parseInt(prompt("Introduzca su edad: "));
console.log("Tu edad es: " + edad);

let genero = prompt("introduzca su genero: ");
console.log(genero);

if(genero==F){
    console.log("Eres mujer");
}else{
    console.log("Eres hombre");
}


if (edad>=18){
    console.log("Usted es mayor de edad");
} else if (edad>12) {
    console.log("Usted es un adolescente");
} else{
    console.log("Usted es un niño");
}