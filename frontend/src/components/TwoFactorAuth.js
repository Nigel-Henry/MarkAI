// frontend/src/components/TwoFactorAuth.js
import React, { useState } from 'react';
import { enable2FA, verify2FA } from '../services/api';

function TwoFactorAuth() {
    const [token, setToken] = useState('');

    // Function to handle enabling 2FA
    const handleEnable2FA = async () => {
        try {
            const response = await enable2FA();
            console.log('Enable 2FA Response:', response);
        } catch (error) {
            console.error('Enable 2FA Error:', error);
        }
    };

    // Function to handle verifying 2FA
    const handleVerify2FA = async () => {
        try {
            const response = await verify2FA(token);
            console.log('Verify 2FA Response:', response);
        } catch (error) {
            console.error('Verify 2FA Error:', error);
        }
    };

    return (
        <div>
            <h2>Two-Factor Authentication</h2>
            <button onClick={handleEnable2FA}>Enable 2FA</button>
            <input
                type="text"
                placeholder="2FA Token"
                value={token}
                onChange={(e) => setToken(e.target.value)}
            />
            <button onClick={handleVerify2FA}>Verify 2FA</button>
        </div>
    );
}

export default TwoFactorAuth;