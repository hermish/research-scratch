/* Falsy Values */
var bad = false;
bad = 0;
bad = "";
bad = null;
bad = undefined;
bad = NaN;

/* Undefined Arguments */
function example(arg1, arg2) {
	console.log(arg2);
}
example(0);
// undefined

/* Array Manipulation */
var one = [];
var two = new Array();

var numbers = [1, 2, 3];
numbers[4] = 5;
numbers;
// [1, 2, 3, empty, 5]

for(var pos = 0; pos < numbers.length; pos++) {
	console.log(numbers[pos]);
}

numbers.forEach(function(number) {
	console.log(number);
})