import logo from "./logo.svg";
import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./ProfileCard.jsx";
import { useState } from "react";
import member_list from "./profileCard.json";
import { render } from "@testing-library/react";

function App() {
  const [pageName, setPageName] = useState("member1");

  return (
    <>
      {/* <PageLotto /> */}

      {member_list.map((member, index) => {
        if (pageName === member.member_id) {
          return (
            <div className={`member${(index % 4) + 1}`}>
              <ProfileCard {...member}>
                <nav className="others">
                  <a onClick={() => setPageName("member1")}></a>
                  <a onClick={() => setPageName("member2")}></a>
                  <a onClick={() => setPageName("member3")}></a>
                  <a onClick={() => setPageName("member4")}></a>
                </nav>
              </ProfileCard>
            </div>
          );
        }
      })}
    </>
  );
}

export default App;
