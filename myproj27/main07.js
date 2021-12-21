
// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(song => song.artist === '방탄소년단');
const bts_songlist = result.map((fn) => fn.title);
console.log(bts_songlist);
