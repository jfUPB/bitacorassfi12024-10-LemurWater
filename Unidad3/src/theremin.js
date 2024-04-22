let canvasX = 600;
let canvasY = 400;

function setup() {
   create_canvas();
   axis();
}

function draw() {
  l_horizontal.fill(0);
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}

function create_canvas() {
    createCanvas(canvasX, canvasY);
    background(200);
}
function axis() {
    stroke('magenta');
    strokeWeight(5);
    l_horizontal = line(0, canvasY/2, canvasX, canvasY/2);
   stroke('cyan')
}
