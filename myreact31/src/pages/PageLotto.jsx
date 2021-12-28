import { useState } from "react";

function makeLottoNumbers() {
  const lottoSet = new Set(); // Set은 중복x
  while (lottoSet.size < 7) {
    let randomNum = Math.floor(Math.random() * 45) + 1;
    lottoSet.add(randomNum); // set은 add해서 넣어줌.(append, push 아님)
  }
  const lottoList = Array.from(lottoSet); // from을 쓰면 set객체를 배열로 변환해줌.
  lottoList.sort((a, b) => a - b);
  return lottoList;
}

function PageLotto() {
  const [numbers, setNumbers] = useState([10, 11, 12, 13, 14, 15, 16, 17]);

  const handleClick = () => {
    setNumbers(makeLottoNumbers());
    console.log("clicked");
  };

  return (
    <>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지</button>

      {/* 1번 방법 */}
      {/* <span style={{ margin: "2rem" }}>{numbers[0]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[1]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[2]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[3]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[4]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[5]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[6]}</span>
      <span style={{ display: "inline-block", margin: "2rem" }}>{numbers[7]}</span> */}

      {/* 2번 방법 */}
      {numbers.map((number) => {
        return (
          <span
            style={{
              display: "inline-block",
              margin: "2rem",
              backgroundColor: "lightcoral",
              width: "100px",
              height: "100px",
              borderRadius: "50%",
              textAlign: "center",
              lineHeight: "100px",
            }}
          >
            {number}
          </span>
        );
      })}
    </>
  );
}

export default PageLotto;
