document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container');
    const registerBtn = document.getElementById('register');
    const loginBtn = document.getElementById('login');
    const signInForm = document.querySelector('.sign-in form');
    const signUpForm = document.querySelector('.sign-up form');

    // Existing event listeners for toggling forms
    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });

    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });

    // Handle Sign In Form Submission
    signInForm.addEventListener('submit', event => {
        event.preventDefault();
        const email = event.target.querySelector('input[type="email"]').value;
        const password = event.target.querySelector('input[type="password"]').value;

        // Implement your login logic here
        console.log('Sign In with:', email, password);
    });

    // Handle Sign Up Form Submission
    signUpForm.addEventListener('submit', event => {
        event.preventDefault();
        const name = event.target.querySelector('input[type="text"]').value;
        const email = event.target.querySelector('input[type="email"]').value;
        const password = event.target.querySelector('input[type="password"]').value;

        // Implement your registration logic here
        console.log('Sign Up with:', name, email, password);
    });

    // Social Media Login Logic
    // Example for Google Plus
    const googlePlusLogin = document.querySelectorAll('.fa-google-plus-g');
    googlePlusLogin.forEach(icon => {
        icon.addEventListener('click', event => {
            event.preventDefault();
            // Implement Google Plus Login Logic
            console.log('Google Plus Login');
        });
    });

    // Repeat for Facebook, GitHub, and LinkedIn
    // After repeating must implement backend
    // Consult Alex
});
