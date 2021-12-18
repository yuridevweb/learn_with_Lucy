const isCorrect = document.getElementById("isCorrect")
const isIncorrect = document.getElementById("isIncorrect")
const addition = document.getElementById("addition")
const counter = document.getElementById("counter")
const score = document.getElementById("score")
const correctAnswer = document.getElementById("correctAnswer")
const correctBonus = 10;
const maxQuestions = 3;

//on screen input
function addNumber(element){
  document.getElementById('input').value = document.getElementById('input').value+element.value;
}

//clears field after clicking submit
function cleanInput(){
  document.getElementById('input').value = "";
}

//gets a random number
function ranNum() {
  return num = Math.floor(Math.random() * 12) + 1
}

//class to store required data from a session
function Addition() {
  this.num1 = ranNum()
  this.num2 = ranNum()
  this.total = this.num1 + this.num2
  this.counter = 0
  this.score = 0
}

//checking user's answer and taking action based on it
Addition.prototype.checkAnswer = function () {
  this.counter += 1
  answer = document.getElementById('input').value
  if (this.total == answer) {
    this.score += correctBonus
    isCorrect.style.display = "block"
    isCorrect.innerHTML =answer + "&#10004";
  } else {
    isIncorrect.style.display = "block"
    isIncorrect.innerHTML = answer + "&#x2717";
    correctAnswer.style.display = "block"
    correctAnswer.innerHTML =
      this.num1 + ' + ' + this.num2 + ' = ' + this.total;
  }
}

//displays HTML data
Addition.prototype.displayHTML = function () {
  addition.innerHTML = this.num1 + ' + ' + this.num2 + ' = ';
  counter.innerHTML = this.counter;
  score.innerHTML = this.score;
}

//update numbers for a next round
Addition.prototype.updateNums = function () {
  this.num1 = Math.floor(Math.random() * 12) + 1
  this.num2 = Math.floor(Math.random() * 12) + 1
  this.total = this.num1 + this.num2
}


//creating a class to run a game
var game = new Addition();
game.displayHTML();


function hideResult() {
  isCorrect.style.display = "none"
  isIncorrect.style.display = "none"
  correctAnswer.style.display = "none"
}

//game logic
document.getElementById('submit').onclick = (e) => {
  if(document.getElementById("input").value.length == 0)
  {
      alert("Please enter your answer!")
  } else {
    e.preventDefault()
    game.checkAnswer()
    cleanInput()
      if ((game.counter == maxQuestions) || (game.counter > maxQuestions)) {
        sent_ajax();
        return window.location.assign('highscores/');             
    }    
    setTimeout(function () {
      game.updateNums()
      game.displayHTML()
      hideResult()
    },1100);
  }
}

let formattedTime, 
  startTime,
  currentTime,
  elapsedTime,
  clockInterval,
  hours,
  minutes,
  seconds,
  remainder;

// adding leading zero to a timer
function add_leading_zero(number){
    if(number < 10) {
        return "0" + number.toString();
    } else {
        return number.toString();
    }
}

//game timer
window.onload = () => {
  startTime = new Date().getTime();
  clockInterval = setInterval(function () {
    currentTime = new Date().getTime();
    elapsedTime = currentTime - startTime;

    hours = Math.floor(elapsedTime / 3600000);
    remainder = elapsedTime - (hours * 3600000);

    minutes = Math.floor(remainder / 60000);
    remainder -= (minutes * 60000);

    seconds = Math.floor(remainder / 1000);

    formattedTime = add_leading_zero(hours) + ":" + add_leading_zero(minutes) + ":" + add_leading_zero(seconds);
    document.getElementById("timer").innerHTML = formattedTime;

  },100);
}
console.log(elapsedTime)

//funtion to send and save elapsed data before refreshing the page
function sent_ajax() {
    // make POST ajax call
    $.ajax({
        type: 'POST',
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val(),
        },
        url: "/maths/addition/get_addition_score/",
        data: {"elapsedTime": elapsedTime,"score": game.score,},
    })
}

