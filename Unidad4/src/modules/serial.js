function startSerial() {
  port = createSerial();
  connectBtn = createButton("Connect to micro:bit");
  connectBtn.position(CANVAS_WIDTH / 2 - 50, 250);
  connectBtn.mousePressed(connectBtnClick);
}
// --------------------------------------------------------------------
function connectBtnClick() {
  if (!port.opened()) {
    port.open("MicroPython", 115200);
  } else {
    port.close();
  }
}
// --------------------------------------------------------------------
function checkPortState() {
  if (!port.opened()) {
    connectBtn.position(CANVAS_WIDTH / 2 - 80, 300);
    connectBtn.html("Connect to micro:bit");
  } else {
    connectBtn.position(350, 300);
    connectBtn.html("Disconnect");
  }
}
// --------------------------------------------------------------------
function sendSerial(message) {
  port.write(message);
}
// --------------------------------------------------------------------
function receiveSerial() {
  if (port.availableBytes() > 0) {
    let dataRx = port.read(1);
    return dataRx;
  }
  return null;
}
// --------------------------------------------------------------------
function ThisButton() {
  background(220);
  ellipse(width / 2, height / 2, 100, 100);
  fill("black");
  text(dataRx, width / 2, height / 2);
}
// --------------------------------------------------------------------
