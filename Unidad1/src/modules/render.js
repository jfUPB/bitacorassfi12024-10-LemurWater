const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 400;
const CANVAS_COLOR = 40;

let explosion_size;
let explosion_counter;

let EXPLOSION_SIZE_ = 25;
let EXPLOSION_COUNTER_ = 0;
let EXPLOSION_RATE = 1.025;
let EXPLOSION_MAX = 220;

let wireRed = true;
let wireGreen = true;
let wireYellow = true;
let WIRE_THICKNESS = 10;
let CABLE_CONNECT = 25;
// --------------------------------------------------------------------

// --------------------------------------------------------------------
let display1;
let display2;
let display3;
let display4;
let display5;
let display6;
// --------------------------------------------------------------------
function setWindow() {
  createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
  background(CANVAS_COLOR);
}
// --------------------------------------------------------------------
function intro() {
  textSize(300);
  text("🧨", 250, 270);
  ellipse(CANVAS_WIDTH / 2, 190, 250, 80);
  textSize(42);
  text("micro:bomb", CANVAS_WIDTH / 2 - 100, CANVAS_HEIGHT / 2 - 0);
}

function bomb() {
  renderWires();

  strokeWeight(1);
  stroke(1);
  // Background
  background(40);
  fill(color(80));
  triangle(0, CANVAS_HEIGHT, CANVAS_WIDTH, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

  // Graphics
  fill(color(102, 255, 204));
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
  display1 = text("T", 249, 222);
  display2 = text("=", 306, 222);
  display3 = text("0", 359, 222);
  display4 = text("5", 414, 222);
  display5 = text("-", 470, 222);
  display6 = text("s", 525, 222);

  renderWires();
}
// --------------------------------------------------------------------
function setTimer() {
  // Pixels
  strokeWeight(0);
  fill(color(179, 255, 240));
  rect(355, 173, 45, 55);
  rect(410, 173, 45, 55);

  // Text
  fill(color(0, 102, 82));
  if (timer > 9) {
    display3 = text(str(timer).charAt(0), 359, 222);
    display4 = text(str(timer).charAt(1), 414, 222);
  } else {
    display3 = text("0", 359, 222);
    display4 = text(str(timer), 414, 222);
  }
}
// --------------------------------------------------------------------
function renderWires() {
  strokeWeight(WIRE_THICKNESS);

  switch (wireIndex) {
    case 0:
      wireRed = true;
      wireGreen = true;
      wireYellow = true;
      break;
    case 1:
      wireRed = true;
      wireGreen = false;
      wireYellow = true;
      break;
    case 2:
      wireRed = true;
      wireGreen = false;
      wireYellow = false;
      break;
    case 3:
      wireRed = false;
      wireGreen = false;
      wireYellow = false;
      break;
  }

  if (wireRed) {
    noFill();
    stroke("red");
    bezier(265, 260, 265, 350, 285, 350, 450, 325);

    noStroke();
    fill(color("lightgrey"));
    circle(265, 260, CABLE_CONNECT);
  }

  if (wireGreen) {
    noFill();
    stroke("green");
    bezier(300, 260, 320, 400, 320, 350, 450, 325);

    noStroke();
    fill(color("lightgrey"));
    circle(300, 260, CABLE_CONNECT);
  }

  if (wireYellow) {
    noFill();
    stroke("yellow");
    bezier(350, 260, 360, 400, 360, 350, 450, 325);

    noStroke();
    fill(color("lightgrey"));
    circle(350, 260, CABLE_CONNECT);
  }
  noFill();
  stroke("black");
  bezier(560, 260, 660, 400, 500, 350, 450, 325);

  noStroke();
  fill(color("lightgrey"));
  circle(560, 260, CABLE_CONNECT);
}
// --------------------------------------------------------------------
function renderExplosion() {
  if (explosion_counter > EXPLOSION_MAX) {
    state = 1;
    explosion_counter = 0;
    return;
  } else {
    explosion_counter++;

    explosion_size *= EXPLOSION_RATE;
    fill(color("white"));
    circle(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, explosion_size);
  }
}
// --------------------------------------------------------------------
