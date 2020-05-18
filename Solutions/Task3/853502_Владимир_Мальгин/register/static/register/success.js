let timeLeftSpan = $("#timeLeft");
console.log(timeLeftSpan);
const urlParams = new URLSearchParams(window.location.search);
const fromUrl = urlParams.get("from");


let timeLeft=5;
function timeout() {
    timeLeftSpan.text(timeLeft);
    if (timeLeft > 0) {
        timeLeft--;
        setTimeout(timeout, 1000)
    } else {
        window.location.replace(fromUrl);
    }
}
timeout();
