import React, { useState } from 'react';
import axios from 'axios';

const SecuritySettings = () => {
    const [secret, setSecret] = useState('');
    const [token, setToken] = useState('');
    const [error, setError] = useState('');

    const handleEnable2FA = async () => {
        try {
            const response = await axios.post('/api/security/enable-2fa');
            setSecret(response.data.secret);
            setError('');
        } catch (error) {
            console.error('Error enabling 2FA:', error);
            setError('Failed to enable 2FA. Please try again.');
        }
    };

    const handleVerify2FA = async () => {
        try {
            const response = await axios.post('/api/security/verify-2fa', { token });
            alert(response.data.message);
            setError('');
        } catch (error) {
            console.error('Error verifying 2FA:', error);
            setError('Failed to verify 2FA. Please check your token and try again.');
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Security Settings</h2>
            <button onClick={handleEnable2FA} className="bg-blue-500 text-white p-2 rounded mb-4">
                Enable 2FA
            </button>
            {secret && (
                <div className="mb-4">
                    <p className="font-bold">2FA Secret:</p>
                    <p>{secret}</p>
                </div>
            )}
            <input
                type="text"
                placeholder="2FA Token"
                value={token}
                onChange={(e) => setToken(e.target.value)}
                className="p-2 border rounded mb-4"
            />
            <button onClick={handleVerify2FA} className="bg-green-500 text-white p-2 rounded">
                Verify 2FA
            </button>
            {error && (
                <div className="text-red-500 mt-4">
                    {error}
                </div>
            )}
        </div>
    );
};

export default SecuritySettings;