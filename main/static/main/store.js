//Wait until scores are updated
$(window).on('load', function () {
  $("#cover").hide();
  aboutUsTabs[0].style["background-color"] = seletectedColor;
});

const avatars = document.getElementById("box-text").innerHTML
const pets = document.getElementById("box-text-2").innerHTML
const dwellings = document.getElementById("box-text-3").innerHTML

var aboutUs = {
  "Avatars": avatars,
  "Pets": pets,
  "Dwellings": dwellings,
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

