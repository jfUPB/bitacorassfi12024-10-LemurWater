const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 400;
const CANVAS_COLOR = 40;

let explosion_size;
let explosion_counter;

let EXPLOSION_SIZE_ = 25;
let EXPLOSION_COUNTER_ = 0;
let EXPLOSION_RATE = 1.025;
let EXPLOSION_MAX = 220;
// --------------------------------------------------------------------
const CIVILIAN_1 = "🤰";
const CIVILIAN_2 = "👶";
// --------------------------------------------------------------------
const ENEMY_1 = "😈";
const ENEMY_2 = "👻";
const ENEMY_3 = "👺";
const ENEMY_4 = "👹";
const ENEMY_5 = "👾";
const ENEMY_6 = "🤖";
const ENEMY_7 = "🎃";
// --------------------------------------------------------------------
const CLOWN = "🤡";
const ALIEN = "👽";
// --------------------------------------------------------------------
const OIL = '🛢️';

const ARMOR = "🪖";
const HEALTH = "❤️‍🩹";
const PICKUP = "🎁";
const STONE = "🗿";

const POO = "💩";
const KEY = "🔑";

const DOOR = "🚪";
// --------------------------------------------------------------------
function setWindow() {
  createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
  background(CANVAS_COLOR);
}
// --------------------------------------------------------------------
function intro() {
  textSize(300);
  text(ENEMY_5, 200, 280);
  ellipse(CANVAS_WIDTH / 2 - 12, 190, 250, 80);
  textSize(40);
  text(GAME_NAME, CANVAS_WIDTH / 2 - 134, CANVAS_HEIGHT / 2);
  textSize(26);
  text(COMPANY_NAME, CANVAS_WIDTH / 2 - 85, CANVAS_HEIGHT / 2 + 190);
}
// --------------------------------------------------------------------
function renderMap() {
  switch (level) {
    case 1:
      // Background
      fill("darkgrey");
      rect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
      // Front
      fill("lightblue");
      rect(280, 0, 200, 400);
      // Floor
      fill("grey");
      ellipse(CANVAS_WIDTH / 2, CANVAS_HEIGHT, CANVAS_WIDTH, 200);
      break;
    case 2:
      // Front
      fill("lightgreen");
      rect(30, 20, 55, 55);
      // Floor
      fill("darkgreen");
      ellipse(CANVAS_WIDTH / 2, CANVAS_HEIGHT, CANVAS_WIDTH, 200);
      break;
    case 3:
      // Front
      fill("pink");
      rect(30, 20, 55, 55);
      // Floor
      fill("darkred");
      ellipse(CANVAS_WIDTH / 2, CANVAS_HEIGHT, CANVAS_WIDTH, 200);
      break;
  }
}
// --------------------------------------------------------------------
function renderExplosion() {
  if (explosion_counter > EXPLOSION_MAX) {
    explosion_counter = 0;
    state = 1;
    return;
  } else {
    explosion_counter++;

    explosion_size *= EXPLOSION_RATE;
    fill(color("white"));
    circle(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, explosion_size);
  }
}
// --------------------------------------------------------------------
