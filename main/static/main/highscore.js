//Wait until scores are updated
$(window).on('load', function () {
  $("#cover").hide();
  aboutUsTabs[0].style["background-color"] = seletectedColor;
});

const score1 = document.getElementById("box-text").innerHTML
console.log(score1)
const score2 = document.getElementById("box-text-2").innerHTML

var aboutUs = {
  "Addition": score1,
  "Advanced addition": score2,
  "Values": "<ul><li>Nunc iaculis</li><li>Donec dictum fringilla</li><li>Duis convallis tortor ultrices</li><li>Curabitur in est lectus</li><li>Maecenas condimentum elit</li></ul>"
};

var unseletectedColor = "#ffebcd";
var seletectedColor = "#32FF6F";

var aboutUsTabs = document.getElementsByClassName("single-tab");

for (var a = 0; a < aboutUsTabs.length; a++) {
  aboutUsTabs[a].onclick = function() {
    var clickedValue = this.innerHTML;
    document.getElementById("box-text").innerHTML = aboutUs[clickedValue];

    for (var b = 0; b < aboutUsTabs.length; b++) {
      aboutUsTabs[b].style["background-color"] = unseletectedColor;
      aboutUsTabs[b].style["font-weight"] = "normal";
    }

    this.style["background-color"] = seletectedColor;
    this.style["font-weight"] = "bold";


  }
}

