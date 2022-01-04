import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";
import { Children } from "react/cjs/react.production.min";

function ProfileCard({
  member_id,
  setPageName,
  profileImage,
  name,
  role,
  facebookUrl,
  email,
}) {
  return (
    <div>
      <section>
        <nav className="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>

        <article className="profile">
          <img src={profileImage} alt="프로필 이미지" />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>

        <ul className="contact">
          <li>
            {/* <i className="fab fa-facebook-f"></i> */}
            <FontAwesomeIcon icon={faFacebook} />
            <span style={{ margin: "10px" }}>{facebookUrl}</span>
          </li>
          <li>
            {/* <i className="fas fa-envelope"></i> */}
            <FontAwesomeIcon icon={faEnvelope} />
            <span style={{ margin: "10px" }}>{email}</span>
          </li>
        </ul>

        {/* <nav className="others">
          <a onClick={() => setPageName("member1")}></a>
          <a onClick={() => setPageName("member2")}></a>
          <a onClick={() => setPageName("member3")}></a>
          <a onClick={() => setPageName("member4")}></a>
        </nav> */}

        <ProfileCard>
          <nav>{Children}</nav>
        </ProfileCard>
      </section>
    </div>
  );
}

export default ProfileCard;
