
// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const like_array = song_array.sort(function (song1, song2) {
    if (song1.title > song2.title) {
        return 1;
    }
    if (song1.title < song2.title) {
        return -1;
    }
    return 0;
}).filter(song => song.like >= 200000);

for (const song of like_array) {
    console.log(`[${song.like}]`, song.title, song.artist);
}
