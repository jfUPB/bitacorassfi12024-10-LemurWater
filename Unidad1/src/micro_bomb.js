let port;
let connectBtn;
// --------------------------------------------------------------------
let state = 1;

let canvasWidth = 800;
let canvasHeight = 400;
let canvasColor = 40;
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function setup() {
  setWindow();
  intro();

  port = createSerial();
  connectBtn = createButton("Connect to micro:bit");
  connectBtn.position(300, 345);
  connectBtn.mousePressed(connectBtnClick);
}
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function draw() {
  checkPortState();

  switch (state) {
    case 0:
      break;
    case 1:
      bomb();
      break;
    case 2:
      score();
      break;
  }
}
// --------------------------------------------------------------------

// --------------------------------------------------------------------
function setWindow() {
  createCanvas(canvasWidth, canvasHeight);
  background(canvasColor);
}

function intro() {
  textSize(300);
  text("🧨", 250, 270);
  ellipse(canvasWidth / 2, 190, 250, 80);
  textSize(42);
  text("micro:bomb", canvasWidth / 2 - 100, canvasHeight / 2 - 0);
}

function bomb() {
  // Background
  background(canvasColor);
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
  fill(color(85, 85, 43));
  textSize(60);
  text("X X X", 325, 225);
  fill(color(102, 255, 204));
}
function score() {}

function connectBtnClick() {
  if (!port.opened()) {
    port.open("MicroPython", 115200);
  } else {
    port.close();
  }
}
function checkPortState() {
  if (!port.opened()) {
    connectBtn.position(300, 345);
    connectBtn.html("Connect to micro:bit");
  } else {
    state = 1;
    connectBtn.position(320, 345);
    connectBtn.html("Disconnect");
  }
}

// --------------------------------------------------------------------
