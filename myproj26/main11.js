const fs = require("fs");
const fsPromises = fs.promises;

// await 는 promise 문법에 대한 축약
// await는 함수명 앞에 async를 붙여야함.
async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loaded :", files);
    }
    catch (error) {
        console.log(error);
    }
}

main();



// 2번: Promise
// fsPromises.readdir("c:/Dev")
//     .then(function (files) {
//         console.log("loaded:", files);
//     })
//     .catch(function (error) {
//         console.log(error);
//     });


// 1번: Callback
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// });


console.log("ENDED");