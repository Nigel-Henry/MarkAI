import React, { useState } from 'react';
import axios from 'axios';

const UserRating = () => {
    const [rating, setRating] = useState(0);

    const handleRating = async (value) => {
        try {
            await axios.post('/api/rating', { rating: value });
            setRating(value);
        } catch (error) {
            console.error('Error submitting rating:', error);
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Rate Us</h2>
            <div className="flex">
                {[1, 2, 3, 4, 5].map((value) => (
                    <button
                        key={value}
                        onClick={() => handleRating(value)}
                        className={`p-2 ${rating >= value ? 'text-yellow-500' : 'text-gray-300'}`}
                    >
                        ★
                    </button>
                ))}
            </div>
        </div>
    );
};

export default UserRating;