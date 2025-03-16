import React, { useState } from 'react';
import axios from 'axios';

const APIKeyGenerator = () => {
    const [apiKey, setApiKey] = useState('');
    const [keyType, setKeyType] = useState('free');
    const [error, setError] = useState('');

    const handleGenerateKey = async () => {
        try {
            const response = await axios.post('/api/generate-key', { key_type: keyType });
            setApiKey(response.data.api_key);
            setError(''); // Clear any previous errors
        } catch (error) {
            console.error('Error generating API key:', error);
            setError('Failed to generate API key. Please try again.');
        }
    };

    return (
        <div className="mb-8">
            <h2 className="text-2xl font-bold mb-4">Generate API Key</h2>
            <select
                value={keyType}
                onChange={(e) => setKeyType(e.target.value)}
                className="p-2 border rounded mb-4"
            >
                <option value="free">Free</option>
                <option value="paid">Paid</option>
            </select>
            <button
                onClick={handleGenerateKey}
                className="bg-blue-500 text-white p-2 rounded"
            >
                Generate Key
            </button>
            {error && (
                <div className="mt-4 text-red-500">
                    <p>{error}</p>
                </div>
            )}
            {apiKey && (
                <div className="mt-4">
                    <p className="font-bold">Your API Key:</p>
                    <p className="bg-gray-100 p-2 rounded">{apiKey}</p>
                </div>
            )}
        </div>
    );
};

export default APIKeyGenerator;