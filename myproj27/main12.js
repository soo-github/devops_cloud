
// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const { melon_data: song_array } = require("./melon_data");

const artist_count_object = song_array
    .reduce((acc, { artist }) => {
        // if(!acc[artist]) acc[artist] = 0;
        acc[artist] ||= 0;
        // i = i || 1
        // i ||= 1
        acc[artist] += 1;
        return acc;
    }, {});

Object.values(artist_count_object)
    .filter(number => number >= 2)
    .length;


// const artist_count_object = song_array
//     .reduce((acc, { artist }) => {
//         acc[artist] ||= 0
//         acc[artist] += 1;
//         return acc;
//     }, {});


// const total = Object.values(artist_count_object)
//     .filter(count => count >= 2)
//     .length;


// console.log(total);