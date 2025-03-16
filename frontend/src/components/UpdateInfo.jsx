import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UpdateInfo = () => {
    const [updateInfo, setUpdateInfo] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchUpdateInfo = async () => {
            try {
                const response = await axios.get('/api/updates');
                setUpdateInfo(response.data);
            } catch (error) {
                setError('Error fetching update info');
                console.error('Error fetching update info:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchUpdateInfo();
    }, []);

    if (loading) {
        return <div className="p-4 bg-white rounded-lg shadow">Loading...</div>;
    }

    if (error) {
        return <div className="p-4 bg-white rounded-lg shadow">{error}</div>;
    }

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Update Information</h2>
            <p><strong>Version:</strong> {updateInfo.version}</p>
            <p><strong>Release Notes:</strong> {updateInfo.release_notes}</p>
        </div>
    );
};

export default UpdateInfo;