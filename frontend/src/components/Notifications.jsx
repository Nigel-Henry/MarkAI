import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('/api/notifications')
            .then(response => {
                setNotifications(response.data.notifications);
                setLoading(false);
            })
            .catch(error => {
                console.error(error);
                setError('Failed to fetch notifications');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div className="p-4 bg-white rounded-lg shadow">Loading...</div>;
    }

    if (error) {
        return <div className="p-4 bg-white rounded-lg shadow">{error}</div>;
    }

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Notifications</h2>
            <ul>
                {notifications.map((notification, index) => (
                    <li key={index} className="p-2 border-b">
                        {notification.message}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Notifications;