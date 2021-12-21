
// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const slice_fn = song_array.sort(function (song1, song2) {
    return song2.like - song1.like;
}).slice(0, 10);


for (const song of slice_fn) {
    console.log(song.like, song.title, song.artist);
}
