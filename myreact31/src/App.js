import logo from "./logo.svg";
import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./ProfileCard.jsx";
import { useState } from "react";
import member_list from "./profileCard.json";

function App() {
  const [pageName, setPageName] = useState("member1");

  return (
    <>
      {/* <PageLotto /> */}

      {member_list.map((member, index) => {
        if (pageName === member.member_id) {
          return (
            <div>
              <ProfileCard {...member} setPageName={setPageName} />
            </div>
          );
        }
      })}
    </>
  );
}

export default App;
