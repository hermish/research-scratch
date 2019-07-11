var p1Score = 0;
var p2Score = 0;
var winningScore = 5;
var gameOver = false;

function reset() {
	p1Score = 0;
	p2Score = 0;
	gameOver = false;

	p1Display.textContent = p1Score;
	p2Display.textContent = p2Score;
	p1Display.classList.remove("winner");
	p2Display.classList.remove("winner");
}

var p1Button = document.getElementById("p1");
var p2Button = document.getElementById("p2");
var p1Display = document.getElementById("p1Display");
var p2Display = document.getElementById("p2Display");

p1Button.addEventListener("click", function(){
	if (!gameOver) {
		p1Score++;
		p1Display.textContent = p1Score;
		if (p1Score === winningScore) {
			p1Display.classList.add("winner");
			gameOver = true;
		}
	}
});

p2Button.addEventListener("click", function(){
	if (!gameOver) {
		p2Score++;
		p2Display.textContent = p2Score;
		if (p2Score === winningScore) {
			p2Display.classList.add("winner");
			gameOver = true;
		}
	}
});

var resetButton = document.getElementById("reset");

resetButton.addEventListener("click", function(){
	reset();
});

var winningInput = document.querySelector("input");
var winningScoreDisplay = document.querySelector("p span");

winningInput.addEventListener("change", function(){
	winningScoreDisplay.textContent = this.value;
	winningScore = Number(this.value);
	reset();
});