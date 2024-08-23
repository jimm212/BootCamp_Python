var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]


document.getElementById("button").onclick = function(){
    const lista = document.getElementById('cuerpo-tareas');
    lista.appendChild(tareas);
};





