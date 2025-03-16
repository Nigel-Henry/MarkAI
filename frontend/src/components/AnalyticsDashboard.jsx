import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AnalyticsDashboard = () => {
    const [analytics, setAnalytics] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAnalytics = async () => {
            try {
                const response = await axios.get('/api/analytics');
                setAnalytics(response.data);
            } catch (error) {
                console.error('Error fetching analytics:', error);
                setError('Failed to fetch analytics data.');
            } finally {
                setLoading(false);
            }
        };

        fetchAnalytics();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Analytics Dashboard</h2>
            <div className="grid grid-cols-3 gap-4">
                <div className="p-4 bg-blue-100 rounded">
                    <p className="font-bold">Users</p>
                    <p>{analytics.users_count}</p>
                </div>
                <div className="p-4 bg-green-100 rounded">
                    <p className="font-bold">Tasks</p>
                    <p>{analytics.tasks_count}</p>
                </div>
                <div className="p-4 bg-yellow-100 rounded">
                    <p className="font-bold">Tickets</p>
                    <p>{analytics.tickets_count}</p>
                </div>
            </div>
        </div>
    );
};

export default AnalyticsDashboard;