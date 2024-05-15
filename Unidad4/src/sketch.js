const GAME_NAME = "micro:shooter";
const COMPANY_NAME = "Infinity Ga∞es";
const LOGO = '🚀';

let port;
let connectBtn;

let level = 1;


let worker = new Worker('worker.js');
// --------------------------------------------------------------------
function preload() {
  //loadSounds();
}
// --------------------------------------------------------------------
function setup() {
  initialize();
  createWorker();
}
// --------------------------------------------------------------------
function draw() {
  checkPortState();
  switch (state) {
    case 0:
      //initialize();
      break;
    case 1:
      _setup_();
      break;
    case 2:
      update();
      //messageWorker();
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
