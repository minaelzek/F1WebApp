import React, { useState } from "react";
import { endpoints } from "../api";
import { Container, Form, Button, Col, Row, Alert } from "react-bootstrap";

const RegisterPage = () => {
  const [registerData, setRegisterData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });

  const [passwordMatchError, setPasswordMatchError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (registerData.password !== registerData.confirmPassword) {
      setPasswordMatchError(true);
      return;
    }

    const { confirmPassword, ...dataWithoutConfirmPassword } = registerData;

    await endpoints.user.register(dataWithoutConfirmPassword);
    await endpoints.user.login({
        username: registerData.username,
        password: registerData.password,
      })
    const userData = await endpoints.user.getUserInfo()
    console.log(userData)
    // TODO: direct user to home page
  };

  return (
    <Container className="login d-flex align-items-center justify-content-center">
      <Form onSubmit={handleSubmit} className="col-4">
        <h1 className="mb-5">Create New Account</h1>
        <Row className="mb-3">
          <Form.Group as={Col} controlId="forFirstName">
            <Form.Control
              type="text"
              placeholder="First Name"
              value={registerData.first_name}
              onChange={(e) =>
                setRegisterData((prevData) => ({
                  ...prevData,
                  first_name: e.target.value,
                }))
              }
              required
            />
          </Form.Group>
          <Form.Group as={Col} controlId="formLastName">
            <Form.Control
              type="text"
              placeholder="Last Name"
              value={registerData.last_name}
              onChange={(e) =>
                setRegisterData((prevData) => ({
                  ...prevData,
                  last_name: e.target.value,
                }))
              }
              required
            />
          </Form.Group>
        </Row>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Control
            type="email"
            placeholder="Email"
            value={registerData.email}
            onChange={(e) =>
              setRegisterData((prevData) => ({
                ...prevData,
                email: e.target.value,
              }))
            }
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicUsername">
          <Form.Control
            type="text"
            placeholder="Username"
            value={registerData.username}
            onChange={(e) =>
              setRegisterData((prevData) => ({
                ...prevData,
                username: e.target.value,
              }))
            }
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Control
            type="password"
            placeholder="Password"
            value={registerData.password}
            onChange={(e) =>
              setRegisterData((prevData) => ({
                ...prevData,
                password: e.target.value,
              }))
            }
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formConfirmPassword">
          <Form.Control
            type="password"
            placeholder="Confirm Password"
            value={registerData.confirmPassword}
            onChange={(e) =>
              setRegisterData((prevData) => ({
                ...prevData,
                confirmPassword: e.target.value,
              }))
            }
            required
          />
        </Form.Group>
        {passwordMatchError && (
          <Alert variant="danger" className="mb-3">
            Passwords do not match.
          </Alert>
        )}
        <div className="d-flex justify-content-center">
          <Button variant="main" type="submit">
            Sign Up
          </Button>
        </div>
      </Form>
    </Container>
  );
};

export default RegisterPage;
