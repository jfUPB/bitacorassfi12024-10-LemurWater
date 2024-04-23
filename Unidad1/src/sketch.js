// micro_bomb.js
// --------------------------------------------------------------------
let port;
let connectBtn;

let state = 1;
// --------------------------------------------------------------------
function setup() {
  setWindow();
  intro();

  startSerial();
}
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
