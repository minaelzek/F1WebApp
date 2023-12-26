const express = require('express');
const mongoose = require('mongoose');
const passport = require('passport');
require('dotenv').config();

const app = express();

// Middleware for JSON parsing
app.use(express.json());

// Passport middleware
app.use(passport.initialize());

// Database Connection
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB Connected'))
    .catch(err => console.error(err));

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const FacebookStrategy = require('passport-facebook').Strategy;
const GitHubStrategy = require('passport-github').Strategy;
const LinkedInStrategy = require('passport-linkedin-oauth2').Strategy;
const User = require('./models/User');

// Passport Configurations
passport.use(new GoogleStrategy({
    // Google strategy configuration
}, (accessToken, refreshToken, profile, done) => {
    // Handle user profile
}));

passport.use(new FacebookStrategy({
    // Facebook strategy configuration
}, (accessToken, refreshToken, profile, done) => {
    // Handle user profile
}));

passport.use(new GitHubStrategy({
    // GitHub strategy configuration
}, (accessToken, refreshToken, profile, done) => {
    // Handle user profile
}));

passport.use(new LinkedInStrategy({
    // LinkedIn strategy configuration
}, (accessToken, refreshToken, profile, done) => {
    // Handle user profile
}));
// Google Authentication
app.get('/auth/google', passport.authenticate('google', { scope: ['profile', 'email'] }));
app.get('/auth/google/callback', passport.authenticate('google', { failureRedirect: '/' }), (req, res) => {
    // Successful authentication
});

// Repeat for Facebook, GitHub, LinkedIn
