
// 객체
// const age = "나이";
// const tom = {
//     "name": "Tom",
//     //"age": 10, 이것과 아래 모두 가능
//     //age: 10,
//     //["ag"+"e"]: 10, // key에 계산을 해야하면 []를 넣음
//     [age]: 10,
// }
// console.log(tom);


const name = "Tom"
const age = 10
const tom1 = {
    name,    // name:name 처럼 key와 value가 같으면 생략 가능.
    age,
    print() {   // print: function () { 에서 줄여서 사용 가능
        //console.log(this.name, this.age);

        //Templage Literals
        console.log(`안녕. 나는 ${this.name}이야. 
${age}살이지.`);  // """ 없어도 기본적으로 여러 줄 출력 가능
    }
}

tom1.print()

