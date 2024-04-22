let canvasX = 600;
let canvasY = 400;

let cursorSize = 40

// --------------------------------------------------
function setup() {
  generateCanvas()
  axis();
}
// --------------------------------------------------

// --------------------------------------------------
function draw() {
  renderCursor()
}
// --------------------------------------------------

// --------------------------------------------------
function generateCanvas() {
  createCanvas(canvasX, canvasY);
  background(200);
}
function axis() {
  stroke('magenta');
  strokeWeight(5);
  line(0, canvasY/2, canvasX, canvasY/2);
  line(canvasX, canvasY/2, canvasX, canvasY/2);
  stroke('cyan')
}

function renderCursor() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}
// --------------------------------------------------
