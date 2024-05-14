let port;
let connectBtn;

var song;
// --------------------------------------------------------------------
function preload() {
  soundExpl = loadSound(pathExpl);
}
// --------------------------------------------------------------------
function setup() {
  initialize();
}
// --------------------------------------------------------------------
function draw() {
  checkPortState();
  switch (state) {
    case 0:
      initialize();
      break;
    case 1:
      _setup_();
      break;
    case 2:
      configure();
      break;
    case 3:
      countdown();
      break;
    case 4:
      explode();
      break;
    case 5:
      disarm();
      break;
  }
  console.log("state = " + state);
}
// --------------------------------------------------------------------
