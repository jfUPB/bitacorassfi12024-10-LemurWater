// --------------------------------------------------
let canvasWidth = 600;
let canvasHeight = 400;

let cursorSize = 40
const cursorObj = {x:0, y:0};
let webglX = 0;
let webglY = 0;
// --------------------------------------------------
function setup() {
  generateCanvas()
  axis();
}
// --------------------------------------------------

// --------------------------------------------------
function draw() {
  cursorPosition();
  cursorColor();
  renderCursor();
}
// --------------------------------------------------

// --------------------------------------------------
function generateCanvas() {
  //createCanvas(canvasX, canvasY);
  createCanvas(canvasWidth, canvasHeight, WEBGL);
  background(200);
}
function axis() {
  stroke('black');
  strokeWeight(5);
  //line(0, canvasY/2, canvasX, canvasY/2);
  //line(canvasX/2, 0, canvasX/2, canvasY);
  line(-canvasWidth/2, 0, 0, canvasWidth/2, 0, 0);
  line(0, -canvasWidth/2, 0, 0, canvasWidth/2, 0);
  stroke('cyan')
}

function cursorPosition(){
  //ellipse(mouseX, mouseY, 80, 80, 3);
  webglX = mouseX - canvasWidth / 2;
  webglY = mouseY - canvasHeight / 2;
}
function cursorColor() {
  if (webglX  > 0) {
    stroke('red');
  } else {
    stroke('pink');
  }
}
function renderCursor() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(webglX, webglY, cursorSize, cursorSize, 14);
}
// --------------------------------------------------
