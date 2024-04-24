let port;
let connectBtn;
// --------------------------------------------------
let canvasWidth = 510;
let canvasHeight = 510;

let cSize = 40;
let cColor = [127, 127, 127];
const cObj = { x: 0, y: 0 };
let cPosition = [0, 0];

let state = 1;
// --------------------------------------------------
function setup() {
  generateCanvas();
  axis();

  port = createSerial();
  serialBtn();
}
// --------------------------------------------------

// --------------------------------------------------
function draw() {
  switch (state) {
    case 1:
      checkPort();
      break;
    case 2:
      read();
      update();
      write();
      break;
  }
}
// --------------------------------------------------

// --------------------------------------------------
function generateCanvas() {
  createCanvas(canvasWidth, canvasHeight, WEBGL);
  background(200);
}
function axis() {
  stroke("black");
  strokeWeight(5);
  line(-canvasWidth / 2, 0, 0, canvasWidth / 2, 0, 0);
  line(0, -canvasWidth / 2, 0, 0, canvasWidth / 2, 0);
  stroke("cyan");
}

function update() {
  cursorPosition();
  cursorColor();
  cursorRender();
}
function cursorPosition() {
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
// Serial
// --------------------------------------------------
function serialBtn() {
  connectBtn = createButton("Connect to micro:bit");
  connectBtn.position(80, 300);
  connectBtn.mousePressed(connectBtnClick);
  let sendBtn = createButton("PLAY");
  sendBtn.position(220, 300);
  sendBtn.mousePressed(sendBtnClick);
  fill("white");
  ellipse(width / 2, height / 2, 100, 100);
}

function connectBtnClick() {
  if (!port.opened()) {
    port.open("MicroPython", 115200);
    state = 1;
  } else {
    port.close();
  }
}

function sendBtnClick() {
  state = 2;
}

function checkPort() {
  if (!port.opened()) {
    connectBtn.html("Connect to micro:bit");
  } else {
    connectBtn.html("Disconnect");
  }
}

function write() {
  port.write("q");
}
function read() {
  if (port.availableBytes() > 0) {
    let dataRx = port.read(1);
    console.log(dataRx);
  }
}
