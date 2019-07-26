var express = require('express');
var bodyParser = require('body-parser');
var app = express();

// Render assumes ejs, static files in public/
app.set('view engine', 'ejs');
app.use(express.static('public'));
// Uses body-parser 
app.use(bodyParser.urlencoded({extended: true}));

var friends = ['biden', 'pete', 'trump', 'warren'];

app.get('/', function(req, res){
	res.render('index', {friends: friends});
});

app.post('/add', function(req, res){
	friends.push(req.body.name);
	res.redirect('/');
});

app.listen(3000, function(){
	console.log('Listening on PORT 3000');
});
