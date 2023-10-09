const btnSubmit = document.querySelector(".positive-button");
const btnClear = document.querySelector(".negative-button");
const inputTxtArea = document.querySelector(".input-textarea");
//const formatCombo = document.querySelector(".format-combo");
const btnDraw = document.getElementById("draw-btn");
const enterInstructionsPar = document.getElementById("input-instructions");
const referencesDialog = document.getElementById("refs-dialog");
const referencesListItem = document.getElementById("refs-li");
const patternsDialog = document.getElementById("pats-dialog");
const patternsListItem = document.getElementById("pats-li");
const dialogRefsCloseBtn = document.getElementById("close-refs-dialog-btn");
const dialogPatsCloseBtn = document.getElementById("close-pats-dialog-btn");
//const oracleBehTxtArea = document.getElementById("oracle_behaviour");
//const rotateBehTxtArea = document.getElementById("rotate_behaviour");
var nextSlidesBtn = null;
var prevSlidesBtn = null;

let HOME_URL = "http://127.0.0.1:8008/"; // Change URL when deploying
let INPUT_CIRCUIT_STR = "";
let INPUT_FORMAT = "json"; // Posible values: {'json', 'xml'}
let IS_DIALOG_OPEN = false;
let SLIDE_INDEX = 1;

//////// AUXILIAR METHODS ////////
function contarPatron(cadena, patron) {
    const expresion = new RegExp(patron, 'g');
    const coincidencias = cadena.match(expresion);
    return coincidencias ? coincidencias.length : 0;
}

//////// INITIALIZATION ////////
//formatCombo.value = "json";
btnSubmit.disabled = true;
btnSubmit.style.backgroundColor = "grey";

//////// EVENT HANDLING ////////
/* Check empty textbox */
inputTxtArea.addEventListener("keyup", e => {
    if (inputTxtArea.value == "") {
        btnSubmit.disabled = true;
        btnSubmit.style.backgroundColor = "grey";
    } else {
        btnSubmit.disabled = false;
        btnSubmit.style.backgroundColor = null;
    }
});

/* Submit the Circuit */
btnSubmit.addEventListener("click", e => {
    INPUT_CIRCUIT_STR = inputTxtArea.value;

    // let rotateBehs = [];
    // let nRotates = 0;
    // for (const _ of INPUT_CIRCUIT_STR.matchAll(/"R[XYZ1]"/g)) {
    //     nRotates += 1;
    // }
    // if (nRotates > 0) {
    //     for (let i = 0; i < nRotates; i++) {
    //         let rotateBeh = prompt(`Please enter the Rotation #${i} angle:`, "3.14");
    //         rotateBehs.push(rotateBeh);
    //     }

    //     rotateBehTxtArea.value = rotateBehs.toString();
    // }
});

/* Clear the Input TextArea */
btnClear.addEventListener("click", e => {
    inputTxtArea.value = "";
    INPUT_CIRCUIT_STR = "";
});

/* Show the References Dialog box */
referencesListItem.addEventListener("click", e => {
    referencesDialog.showModal();
    IS_DIALOG_OPEN = true;
    e.stopPropagation();
});

patternsListItem.addEventListener("click", e => {
    patternsDialog.showModal();
    IS_DIALOG_OPEN = true;
    e.stopPropagation();
})  

/* Close the modal dialog for References*/
dialogRefsCloseBtn.addEventListener("click", e => {
    window.location.href = HOME_URL;
});

/* Close the modal dialog for Pattern List*/
dialogPatsCloseBtn.addEventListener("click", e => {
    window.location.href = HOME_URL;
});

function cerrarModal() {
    var modal = document.getElementById("modal-div");
    modal.style.display = "none";
}

/* Submit the circuit instead of new line */
inputTxtArea.addEventListener("keydown", e => {
    if (e.keyCode === 13) {
        e.preventDefault();
        btnSubmit.click();
    }
});
/*
// Change input format
formatCombo.addEventListener("change", e => {
    INPUT_FORMAT = formatCombo.value;
    enterInstructionsPar.textContent = `Paste here your Quantum Circuit in the correct ${INPUT_FORMAT.toUpperCase()} format according to QPainter.`;
});
*/

//////// AUXILIAR METHODS ////////
// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("my-slides");
//   if (n > slides.length) {SLIDE_INDEX = 1}
//   if (n < 1) {SLIDE_INDEX = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   slides[SLIDE_INDEX-1].style.display = "block";
// }