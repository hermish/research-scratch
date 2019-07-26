var express = require('express');
var app = express();

var NOISES = {
	'pig': 'Oink',
	'cow': 'Moo',
	'dog': 'Woof Woof'
};

app.get('/', function(req, res) {
	res.send('Hi there!');
})

app.get('/speak/:animal', function(req, res) {
	var animal = req.params.animal.toLowerCase();
	res.send('The ' + animal + ' says "' + NOISES[animal] + '"!');
})

app.get('/repeat/:word/:number', function(req, res) {
	var repeats = Number(req.params.number);
	var word = req.params.word;
	res.send((word + ' ').repeat(repeats));
})

app.get('*', function(req, res) {
	res.send('Wrong Page');
})

PORT = 3000
app.listen(PORT, function() {
	console.log('Listening on: ' + PORT);
});
