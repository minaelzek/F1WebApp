import { Navbar, Container, NavDropdown, Nav, Button } from "react-bootstrap";
import { useNavigate, useLocation } from "react-router-dom";
import { endpoints } from "../api";
import "./home.css"

const TopNavigation = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const logout = async () => {
    const res = await endpoints.user.logout();
    if (res !== false) {
      navigate("/");
    }
  };

  const isLoginPage = location.pathname === '/';
  const isregisterPage = location.pathname === '/register';

  if (isLoginPage || isregisterPage) {
    return null;
  }

  return (
    <Navbar className="nav">
      <Container>
        <Navbar.Brand className="nav" href="#home">F1 Fantasy</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
            <Button xs="auto" variant="main" type="submit" onClick={logout}>
            Sign out
          </Button>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default TopNavigation;
