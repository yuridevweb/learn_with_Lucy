const isCorrect = document.getElementById("isCorrect")
const isIncorrect = document.getElementById("isIncorrect")
const addition = document.getElementById("addition")
const counter = document.getElementById("counter")
const score = document.getElementById("score")
const correctAnswer = document.getElementById("correctAnswer")
const correctBonus = 10;
const maxQuestions = 3;
let freezeClic = false; // just modify that variable to disable all clics events
let Game, arr;

document.addEventListener("click", e => {
    if (freezeClic) {
        e.stopPropagation();
        e.preventDefault();
    }
}, true);

//gets a random number
function ranNum() {
  return num = Math.floor(Math.random() * 12) + 1
}


//class to store required data from a session
function GameSettings() {
  this.num1 = ranNum()
  this.num2 = ranNum()
  this.total = this.num1 + this.num2
  this.choices = createChoices(this.total)
  this.counter = 0
  this.score = 0
}

//displays HTML data
GameSettings.prototype.displayHTML = function () {
  addition.innerHTML = this.num1 + ' + ' + this.num2 + ' = ';
  counter.innerHTML = this.counter;
  score.innerHTML = this.score;
}

//on screen input
/* function addNumber(element){
  document.getElementById('input').value = document.getElementById('input').value+element.value;
} */

//clears field after clicking submit
/* function cleanInput(){
  document.getElementById('input').value = "";
} */


function hideResult() {
  isCorrect.style.visibility = "hidden"
  isIncorrect.style.visibility = "hidden"
  correctAnswer.style.visibility = "hidden"
}

function createChoices(total) {
  var nums = new Set();
  nums.add(total)
  while(nums.size !== 4) {
    nums.add(Math.floor(Math.random() * 20) + 1);
  }
  return Array.from(nums)
}

function shuffle(array) {
  array.sort(() => Math.random() - 0.5);
}

//creating a class to run a game
Game = new GameSettings();
Game.displayHTML();

//checking user's answer and taking action based on it
GameSettings.prototype.checkAnswer = function (answer) {
  this.counter += 1
  freezeClic = true
  if (this.total == answer) {
    this.score += correctBonus
    isCorrect.style.visibility = "visible"
    isCorrect.innerHTML =answer + "&#10004";
  } else {
    isIncorrect.style.visibility = "visible"
    isIncorrect.innerHTML = answer + "&#x2717";
    correctAnswer.style.visibility = "visible"
    correctAnswer.innerHTML =
      this.num1 + ' + ' + this.num2 + ' = ' + this.total;
  }

  if ((Game.counter == maxQuestions) || (Game.counter > maxQuestions)) {
    console.log("dsddasd")
    sent_ajax();
    console.log("dsddasd")
        return window.location.assign('highscores/');             
  }
    setTimeout(
      function () {
        Game.updateNums()
        Game.displayHTML()
        hideResult()
        makeChoice()
        freezeClic = false
      }, 1100);
}


//update numbers for a next round
GameSettings.prototype.updateNums = function () {
  this.num1 = ranNum()
  this.num2 = ranNum()
  this.total = this.num1 + this.num2
  this.choices = createChoices(this.total)
}


makeChoice = function () {
  arr = Game.choices;
  document.getElementById('choices').innerHTML = ""
  shuffle(arr);
  var i,buttonContainer, newButton;
  buttonContainer = document.getElementById('choices');
  for (i = 0; i < arr.length; i++) {
    newButton = document.createElement('input');
    newButton.className = 'dot'
    newButton.type = 'button';
    newButton.value = arr[i];
    newButton.onclick = function () {
      Game.checkAnswer(this.value)
    };
    buttonContainer.appendChild(newButton);    
  }
};

makeChoice()


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


//funtion to send and save elapsed data before refreshing the page
function sent_ajax() {
    // make POST ajax call
    $.ajax({
        type: 'POST',
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val(),
        },
        url: "/maths/addition/get_simple_add_score/",
        data: {"elapsedTime": elapsedTime,"score": Game.score,},
    })
}

