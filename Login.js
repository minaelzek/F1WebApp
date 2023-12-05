import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './style.css'; 

const Login = () => {
    const [isLoginView, setIsLoginView] = useState(true); // State to toggle between login and register view
    const history = useHistory();

    const handleLogin = (event) => {
        event.preventDefault();
        const username = event.target.username.value;
        const password = event.target.password.value;

        // Add your login logic here
        // ...

        history.push('/Dashboard'); // Navigate to dashboard after login
    };

    const handleRegister = (event) => {
        event.preventDefault();
        // Add your registration logic here
        // ...
    };

    return (
        <div className="container">
            <div className={`form-container ${isLoginView ? "" : "sign-up"}`}>
                <form onSubmit={handleLogin}>
                    <h1>Sign In to F1 Fantasy</h1>
                    <input type="text" placeholder="Username" name="username" />
                    <input type="password" placeholder="Password" name="password" />
                    <button type="submit">Login</button>
                </form>
            </div>
            <div className={`form-container ${isLoginView ? "sign-up" : ""}`}>
                <form onSubmit={handleRegister}>
                    <h1>Create Account</h1>
                    <input type="text" placeholder="Name" name="name" />
                    <input type="email" placeholder="Email" name="email" />
                    <input type="password" placeholder="Password" name="password" />
                    <button type="submit">Sign Up</button>
                </form>
            </div>
            <div className="toggle-container">
                <div className="toggle">
                    <div className={`toggle-panel ${isLoginView ? "" : "toggle-right"}`}>
                        <h1>Welcome Back!</h1>
                        <p>To keep connected with us, please login with your personal info</p>
                        <button onClick={() => setIsLoginView(true)}>Sign In</button>
                    </div>
                    <div className={`toggle-panel ${isLoginView ? "toggle-left" : ""}`}>
                        <h1>Hello, Friend!</h1>
                        <p>Enter your personal details and start your journey with us</p>
                        <button onClick={() => setIsLoginView(false)}>Sign Up</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Login;
