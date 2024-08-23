// Selectores Basicos
// APRENDER FUNCIONES FLECHA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
//

const contentDiv = document.getElementById('content');
console.log(contentDiv);

const paragraphs = document.getElementsByTagName('p');
console.log(paragraphs);

const textElement = document.getElementsByClassName('text');
console.log(textElement);

// primer elemento que coincida con la clase
const firstParagraph = document.querySelector('.text'); // . solo en etiquetas
console.log(firstParagraph);

const allElements = document.querySelectorAll('.text');
console.log(allElements);

// Manipulando el DOM

// Sustituir el texto del div
// contentDiv.innerHTML = '<h2> Nuevo contenido del div </h2>';

// Sustituir el texto del primer parrafo
// firstParagraph.innerText = 'Este texto ha sido modificado en JS';

// document.getElementById('changeTextButton').onclick = function(){
//     firstParagraph.innerText = 'Texto cambiado con onclick';
// };

firstParagraph.onmouseover= function(){
    firstParagraph.classList.add('highlight');
};

firstParagraph.onmouseout= function(){
    firstParagraph.classList.remove('highlight');
};


const lista = document.getElementById("miLista");
const nuevoElemento= document.createElement('li');
nuevoElemento.textContent= 'Elemento 3';
lista.appendChild(nuevoElementoElemento);
