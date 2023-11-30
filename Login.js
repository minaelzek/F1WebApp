import React from 'react';
import { useHistory } from 'react-router-dom'; // Import useHistory hook for redirection
import './style.css'; // Assuming the CSS is saved as style.css

const Login = () => {
    const history = useHistory(); // Initialize useHistory hook

    const handleLogin = (event) => {
        event.preventDefault(); // Prevent the default form submission behavior
        const username = event.target.username.value;
        const password = event.target.password.value;

        // Check if both username and password are empty
        if (username === "" && password === "") {
            // Redirect to the dashboard page
            history.push('/dashboard'); // Replace '/dashboard' with your actual dashboard route
        } else {
            // Here you can add your login validation logic if username and password are not empty
        }
    };

    return (
        <div className="login-container">
            <form className="login-form" onSubmit={handleLogin}>
                <h1>F1 Fantasy Login</h1>
                <input type="text" placeholder="Username" name="username"/>
                <input type="password" placeholder="Password" name="password"/>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;
