// Primera Parte
$('#text2').toggle();
$('#text1').mouseenter(function(){
    $('#text2').toggle();
});
$('#text1').mouseout(function(){
    $('#text2').toggle();
});

// Agrandar Imagen
$('#img').click(function(){
    $('#img').css('width','100%');
})

$('#img').mouseout(function(){
    $('#img').css('width','20%');
})

// ondblclick="letragrande()"
$('#caja3').dblclick(function(){
    $('#caja3').css('fontSize','150%');
})
