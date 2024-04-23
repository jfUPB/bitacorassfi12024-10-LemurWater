// serial_ascii.js
// --------------------------------------------------------------------
function startSerial() {
  port = createSerial();
  connectBtn = createButton("Connect to micro:bit");
  connectBtn.position(300, 345);
  connectBtn.mousePressed(connectBtnClick);
}

function connectBtnClick() {
  if (!port.opened()) {
    port.open("MicroPython", 115200);
  } else {
    port.close();
  }
}
function checkPortState() {
  if (!port.opened()) {
    connectBtn.position(300, 345);
    connectBtn.html("Connect to micro:bit");
  } else {
    state = 1;
    console.log("state 1 - bomb");
    connectBtn.position(320, 345);
    connectBtn.html("Disconnect");
  }
}
// --------------------------------------------------------------------
