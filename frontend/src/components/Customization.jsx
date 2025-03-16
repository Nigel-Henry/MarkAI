import React, { useState } from 'react';
import axios from 'axios';

const Customization = () => {
    const [theme, setTheme] = useState('light');
    const [error, setError] = useState(null);

    const handleThemeChange = async (newTheme) => {
        try {
            await axios.post('/api/customization/theme', { theme: newTheme });
            setTheme(newTheme);
            setError(null);
        } catch (error) {
            console.error('Error changing theme:', error);
            setError('Failed to change theme. Please try again.');
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Customization</h2>
            {error && <p className="text-red-500 mb-4">{error}</p>}
            <select
                value={theme}
                onChange={(e) => handleThemeChange(e.target.value)}
                className="p-2 border rounded"
            >
                <option value="light">Light Theme</option>
                <option value="dark">Dark Theme</option>
            </select>
        </div>
    );
};

export default Customization;