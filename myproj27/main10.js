
// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

const { melon_data: song_array } = require("./melon_data");

// 1번 방법
// const bts_like = song_array.filter((song) => song.artist === '방탄소년단')
//     .reduce((acc, cur) => { return acc + cur.like }, 0);
// console.log(`방탄소년단의 좋아요 총 합은?  ${bts_like}`);


// sum을 사용하는 방법
Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
}

const result = song_array
    .filter(
        ({ artist }) => artist === '방탄소년단'
    )
    // .reduce((acc, { like }) => acc + like, 0);
    .map(({ like }) => like)
    .sum();

console.log("result :", result);
