import { Button } from "react-bootstrap";
import { endpoints } from "../api";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const logout = async () => {
    const res = await endpoints.user.logout();
    if (res !== false) {
      navigate("/");
    }
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
