const CROSSHAIR_X = CANVAS_WIDTH / 2 - 50;
const CROSSHAIR_Y = CANVAS_HEIGHT / 2 - 50;
// --------------------------------------------------------------------
const CROSSHAIR_LENGHT = 100;
const CROSSHAIR_THICKNESS = 5;
const HIT_REG_SIZE = 25;
// --------------------------------------------------------------------
let crosshairX;
let crosshairY;
// --------------------------------------------------------------------
function renderCrosshair() {
  fill("black");
  // Horizontal
  rect(crosshairX - CROSSHAIR_LENGHT / 2, crosshairY, CROSSHAIR_LENGHT, CROSSHAIR_THICKNESS);
  // Vertical
  rect(crosshairX, crosshairY - CROSSHAIR_LENGHT / 2, CROSSHAIR_THICKNESS, CROSSHAIR_LENGHT);
}
// --------------------------------------------------------------------
function renderActor(a) {
  textSize(85);
  text(a, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2);
}
// --------------------------------------------------------------------
function moveCrosshair() {
  crosshairX = mouseX - CROSSHAIR_THICKNESS / 2; //  - CANVAS_WIDTH / 2
  crosshairY = mouseY - CROSSHAIR_THICKNESS / 2; //  - CANVAS_HEIGHT / 2
  /*
  joystick.onButtonPressed(function(eventObj){
  });*/
  
  //if (getButtonPressedByIndex(0, 0) == true){
   // console.log("pressed");
  //}
}
// --------------------------------------------------------------------
function hitRegRender() {
  if (mouseIsPressed) {
    fill(255);
    circle(crosshairX + CROSSHAIR_THICKNESS / 2, crosshairY + CROSSHAIR_THICKNESS / 2, HIT_REG_SIZE);
    worker.postMessage('gunshot');
  }
}
// --------------------------------------------------------------------