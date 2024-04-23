// render.js
// --------------------------------------------------------------------
let canvasWidth = 800;
let canvasHeight = 400;
let canvasColor = 40;
// --------------------------------------------------------------------

// --------------------------------------------------------------------
let display1 = "?";
let display2 = "=";
let display3 = "A";
let display4 = "X";
let display5 = "Y";
let display6 = "Z";
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function intro() {
  textSize(300);
  text("🧨", 250, 270);
  ellipse(canvasWidth / 2, 190, 250, 80);
  textSize(42);
  text("micro:bomb", canvasWidth / 2 - 100, canvasHeight / 2 - 0);
}

function bomb() {
  // Background
  background(40);
  textSize(300);
  text("🧨", 250, 270);
  strokeWeight(15);
  rect(230, 160, 350, 80);

  // Pixels
  strokeWeight(0);
  fill(color(179, 255, 240));
  rect(245, 173, 45, 55);
  rect(300, 173, 45, 55);
  rect(355, 173, 45, 55);
  rect(410, 173, 45, 55);
  rect(465, 173, 45, 55);
  rect(520, 173, 45, 55);

  // Text
  fill(color(0, 102, 82));
  textSize(55);
  text("1", 249, 222);
  text("0", 306, 222);
  text("1", 359, 222);
  text("0", 414, 222);
  text("1", 470, 222);
  text("0", 525, 222);
  fill(color(102, 255, 204));
}

function score() {}
// --------------------------------------------------------------------
function setWindow() {
  createCanvas(canvasWidth, canvasHeight);
  background(canvasColor);
}
// --------------------------------------------------------------------
