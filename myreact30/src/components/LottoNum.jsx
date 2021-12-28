import { useState, useEffect } from 'react';

function LottoNum() {
  const [lotto, setLotto] = useState([]);

  // let L_num = [];
  // let randomNum = 0;
  // let i = 0;

  // for (i = 0; i < 7; i++) {
  //   randomNum = Math.floor(Math.random() * 45) + 1;
  //   if (L_num.indexOf(randomNum) === -1) {
  //     L_num.push(randomNum);
  //   } else {
  //     i--;
  //   }
  // }
  // console.log(L_num);
  // return L_num;

  function make_LottoNum() {
    let L_num = [];
    let R_num = 0;
    let i = 0;

    let lottos = [];
    let a = 0;

    for (i = 1; i <= 45; i++) {
      lottos.push(i);
    }

    for (i = 0; i <= 44; i++) {
      R_num = Math.floor(Math.random() * 45);

      a = lottos[i];
      lottos[i] = lottos[R_num];
      lottos[R_num] = a;
    }
    console.log(lottos);

    for (i = 0; i < 7; i++) {
      L_num.push(lottos[i]);
    }

    setLotto(L_num);
  }

  const handleClick = () => {
    setLotto(make_LottoNum);
  };

  useEffect(() => {
    make_LottoNum();
  }, []);

  return (
    <>
      <h2>로또 번호 예지</h2>
      {/* <button onProgress={() => make_LottoNum()}>예지</button> */}
      <button onClick={handleClick}>예지</button>
      <div>{lotto}</div>
    </>
  );
}

export default LottoNum;
