
// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

const { melon_data: song_array } = require("./melon_data");

// const singer = new Set();
// for (song of song_array) {
//     singer.add(song.artist);
// }
// console.log(singer.size);


// 문제 풀이
// reduce를 사용
const artist_count = song_array
    // .map(({ artist }) => artist)
    .reduce((acc, { artist }) => {
        acc.add(artist);
        return acc;
    }, new Set())
    .size;

console.log(`artist_count : ${artist_count}`);


// const artist_array = song_array.map(({ artist }) => artist);
// const total1 = new Set(artist_array).size;

// console.log(`랭크된 가수는 ${total1}팀입니다.`);


// const total2 = song_array
//     .reduce((acc, { artist }) => {
//         acc.add(artist);
//         return acc;
//     }, new Set())
//     .size;

// console.log(`랭크된 가수는 ${total2}팀입니다.`);


