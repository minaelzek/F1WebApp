
import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
    const [leaders, setLeaders] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchLeaderboardData()
            .then(data => {
                setLeaders(data);
                setIsLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setIsLoading(false);
            });
    }, []);

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <section className="leaderboard">
            <h2>Leaderboard</h2>
            {leaders.map((leader, index) => (
                <div key={index}>
                    <p>{leader.name} - {leader.score}</p>
                </div>
            ))}
        </section>
    );
}

export default Leaderboard;
