
var numero1, numero2;

numero1 = parseInt(prompt("Ingrese el primer numero"));

numero2 = parseInt(prompt("Ingrese el segundo numero"));


if (numero1>numero2){
    console.log(numero1 + " es mayor que " + numero2);
    alert(numero1 + " es mayor que " + numero2);
} else if (numero2>numero1){
    console.log(numero2 + " es mayor que " + numero1);
    alert(numero2 + " es mayor que " + numero1);
}else{
    console.log("ambos numeros son iguales");
    alert("ambos numeros son iguales");
}