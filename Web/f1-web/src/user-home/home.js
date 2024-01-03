import { Button } from "react-bootstrap";
import { endpoints } from "../api";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const logout = () => {
    endpoints.user.logout();
    navigate("/");
  };
  return (
    <div>
      <Button variant="main" type="submit" onClick={logout}>
        Sign out
      </Button>
    </div>
  );
};

export default HomePage;
