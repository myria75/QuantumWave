nextSlidesBtn = document.getElementById("next-btn");
prevSlidesBtn = document.getElementById("prev-btn");

//////// INITIALIZATION ////////
let SLIDE_INDEX = 1;
showSlides(SLIDE_INDEX);

//////// EVENT HANDLING ////////
/* Move to next pattern IFrame in results' slideshow */
nextSlidesBtn.addEventListener("click", e => {
    showSlides(SLIDE_INDEX += 1);
});

/* Move to previous pattern IFrame in results' slideshow */
prevSlidesBtn.addEventListener("click", e => {
    showSlides(SLIDE_INDEX -= 1);
});

//////// AUXILIAR METHODS ////////
function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("my-slides");
  if (n > slides.length) {SLIDE_INDEX = 1}
  if (n < 1) {SLIDE_INDEX = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[SLIDE_INDEX-1].style.display = "block";
}