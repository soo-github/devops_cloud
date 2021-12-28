import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import LottoNum from 'components/LottoNum';
// import PageLotto from 'pages/PageLotto';
// import PagePlaylist from 'pages/PagePlaylist';
import TopNav from 'components/TopNav';
import { useState } from 'react';

function App() {
  const [pageName, setPageName] = useState('about');

  const changePageName = (pageName) => {
    setPageName(pageName);
  };

  return (
    <div>
      <h1>김수인의 리액트</h1>
      <TopNav changePageName={changePageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {/* {pageName === 'lotto' && <PageLotto />}
      {pageName === 'playlist' && <PagePlaylist />} */}
      {pageName === 'lotto' && <LottoNum />}
    </div>
  );
}

export default App;
