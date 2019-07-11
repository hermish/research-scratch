var game = {
	// Constants
	MODES: {"Easy": 3, "Hard": 6},

	// Elements
	squares: document.getElementsByClassName("square"),
	colorDisplay: document.getElementById("colorDisplay"),
	message: document.getElementById("message"),
	h1: document.querySelector("h1"),
	reset: document.getElementById("reset"),
	modeButtons: document.querySelectorAll(".mode"),

	// Variables
	numSquares: 6,

	// Functions
	initialize: function() {
		game.setUpModes();
		game.setUpColors();
		game.reset.addEventListener("click", function(){
			game.resetGame();
		});
		game.resetGame();
	},

	setUpModes: function() {
		for (var pos = 0; pos < game.modeButtons.length; pos++) {
			game.modeButtons[pos].addEventListener("click", function(){
				game.modeButtons[0].classList.remove("selected");
				game.modeButtons[1].classList.remove("selected");
				this.classList.add("selected");

				game.numSquares = game.MODES[this.textContent];
				game.resetGame();
			});
		}
	},

	setUpColors: function() {
		for (var pos = 0; pos < game.squares.length; pos++) {
			game.squares[pos].addEventListener("click", function(){
				var clicked = this.style.backgroundColor;
				if (clicked === game.goalColor) {
					game.message.textContent = "Correct!";
					game.h1.style.backgroundColor = clicked;
					game.reset.textContent = "Play Again?";
					game.changeColors(clicked);
				} else {
					this.style.backgroundColor = "white";
					game.message.textContent = "Try Again?";
				}
			})
		}
	},

	resetGame: function() {
		game.colors = game.generateRandomColors(game.numSquares);
		game.goalColor = game.randomEntry(game.colors);
		game.colorDisplay.textContent = game.goalColor;

		for (var pos = 0; pos < game.squares.length; pos++) {
			if (game.colors[pos]) {
				game.squares[pos].style.display = "block";
				game.squares[pos].style.backgroundColor = game.colors[pos];
			} else {
				game.squares[pos].style.display = "none";
			}
		}

		game.message.textContent = "";
		game.reset.textContent = "New Colors";
		game.h1.style.backgroundColor = null;
	},

	changeColors: function changeColors(target) {
		for (var pos = 0; pos < game.squares.length; pos++) {
			game.squares[pos].style.backgroundColor = target;
		}
	},

	randomEntry: function(array) {
		var index = Math.floor(Math.random() * array.length);
		return array[index];
	},

	generateRandomColors: function(number) {
		var colors = [];
		for (pos = 0; pos < number; pos++) {
			colors.push(game.randomColor());
		}
		return colors;
	},

	randomColor: function() {
		red = Math.floor(Math.random() * 256);
		blue = Math.floor(Math.random() * 256);
		green = Math.floor(Math.random() * 256);
		return "rgb(" + red + ", " + blue + ", " + green + ")";
	}
};

game.initialize();
