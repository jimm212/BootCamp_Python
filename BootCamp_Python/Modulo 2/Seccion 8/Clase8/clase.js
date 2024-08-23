// Antes de esto estaban los ciclos ---> 
// no he usado mucho el do{}while{}
/*
try{
    let resultado = 10/0;
    console.log("El resultado es: " + resultado);
}catch{
    console.log("Se ha producido un error: " + error.message);
}finally{
    console.log("Este bloque se ejecuta siempre");
}
*/
function convertirAEntero(n){
    try {
        let numero = parseInt(n);
        console.log(numero);
        
        // VERIFICAR
        if(isNaN(numero)){
            throw new Error("La entrada no es un numero valido");
        }

        console.log(" El numero ingresado es: " + numero);

        

    } catch(error){
        console.log("Error: " + error.message);
    }
}


let n  = prompt('Introduce una cadena de caracteres numerica ');
convertirAEntero(n);


console.log("----------------------------------------------------------------");
// Push= Anadir
// Pop=Eliminar
// arreglo.push/pop(n)

var arreglo =[1,2,3,4,5]; 
console.log(arreglo);

arreglo.push(4554);
console.log(arreglo);

arreglo.unshift(12);
console.log(arreglo);

console.log("----------------------------------------------------------------");

var arreglo2 = ['arbol','banana','casa','cama', 'carro'];
console.log(arreglo2);

arreglo2.pop();
console.log(arreglo2);

arreglo2.shift();
console.log(arreglo2);

arreglo2.unshift('azul');
console.log(arreglo2);



console.log("----------------------------------------------------------------");

var arreglo3 = ['arbol','banana','casa','carro' ,'cama', 'mesa'];
console.log(arreglo3);

// ver posicion especifica de lista
console.log(arreglo3[4]);

var cadena = arreglo3[4];
console.log(cadena);

// Largo de la cadena
let tam = arreglo3.length;
console.log(tam);

// añadir a una lista  --- 0 solo añade, 1+ quita elemetos a la lista
arreglo3.splice(3,0,'manzana');
console.log(arreglo3);

// arreglo4 = [50,,80,25,10,30,70] ---> ordenar de menor a mayor



//                                  POO
console.log("----------------------- POO --------------------------------------");

let persona={
    nombre:"Jorge",
    edad:"30",
    saludo: function(){
        console.log("Holi, mi nombre es "+ this.nombre);
    }

}

console.log(persona);
console.log(persona.edad);
console.log(persona.nombre);
persona.saludo();

console.log("------------------- Funcion Constructora -------------------");

function Persona(nombre, edad){
    this.nombre = nombre;
    this.edad   = edad  ;
    this.saludo = function(){
        console.log("Hola, mi nombre es " + this.nombre);
    };
}

let persona1= new Persona("Juan"  , 30);
console.log(persona1.nombre);
persona1.saludo();

let persona2= new Persona("Javier", 26);
console.log("Mi nombre es " + persona2.nombre + " y tengo " + persona2.edad + " años.");