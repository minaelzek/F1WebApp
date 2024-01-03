import React, { useState } from "react";
import "./login.css"
import { Container, Form, Button, Col, Row } from 'react-bootstrap';
import { endpoints } from "../api";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async(e) => {
    e.preventDefault();

    await endpoints.user.login({
      username: username,
      password: password,
    });

    const userData = await endpoints.user.getUserInfo()
    console.log(userData)
  };

  return (
    <Container className="login d-flex align-items-center justify-content-center">
      <Form onSubmit={handleSubmit} className="col-8">
            <Form.Group  className="mb-3" controlId="formBasicUsername">
              <Form.Control
                type="username"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword" >
              <Form.Control
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </Form.Group >
            <div className="d-grid">
                <Button variant="main" type="submit">
                    Sign In
                </Button>
            </div>
            <Row className="mt-3">
          <Col>
            <p className="">
             <a href="/register">Register</a>
            </p>
          </Col>
          <Col>
            <p className="">
              <a href="/forgot-password">Forgot Password?</a>
            </p>
          </Col>
        </Row>
      </Form>
    </Container>
  );
};

const LoginHeader = () => {


    return(
        <div className="header">
            Welcome to F1 Fantasy
        </div>
    )
}

export {LoginForm, LoginHeader};
