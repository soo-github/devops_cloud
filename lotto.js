function makeLottoNumbers() {
  const lottoSet = new Set(); // Set은 중복x
  while (lottoSet.size < 7) {
    randomNum = Math.floor(Math.random() * 45) + 1;
    lottoSet.add(randomNum); // set은 add해서 넣어줌.(append, push 아님)
  }
  const lottoList = Array.from(lottoSet); // from을 쓰면 set객체를 배열로 변환해줌.
  lottoList.sort((a, b) => a - b);
  return lottoList;
}
console.log(makeLottoNumbers());
