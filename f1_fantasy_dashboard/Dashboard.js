
import React from 'react';
import PredictionHistory from './PredictionHistory';
import NewPrediction from './NewPrediction';
import Leaderboard from './Leaderboard';
import './Dashboard.css';

const Dashboard = () => {
    return (
        <div className="dashboard-container">
            <header className="dashboard-header">
                <h1>F1 Fantasy Dashboard</h1>
            </header>
            <PredictionHistory />
            <NewPrediction />
            <Leaderboard />
        </div>
    );
}

export default Dashboard;
