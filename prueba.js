var x=2;
var a=2;
var b=2;
var me = this;


function pararInterval(){
	clearInterval(h);
}
function sumar(a,b){
	console.log(me.a+me.b);
}
function restar(a,b){
    console.log(a-b);
}

var h=setInterval(
	function(){
		//console.log(x++);                
	}, 500);

setTimeout(pararInterval, 3000);

restar(6,5);
sumar(1,2);
sumar(a,b);





