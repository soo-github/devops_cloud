
// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const { melon_data: song_array } = require("./melon_data");

// const mapped_array = song_array.map((song) => ({
//     title: song.title,
//     length: song.title.split(' ').length
// }));
//
// for (const song of mapped_array) {
//     console.log(`${song.title} / ${song.length}`);
// }


// 문제 풀이

// 1개의 song object을 문자열로 변환
const title_array1 = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return `${song.title} / ${word_count}`;
    },
);

// 기존 song_array 배열에서
// word_count 라는 컬럼을 추가하고 싶다.
const new_song_array = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return {
            ...song,
            word_count: word_count,
        };
    },
);

for (const new_song of new_song_array) {
    console.log(new_song);  // 기존 song + word_count 컬럼
}

