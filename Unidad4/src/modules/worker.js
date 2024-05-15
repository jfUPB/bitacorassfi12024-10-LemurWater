onmessage = function (e) {
    console.log("worker working!");
    switch(e.data) {
        case 'bgm':
            playBGM();
            break;
        case 'gunshot':
            playGunshot();
            break;
    }
 }
 // --------------------------------------------------------------------
function createWorker() {
    worker.onmessage = function(event) {
        console.log("worker created!");
     };
}
function workerBGM() {
    worker.postMessage('bgm');
}
function workerGunshot() {
    worker.postMessage('gunshot');
}
// --------------------------------------------------------------------
