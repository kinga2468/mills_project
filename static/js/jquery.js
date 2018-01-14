var p0 = document.getElementById('p0');
var p1 = document.getElementById('p1');
var p2 = document.getElementById('p2');
var p3 = document.getElementById('p3');
var p4 = document.getElementById('p4');
var p5 = document.getElementById('p5');
var p6 = document.getElementById('p6');
var p7 = document.getElementById('p7');
var p8 = document.getElementById('p8');

p0.addEventListener("click", function () { add_pawn(0) } );
p1.addEventListener("click", function () { add_pawn(1) } );
p2.addEventListener("click", function () { add_pawn(2) } );
p3.addEventListener("click", function () { add_pawn(3) } );
p4.addEventListener("click", function () { add_pawn(4) } );
p5.addEventListener("click", function () { add_pawn(5) } );
p6.addEventListener("click", function () { add_pawn(6) } );
p7.addEventListener("click", function () { add_pawn(7) } );
p8.addEventListener("click", function () { add_pawn(8) } );

/*$(p0).on('click', function () { add_pawn(0) } );*/

function add_pawn(nr) {
    alert(nr);
}