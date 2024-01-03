import React, { useState } from "react";
import "./login.css"
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import { endpoints } from "../api";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    endpoints.login.user({
      username: username,
      password: password,
    });
  };

  return (
    <Container className=" d-flex align-items-center justify-content-center" style={{height: "1000px"}}>
      <Form onSubmit={handleSubmit} className="col-4">
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
      </Form>
    </Container>
  );
};

export default LoginForm;
