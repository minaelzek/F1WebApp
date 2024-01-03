import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./login.css";
import { Container, Form, Button, Col, Row, NavLink } from "react-bootstrap";
import { endpoints } from "../api";

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
    console.log(loginRes)
    if (loginRes !== false) {
      const userData = await endpoints.user.getUserInfo();
      console.log(userData);
      navigate("/home");
    }
  };

//   TODO: better way of checking if user is logged in, check for sessionId and csrf token in cookies or create another endpoint for checkIfLoggedIn
  const checkIfUserIsLoggedIn = async () => {
    const user = await endpoints.user.getUserInfo()
    if(user){
        navigate('/home');
    }
  };
  useEffect(() => {
    checkIfUserIsLoggedIn();
  }, []);

  return (
    <Container className="login d-flex align-items-center justify-content-center">
      <Form onSubmit={handleSubmit} className="col-8">
        <Form.Group className="mb-3" controlId="formBasicUsername">
          <Form.Control
            type="username"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Control
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </Form.Group>
        <div className="d-grid">
          <Button variant="main" type="submit">
            Sign In
          </Button>
        </div>
        <Row className="mt-3">
          <Col>
            <p className="">
              <NavLink href="/register">Register</NavLink>
            </p>
          </Col>
          <Col>
            <p className="">
              <NavLink href="/forgot-password">Forgot Password?</NavLink>
            </p>
          </Col>
        </Row>
      </Form>
    </Container>
  );
};

const LoginHeader = () => {
  return <div className="header">Welcome to F1 Fantasy</div>;
};

export { LoginForm, LoginHeader };
