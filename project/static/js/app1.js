var texts = ["For Geeks!", "Gratifies Your Intellectual Curiosity", "For You, By You", "You Judge!"];
var count = 0;
function changeText() {
        $("#changeText").text(texts[count]);
            count < 3 ? count++ : count = 0;
}
setInterval(changeText, 3000);