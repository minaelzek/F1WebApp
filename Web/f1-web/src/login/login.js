import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./login.css";
import { Container, Form, Button, NavLink } from "react-bootstrap";
import { endpoints } from "../api";
import Cookies from 'js-cookie';

const LoginForm = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const loginRes = await endpoints.user.login({
      username: username,
      password: password,
    });
    console.log(loginRes);
    if (loginRes !== false) {
      const userData = await endpoints.user.getUserInfo();
      console.log(userData);
      navigate("/home");
    }
  };

  //   TODO: better way of checking if user is logged in, check for sessionId and csrf token in cookies or create another endpoint for checkIfLoggedIn
  const checkIfUserIsLoggedIn = async () => {
    const sessionId = Cookies.get('sessionid');
    const csrfToken = Cookies.get('csrftoken');
    if (sessionId && csrfToken) {
      const user = await endpoints.user.getUserInfo();
      if (user) {
        navigate("/home");
      }
    }

    const user = await endpoints.user.getUserInfo();
    if (user) {
      navigate("/home");
    }
  };
  useEffect(() => {
    checkIfUserIsLoggedIn();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <Container className="login-form-border d-flex align-items-center justify-content-center">
      <Form onSubmit={handleSubmit} className="col-7">
        <Form.Group className="mb-3" controlId="formBasicUsername">
          <Form.Control
            type="username"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </Form.Group>
        <Form.Group className="mb-1" controlId="formBasicPassword">
          <Form.Control
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </Form.Group>
        <div>
          <div className="row">
            <div className="col-6">
              <NavLink href="/forgot-password" className="">
                Forgot Password?
              </NavLink>
            </div>
            <div className="col-12 d-flex justify-content-center mt-3">
              <Button variant="main" type="submit" className="col-12">
                Sign In
              </Button>
            </div>
          </div>
          <div className="row justify-content-center">
            <div className="col-6 ">
              <NavLink href="/register" className="mt-3">
                Register
              </NavLink>
            </div>
          </div>
        </div>
      </Form>
    </Container>
  );
};

const LoginHeader = () => {
  return <div className="header">Welcome to F1 Fantasy</div>;
};

export { LoginForm, LoginHeader };
