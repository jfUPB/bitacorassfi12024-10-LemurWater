let port;
let connectBtn;

let state = 0;
let pause = false;
let send = false;

let sendBuffer = "mf";

// the snake is divided into small segments, which are drawn and edited on each 'draw' call
let numSegments = 10;
let direction = "right";

const xStart = 0; //starting x coordinate for snake
const yStart = 250; //starting y coordinate for snake
const diff = 10;

let xCor = [];
let yCor = [];

let xFruit = 0;
let yFruit = 0;
let scoreElem;
let counterQuestion = 0;

function setup() {
  port = createSerial();
  connectBtn = createButton("Connect to micro:bit");
  connectBtn.position(80, 500);
  connectBtn.mousePressed(connectBtnClick);

  scoreElem = createDiv("Score = 0");
  scoreElem.position(20, 20);
  scoreElem.id = "score";
  scoreElem.style("color", "white");

  createCanvas(500, 500);
  frameRate(5);
  stroke(255);
  strokeWeight(10);
  updateFruitCoordinates();

  for (let i = 0; i < numSegments; i++) {
    xCor.push(xStart + i * diff);
    yCor.push(yStart);
  }
}

function draw() {
  if (state == 0) {
    if (port.opened()) {
      state = 2;
    }
  } else if (state == 1) {
    setup();
    state = 2;
  } else if (state == 2) {
    background(0);
    for (let i = 0; i < numSegments - 1; i++) {
      line(xCor[i], yCor[i], xCor[i + 1], yCor[i + 1]);
    }

    if (pause == false) {
      counterQuestion++;
      if (counterQuestion === 5) {
        if (port.opened()) {
          port.write("Q\n");
        }
        counterQuestion = 0;
      }

      updateSnakeCoordinates();
      checkGameStatus();
      checkForFruit();

      //sendBuffer[0] = "M";

      //sendData();
      //sendBuffer = "mfp0";
    }

    if (port.availableBytes() > 0) {
      let dataRx = port.read(4); //1
      print("dataRx: " + dataRx);

      if (pause == false) {
        if (dataRx.includes("P")) {
          pause = true;
          //sendBuffer[0] = "m";
        }

        if (dataRx.includes("A")) {
          if (direction == "up") direction = "left";
          else if (direction == "down") direction = "right";
          else if (direction == "left") direction = "down";
          else direction = "up";
        }

        if (dataRx.includes("D")) {
          if (direction == "up") direction = "right";
          else if (direction == "down") direction = "left";
          else if (direction == "left") direction = "up";
          else direction = "down";
        }

        if (dataRx.includes("Q")) {
          
        }
      }
    }
  }

  if (!port.opened()) {
    connectBtn.html("Connect to micro:bit");
  } else {
    connectBtn.html("Disconnect");
  }
}

/*
 The segments are updated based on the direction of the snake.
 All segments from 0 to n-1 are just copied over to 1 till n, i.e. segment 0
 gets the value of segment 1, segment 1 gets the value of segment 2, and so on,
 and this results in the movement of the snake.

 The last segment is added based on the direction in which the snake is going,
 if it's going left or right, the last segment's x coordinate is increased by a
 predefined value 'diff' than its second to last segment. And if it's going up
 or down, the segment's y coordinate is affected.
*/
function updateSnakeCoordinates() {
  for (let i = 0; i < numSegments - 1; i++) {
    xCor[i] = xCor[i + 1];
    yCor[i] = yCor[i + 1];
  }
  switch (direction) {
    case "right":
      xCor[numSegments - 1] = xCor[numSegments - 2] + diff;
      yCor[numSegments - 1] = yCor[numSegments - 2];
      break;
    case "up":
      xCor[numSegments - 1] = xCor[numSegments - 2];
      yCor[numSegments - 1] = yCor[numSegments - 2] - diff;
      break;
    case "left":
      xCor[numSegments - 1] = xCor[numSegments - 2] - diff;
      yCor[numSegments - 1] = yCor[numSegments - 2];
      break;
    case "down":
      xCor[numSegments - 1] = xCor[numSegments - 2];
      yCor[numSegments - 1] = yCor[numSegments - 2] + diff;
      break;
  }
}

/*
 I always check the snake's head position xCor[xCor.length - 1] and
 yCor[yCor.length - 1] to see if it touches the game's boundaries
 or if the snake hits itself.
*/
function checkGameStatus() {
  if (
    xCor[xCor.length - 1] > width ||
    xCor[xCor.length - 1] < 0 ||
    yCor[yCor.length - 1] > height ||
    yCor[yCor.length - 1] < 0 ||
    checkSnakeCollision()
  ) {
    //noLoop();
    const scoreVal = parseInt(scoreElem.html().substring(8));
    scoreElem.html("Game ended! Your score was : " + scoreVal);

    setup();
  }
}

/*
 If the snake hits itself, that means the snake head's (x,y) coordinate
 has to be the same as one of its own segment's (x,y) coordinate.
*/
function checkSnakeCollision() {
  const snakeHeadX = xCor[xCor.length - 1];
  const snakeHeadY = yCor[yCor.length - 1];
  for (let i = 0; i < xCor.length - 1; i++) {
    if (xCor[i] === snakeHeadX && yCor[i] === snakeHeadY) {
      return true;
    }
  }
}

/*
 Whenever the snake consumes a fruit, I increment the number of segments,
 and just insert the tail segment again at the start of the array (basically
 I add the last segment again at the tail, thereby extending the tail)
*/
function checkForFruit() {
  point(xFruit, yFruit);
  if (xCor[xCor.length - 1] === xFruit && yCor[yCor.length - 1] === yFruit) {
    const prevScore = parseInt(scoreElem.html().substring(8));
    scoreElem.html("Score = " + (prevScore + 1));
    xCor.unshift(xCor[0]);
    yCor.unshift(yCor[0]);
    numSegments++;

    sendBuffer[1] = "F";
    sendBuffer[4] = (prevScore + 1).toString();

    updateFruitCoordinates();
  }
}

function updateFruitCoordinates() {
  /*
    The complex math logic is because I wanted the point to lie
    in between 100 and width-100, and be rounded off to the nearest
    number divisible by 10, since I move the snake in multiples of 10.
  */

  xFruit = floor(random(10, (width - 100) / 10)) * 10;
  yFruit = floor(random(10, (height - 100) / 10)) * 10;
}

function keyPressed() {
  switch (keyCode) {
    case 65: // A
      if (direction == "up") direction = "left";
      else if (direction == "down") direction = "right";
      else if (direction == "left") direction = "down";
      else direction = "up";
      break;

    case 68: // D
      if (direction == "up") direction = "right";
      else if (direction == "down") direction = "left";
      else if (direction == "left") direction = "up";
      else direction = "down";
      break;

    case 80: // Pause
      if (pause == false) pause = true;
      else pause = false;
      break;
  }
}

function connectBtnClick() {
  if (!port.opened()) {
    port.open("MicroPython", 115200);
  } else {
    port.close();
    state = 0;
  }
}

function sendData() {
  if (port.opened()) {
    port.write(sendBuffer);
  }
}
