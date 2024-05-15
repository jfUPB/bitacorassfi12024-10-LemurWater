let state;
let subState;
let timer;
let STATE_ = 1;
let SUBSTATE_ = 1;
let TIMER_ = 5;

let wireIndex = 0;
let WIRE_INDEX_ = 0;

let buttonTimer;
let buttonNext;
// --------------------------------------------------------------------
function initialize() {
  setWindow();
  intro();
  startSerial();
  state = 1;
}
// --------------------------------------------------------------------
function _setup_() {
  if (!port.opened()) {
    return;
  }
  state = 2;
  switch (subState) {
    case 1:
      //drawJoystick();
      break;
    case 2:
      state = 2;
      break;
  }
}
function update(){
  renderMap();
  renderActor(ENEMY_1);

  moveCrosshair();
  renderCrosshair();
  hitRegRender();
}
// --------------------------------------------------------------------
function configure() {
  switch (receiveSerial()) {
    case "+":
      timerIncrease();
      setTimer();
      break;
    case "3":
      state = 3;
      break;
  }
}
// --------------------------------------------------------------------
function timerIncrease() {
  if (timer > 59) {
    timer = 5;
  } else {
    timer = timer + 5;
  }
}
// --------------------------------------------------------------------
function countdown() {
  switch (receiveSerial()) {
    case "t":
      timer = timer - 1;
      setTimer();
      switch (timer) {
        case timer > 10:
          fill("yellow");
          break;
        case timer < 11 && timer > 5:
          fill("orange");
          break;
        default:
          fill("red");
          break;
      }
      break;
    case "/":
      wireIndex++;
      break;
    case "4":
      state = 4;
      break;
    case "5":
      state = 5;
      break;
  }
  renderWires();
  bomb();
  setTimer();
}
// --------------------------------------------------------------------
function explode() {
  fill("black");
  if (reproducing == false) {
    reproducing = true;
    soundExpl.play();
  }
  renderExplosion();
}
// --------------------------------------------------------------------
function disarm() {
  fill("green");
  state = 1;
}
// --------------------------------------------------------------------
