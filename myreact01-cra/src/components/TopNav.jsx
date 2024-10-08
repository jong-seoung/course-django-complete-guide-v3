import { NavLink } from "react-router-dom";
import { Alert, Container, Nav, Navbar, NavDropdown } from "react-bootstrap";
import { LOGIN_URL, LOGOUT_URL, PROFILE_URL, SIGNUP_URL } from "../constants";
import { useStatusContext } from "../contexts/StatusContext";

// Alert 컴포넌트의 variant 속성
//  - https://react-bootstrap.github.io/docs/components/alerts/#alert
const VARIANT_MAP = {
  debug: "secondary",
  info: "info",
  success: "success",
  warning: "warning",
  error: "danger",
};

function TopNav() {
  const {
    is_authenticated = null,
    username = "",
    messages = [],
  } = useStatusContext();

  return (
    <>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand to={"/"} as={NavLink}>
            파이썬 사랑방
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto" variant="underline">
              <Nav.Link to="/blog" as={NavLink}>
                블로그
              </Nav.Link>
              <Nav.Link to="/about" as={NavLink}>
                소개
              </Nav.Link>
              {is_authenticated !== null && (
                <NavDropdown title="계정" id="basic-nav-dropdown">
                  {!is_authenticated && (
                    <>
                      <NavDropdown.Item
                        to={`${LOGIN_URL}?next=${window.location.href}`}
                        as={NavLink}
                      >
                        로그인
                      </NavDropdown.Item>
                      <NavDropdown.Item to={SIGNUP_URL} as={NavLink}>
                        회원가입
                      </NavDropdown.Item>
                    </>
                  )}
                  {is_authenticated && (
                    <>
                      <NavDropdown.Item to={PROFILE_URL} as={NavLink}>
                        프로필
                      </NavDropdown.Item>
                      <NavDropdown.Divider />
                      <NavDropdown.Item
                        to={`${LOGOUT_URL}?next=${window.location.href}`}
                        as={NavLink}
                      >
                        로그아웃
                      </NavDropdown.Item>
                    </>
                  )}
                </NavDropdown>
              )}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      {is_authenticated !== null && (
        <Container>
          <Alert variant="info" className="mt-2">
            Your username is <strong>{username}</strong>.
          </Alert>
        </Container>
      )}

      {messages.length > 0 && (
        <Container>
          {messages.map((message, index) => (
            <Alert
              key={index}
              variant={VARIANT_MAP[message.tags]}
              className="mt-2"
            >
              {message.message}
            </Alert>
          ))}
        </Container>
      )}
    </>
  );
}

export default TopNav;