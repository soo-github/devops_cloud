
const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

const { question } = require("readline-sync");


// let shuffle = () => Math.floor(Math.random() * animal_names.length);
// const array = [...animal_names].map(_ => animal_names.splice(shuffle(), 1)[0]);
// console.log(array);

const shuffle = () => Math.floor(Math.random() * animal_names.length);
const array = [...animal_names].map(_ => animal_names.splice(shuffle(), 1)[0]);
const slice_names = array.slice(0, 5);
// console.log(slice_names);


const begin_time = new Date().getTime();

let ok_counter = 0;

for (random_name of slice_names) {
    console.log(random_name);
    const line = question(">>> ");
    if (line == random_name) {
        ok_counter += 1;
        console.log("정확합니다.");
    }
    else {
        console.log("오타가 있어요.");
    }
}

const end_time = new Date().getTime();
const total = (end_time - begin_time)/1000;
const sec = parseInt(total);

console.log(`${ok_counter}번 성공하셨습니다.`);
console.log(`총 ${sec}초가 걸리셨어요.`);
