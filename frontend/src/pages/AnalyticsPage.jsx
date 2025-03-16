import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AnalyticsPage = () => {
    const [analytics, setAnalytics] = useState({});

    useEffect(() => {
        const fetchAnalytics = async () => {
            try {
                const response = await axios.get('/api/analytics');
                setAnalytics(response.data);
            } catch (error) {
                console.error('Error fetching analytics:', error);
            }
        };
        fetchAnalytics();
    }, []);

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-8">Analytics</h1>
            <div className="grid grid-cols-2 gap-8">
                <div className="bg-white p-4 rounded-lg shadow">
                    <h2 className="text-xl font-bold">Active Users</h2>
                    <p>{analytics.active_users}</p>
                </div>
                <div className="bg-white p-4 rounded-lg shadow">
                    <h2 className="text-xl font-bold">Total Requests</h2>
                    <p>{analytics.total_requests}</p>
                </div>
            </div>
        </div>
    );
};

export default AnalyticsPage;