
import React from 'react';
import './style.css'; // Assuming the CSS is saved as style.css

const Login = () => {
    return (
        <div className="login-container">
            <form className="login-form">
                <h1>F1 Fantasy Login</h1>
                <input type="text" placeholder="Username" name="username" required />
                <input type="password" placeholder="Password" name="password" required />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;
