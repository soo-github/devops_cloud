
// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const { melon_data: song_array } = require("./melon_data");

const like_list = song_array.filter(song => song.like >= 200000);
const mapped_like = like_list.map((fn) => fn.title);
console.log(mapped_like);
