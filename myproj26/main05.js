// Array
// js는 파이썬과 달리 좌항과 우항 개수가 같지 않아도 됨.
// const [name] = ["Tom", 10, "Seoul"];

// const [, age] = ["Tom", 10, "Seoul"];

// // hegith는  undefined가 나옴.
// const [name, age, region, height] = ["Tom", 10, "Seoul"];

// // 값 할당에 실패했을 때, 적용되는 디폴트 값
// const [name, age, region, height = 140] = ["Tom", 10, "Seoul"];

// 디폴트 값을 함수 호출로 지정: 디폴트 값이 필요한 시점에 함수가 호출 됨.
function get_default_heght() {
    console.log("get_default_gehht 함수를 호출했습니다.");
    return 140;
}
const [name, age, region, height = get_default_heght()] = ["Tom", 10, "Seoul"];
