var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]

var button1  = document.querySelector(".btn");
var form     = document.getElementById('formulario');
var selector = document.querySelectorAll('.btn');
var button2  = selector[selector.length-1];
var lista    = document.getElementById('tabla-tareas');
var input    = document.getElementById('nuevaTarea');

button1.onclick = function(){
    if(form.style.display === 'none'){
        form.style.display = 'block';
    }else{
        form.style.display = 'none';
    }
};

function agregartarea(){
    const newtarea = input.value.trim();
    if(newtarea){
        tareas.push({tarea: newtarea});
        input.value = '';
        acttable();
    }
}

function eliminar(index){
    tareas.splice(index,1);
    acttable();
}

function acttable(){
    const cuerpotabla = document.getElementById('cuerpo-tabla');
    cuerpotabla.innerHTML = '';
    tareas.forEach((tarea, index)=>{
        const fila = document.createElement('tr');
        fila.innerHTML = `
                <td>${tarea.tarea}</td>
                <td><button onclick = "eliminar(${index})" style = "background-color: crimson; border: none; 
                border-radius:8px; color:white">Finalizar</button></td>
            `;
            cuerpotabla.appendChild(fila);
    });
}

button2.onclick = function(){
    agregartarea();
    form.style.display = 'none';
}

acttable();

