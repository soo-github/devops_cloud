

const mysum2 = (x, y) => { x, y };
console.log(mysum2(1, 2));  // 리턴이 없어서 undefined


const mysum3 = (x, y) => {
    return { x, y };
};
console.log(mysum3(1, 2));


const mysum4 = (x, y) => ({ x, y });  // 리턴을 써주던지, 아니면 ()를 넣어줌.
console.log(mysum4(1, 2));
