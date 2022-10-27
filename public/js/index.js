const rv = responsiveVoice;
const json = require("/lib/maxim.json");

JSONtoArray();

document.getElementById("play").addEventListener("click", () => {
  speakArray(["안녕하세요", "반가워요", "뭘봐 씨바라마"]);
});

function speak(str, gender = "Male") {
  return new Promise((resolve) => {
    rv.speak(str, gender === "Male" ? "Korean Male" : "Korean Female", {
      onend: () => {
        console.log("끝났엉");
        resolve();
      },
    });
  });
}

function speakArray(arr, gender = "Male") {
  speak(arr[0], gender).then(() => {
    arr.shift();
    if (arr !== []) speakArray(arr, gender);
  });
}

function JSONtoArray(json) {
  console.log(JSON.parse(json));
}
