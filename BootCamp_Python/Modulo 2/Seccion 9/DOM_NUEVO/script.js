//Selectores básicos

const contentDiv=document.getElementById('content');
console.log(contentDiv);

/*const contentDiv=document.querySelectorAll('div');
console.log(contentDiv);

for(let i=0;i<contentDiv.length;i++){
    contentDiv[i].innerHTML='<h2>Nuevo contenido del div</h2>';
}*/

const paragraphs=document.getElementsByTagName('p');
console.log(paragraphs);

const elementos=document.getElementsByClassName('text');
console.log(elementos);

const firstParagraph=document.querySelector('.text');
console.log(firstParagraph);

const allElements=document.querySelectorAll('.text');
console.log(allElements);

//Manipulando el DOM
//contentDiv.innerHTML='<h2>Nuevo contenido del div</h2>';

//irstParagraph.innerText='Este texto ha sido modificado en JS';

document.getElementById('changeTextButton').onclick=function(){
    firstParagraph.innerText='TEXTO CAMBIADO CON ON CLICK';
};

firstParagraph.onmouseover=function(){
    firstParagraph.classList.add('highlight');
};

firstParagraph.onmouseout=function(){
    firstParagraph.classList.remove('highlight');
};


const lista=document.getElementById('miLista');
const nuevoElemento=document.createElement('li');
nuevoElemento.textContent='Elemento 3';
lista.appendChild(nuevoElemento);

