// Javascript Owner: Korey Hayes
// Source: https://www.w3schools.com/howto/howto_js_dropdown.asp
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function clickDrop() {                                  // initialize function
    var drop = document.getElementById("navLinks");       // set variable "drop" to the id "navLinks"
    if (drop.style.display === "block") {                 // selection statement for the action on click
      drop.style.display = (window.onclick = "none");     // if the navLinks are displayed, hide them
      drop.style.display = "none";                        // otherwise, show them (on click)
    } else {
      drop.style.display = "block";
    }
  }
  // End Owner: Korey Hayes
  
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}