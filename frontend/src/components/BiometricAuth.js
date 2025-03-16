import React, { useState } from 'react';
import { enrollBiometric, authenticateBiometric } from '../services/api';

function BiometricAuth() {
    const [username, setUsername] = useState('');
    const [faceData, setFaceData] = useState('');

    const handleEnroll = async () => {
        if (!username || !faceData) {
            alert('Please provide both username and face data.');
            return;
        }
        try {
            const response = await enrollBiometric(username, faceData);
            console.log('Enroll Response:', response);
        } catch (error) {
            console.error('Enroll Error:', error);
            alert('Failed to enroll. Please try again.');
        }
    };

    const handleAuthenticate = async () => {
        if (!username || !faceData) {
            alert('Please provide both username and face data.');
            return;
        }
        try {
            const response = await authenticateBiometric(username, faceData);
            console.log('Authenticate Response:', response);
        } catch (error) {
            console.error('Authenticate Error:', error);
            alert('Failed to authenticate. Please try again.');
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
        </div>
    );
}

export default BiometricAuth;