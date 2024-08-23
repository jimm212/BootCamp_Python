var select;

do{
    select = parseInt(prompt("Seleccione visitar ... \n1 Peliculas \n2 Series \n3 libros \n4 Videojuegos \n5 Salir"));

    switch (select){
        case 1:
            eleccion = parseInt(prompt('Selecciona una pelicula \n1 Origen \n2 Avatar \n3 Joker \n4 El caballero oscuro \n5 Volver'));

            if (eleccion == 1){
                alert("ha seleccionado el Origen \n que la disfrute" );

            }else if ( eleccion == 2){
                alert("ha seleccionado Avatar \n que la disfrute" );

            }else if ( eleccion == 3){
                alert("ha seleccionado el Joker \n que la disfrute" );

            }else if ( eleccion == 4){
                alert("ha seleccionado El caballero oscuro \n que la disfrute" );

            }

            break;
        case 2:
            eleccion = parseInt(prompt('Selecciona una Serie \n1 Breaking Bad \n2 Game of Thrones \n3 The Sopranos \n4 Peaky Blinders \n5 Volver'));

            if (eleccion == 1){
                alert("ha seleccionado el Breaking Bad \n que disfrutes la serie" );

            }else if ( eleccion == 2){
                alert("ha seleccionado Game of Thrones \n que disfrutes la serie" );

            }else if ( eleccion == 3){
                alert("ha seleccionado el The Sopranos \n que disfrutes la serie" );

            }else if ( eleccion == 4){
                alert("ha seleccionado Peaky Blinders \n que disfrutes la serie" );

            }
            break;
        case 3:
            eleccion = parseInt(prompt('Selecciona un Libro \n1 Habitos Atomicos \n2 Las Cronicas de Narnia \n3 Harry potter \n4 El señor de los anillos \n5 Volver'));

            if (eleccion == 1){
                alert("ha seleccionado el Habitos Atomicos \n que disfrutes tu lectura" );

            }else if ( eleccion == 2){
                alert("ha seleccionado Las Cronicas de Narnia \n que disfrutes tu lectura" );

            }else if ( eleccion == 3){
                alert("ha seleccionado Harry potter \n que disfrutes tu lectura" );

            }else if ( eleccion == 4){
                alert("ha seleccionado El señor de los anillos \n que disfrutes tu lectura" );

            }
            break;
        case 4:
            eleccion = parseInt(prompt('Selecciona un Juego \n1 The elder scroll Skyrim \n2 The Witcher 3 \n3 Manor Lord \n4 Kingdom come Deliverance \n5 Volver'));

            if (eleccion == 1){
                alert("ha seleccionado The elder scroll Skyrim \n que disfrute su juego" );

            }else if ( eleccion == 2){
                alert("ha seleccionado The Witcher 3 \n que disfrute su juego" );

            }else if ( eleccion == 3){
                alert("ha seleccionado Manor Lord \n que disfrute su juego" );

            }else if ( eleccion == 4){
                alert("ha seleccionado Kingdom come Deliverance \n que disfrute su juego" );

            }
            break;

    }
}while(select != 5 );
