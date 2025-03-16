import React, { useState } from 'react';
import axios from 'axios';

const SubscriptionPlans = () => {
    const [selectedPlan, setSelectedPlan] = useState('basic');

    const handleSubscribe = async () => {
        try {
            const response = await axios.post('/api/subscribe', { plan: selectedPlan });
            alert(response.data.message);
        } catch (error) {
            console.error('Error subscribing:', error);
            alert('Failed to subscribe. Please try again later.');
        }
    };

    return (
        <div className="mb-8">
            <h2 className="text-2xl font-bold mb-4">Subscription Plans</h2>
            <select
                value={selectedPlan}
                onChange={(e) => setSelectedPlan(e.target.value)}
                className="p-2 border rounded mb-4"
            >
                <option value="basic">Basic</option>
                <option value="pro">Pro</option>
                <option value="enterprise">Enterprise</option>
            </select>
            <button
                onClick={handleSubscribe}
                className="bg-blue-500 text-white p-2 rounded"
            >
                Subscribe
            </button>
        </div>
    );
};

export default SubscriptionPlans;