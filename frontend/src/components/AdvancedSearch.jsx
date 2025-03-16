import React, { useState } from 'react';
import axios from 'axios';

const AdvancedSearch = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

    const handleSearch = async () => {
        try {
            const response = await axios.get('/api/search', { params: { q: query } });
            setResults(response.data.results);
            setError(null); // Clear any previous errors
        } catch (error) {
            console.error('Error searching:', error);
            setError('An error occurred while searching. Please try again.');
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Advanced Search</h2>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="w-full p-2 border rounded mb-4"
                placeholder="Search..."
            />
            <button
                onClick={handleSearch}
                className="bg-blue-500 text-white p-2 rounded"
            >
                Search
            </button>
            {error && <div className="text-red-500 mt-2">{error}</div>}
            <div className="mt-4">
                {results.map((result, index) => (
                    <div key={index} className="p-2 border-b">
                        {result}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AdvancedSearch;