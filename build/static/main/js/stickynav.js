window.onload = function() {dynStick()};
window.onload = function() {stick()};
// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
    navbar.classList.remove("no-sticky");
  } else {
   navbar.classList.add("no-sticky");
    navbar.classList.remove("sticky");
  }
}

function dynStick(){
  var home = document.getElementById("home-div");
  if (typeof home !== 'undefined' && home !== null){
    window.onscroll = function() {myFunction()};
  }
}

function stick(){
  var notHome = document.getElementById("not-home-div");
  if (typeof notHome !== 'undefined' && notHome !== null){
    navbar.classList.add("sticky")
  }
}
