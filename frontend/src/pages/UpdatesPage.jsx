import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UpdatesPage = () => {
    const [updates, setUpdates] = useState([]);

    useEffect(() => {
        const fetchUpdates = async () => {
            try {
                const response = await axios.get('/api/updates');
                setUpdates(response.data.updates);
            } catch (error) {
                console.error('Error fetching updates:', error);
            }
        };
        fetchUpdates();
    }, []);

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-8">Updates</h1>
            <div className="bg-white p-4 rounded-lg shadow">
                {updates.map((update, index) => (
                    <div key={index} className="mb-4">
                        <h2 className="text-xl font-bold">{update[1]}</h2>
                        <p>{update[2]}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UpdatesPage;