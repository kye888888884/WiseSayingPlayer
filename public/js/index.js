const rv = responsiveVoice;

document.getElementById("play").addEventListener("click", () => {
  let n = 5;
  let idxs = new Set();
  while (idxs.size < n) idxs.add(Math.floor(Math.random() * data.length));

  let msgs = [];
  Array.from(idxs)
    .map((v) => {
      return [data[v].author, data[v].message];
    })
    .forEach((v) => {
      msgs.push(v[0], v[1]);
    });

  speakArray(msgs, "Male", { pitch: 1, rate: 0.8 });
});

function speak(str, gender = "Male", options = {}) {
  return new Promise((resolve) => {
    options.onend = () => {
      resolve();
    };
    rv.speak(str, gender === "Male" ? "Korean Male" : "Korean Female", options);
  });
}

async function speakArray(arr, gender = "Male", options = {}) {
  //speak(arr[0], gender, options).then(() => {
  //  arr.shift();
  //  if (arr.length > 0) speakArray(arr, gender, options);
  //});

  await speak(arr[0], gender, options);
  arr.shift();
  if (arr.length > 0) speakArray(arr, gender, options);
}
