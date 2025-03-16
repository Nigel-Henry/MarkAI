// frontend/src/components/BiometricAuth.js
import React, { useState } from 'react';
import { enrollBiometric, authenticateBiometric } from '../services/api';

function BiometricAuth() {
    const [username, setUsername] = useState('');
    const [faceData, setFaceData] = useState('');
    const [error, setError] = useState(null);
    const [message, setMessage] = useState(null);

    // Handle biometric enrollment
    const handleEnroll = async () => {
        try {
            const response = await enrollBiometric(username, faceData);
            setMessage('Enrollment successful');
            console.log('Enroll Response:', response);
        } catch (error) {
            setError('Enrollment failed');
            console.error('Enroll Error:', error);
        }
    };

    // Handle biometric authentication
    const handleAuthenticate = async () => {
        try {
            const response = await authenticateBiometric(username, faceData);
            setMessage('Authentication successful');
            console.log('Authenticate Response:', response);
        } catch (error) {
            setError('Authentication failed');
            console.error('Authenticate Error:', error);
        }
    };

    return (
        <div>
            <h2>Biometric Authentication</h2>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                type="text"
                placeholder="Face Data (Base64)"
                value={faceData}
                onChange={(e) => setFaceData(e.target.value)}
            />
            <button onClick={handleEnroll}>Enroll</button>
            <button onClick={handleAuthenticate}>Authenticate</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {message && <p style={{ color: 'green' }}>{message}</p>}
        </div>
    );
}

export default BiometricAuth;