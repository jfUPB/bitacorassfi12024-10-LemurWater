var joystick;


function setJoystick() {
  createCanvas(window.innerWidth, window.innerHeight);

  joystick = createJoystick();
  if (!joystick.calibrated()) joystick.calibrate(true);
  joystick.onButtonPressed(onJoystick);
  joystick.onButtonReleased(onJoystick);
  joystick.onAxesPressed(onJoystick);
  joystick.onAxesReleased(onJoystick);
}
// --------------------------------------------------------------------
function drawJoystick() {
  background(100);
  joystick.draw(width / 2, height / 2);
}
// --------------------------------------------------------------------
function onJoystick(e) {
  console.log("onJoystick", e);
}
// --------------------------------------------------------------------
