// --------------------------------------------------
let canvasWidth = 510;
let canvasHeight = 510;

let cSize = 40
let cColor = [127, 127, 127]
const cObj = {x:0, y:0};
let cPosition = [0, 0];

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
  cursorRender();
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
  cPosition[0] = mouseX - canvasWidth / 2;
  cPosition[1] = mouseY - canvasHeight / 2;
}
function cursorColor() {
  if (cPosition[0] > 0) {
    cColor[0] = cPosition[0];
  } else {
    
  }
  if (cPosition[1] > 0) {
    cColor[1] = cPosition[1];
  } else {
    
  }
  cColor[0] = cPosition[0];
  print(cPosition[0]);
  stroke(cColor);
}
function cursorRender() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(cPosition[0], cPosition[1], cSize, cSize, 14);
}
// --------------------------------------------------
