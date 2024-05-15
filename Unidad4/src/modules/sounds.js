let pathBGM = '/assets/background_music.mp3';
let pathGunshot = '/assets/gunshot.mp3';
let soundBGM;
let soundGunshot;
let reproducingBGM = false;
// --------------------------------------------------------------------
function loadSounds() {
  //soundBGM = loadSound(pathBGM);
  //soundGunshot = loadSounds(pathGunshot);
}
// --------------------------------------------------------------------
function playBGM() {
  //soundFormats('mp3', 'ogg', 'wav');
  
  if (soundBGM.isPlaying() == false) {
    soundBGM.play();
  }
}
// --------------------------------------------------------------------
function playGunshot() {
  //soundFormats('mp3', 'ogg', 'wav');
  
  soundGunshot.play();
}
// --------------------------------------------------------------------