
// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

// const slice_fn = song_array.sort(function (song1, song2) {
//     return song2.like - song1.like;
// }).slice(0, 10);
//
//
// for (const song of slice_fn) {
//     console.log(`[${song.like}] ${song.title}, ${song.artist}`);
// }


// 문제 풀이

// 좋아요 수에 대한 내림차순 정렬 -> 처음 10개
const like_top10 = song_array
    .sort(
        (song1, song2) => song2.like - song1.like,
    )
    .slice(0, 10);

// 인덱스(1,2,3...) 붙임
for (const [index, { like, title, artist }] of like_top10.entries()) {
    console.log(`${index + 1} [${like}] ${title} by ${artist}`);
}


