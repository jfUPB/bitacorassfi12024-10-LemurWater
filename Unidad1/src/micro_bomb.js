let state = 0;

let canvasWidth = 800;
let canvasHeight = 400;
let canvasColor = 40;
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function setup() {
  setWindow();
  intro();
}
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function draw() {}
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function setWindow() {
  createCanvas(canvasWidth, canvasHeight);
  background(canvasColor);
}

function intro() {
  textSize(300);
  text("🧨", 250, 270);
  ellipse(canvasWidth/2, 190, 250, 80);
  textSize(42);
  text("micro:bomb", (canvasWidth/2) - 100, (canvasHeight/2) - 0);
}
// --------------------------------------------------------------------
