import React, { useState } from 'react';
import axios from 'axios';

const MarketingCampaigns = () => {
    const [campaignName, setCampaignName] = useState('');
    const [campaigns, setCampaigns] = useState([]);
    const [error, setError] = useState(null);

    const handleCreateCampaign = async () => {
        try {
            const response = await axios.post('/api/marketing/campaigns', { campaign_name: campaignName });
            setCampaigns([...campaigns, response.data]);
            setCampaignName('');
            setError(null);
        } catch (error) {
            setError('Error creating campaign. Please try again.');
            console.error('Error creating campaign:', error);
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Marketing Campaigns</h2>
            <input
                type="text"
                value={campaignName}
                onChange={(e) => setCampaignName(e.target.value)}
                className="w-full p-2 border rounded mb-4"
                placeholder="Enter campaign name..."
            />
            <button onClick={handleCreateCampaign} className="bg-blue-500 text-white p-2 rounded">
                Create Campaign
            </button>
            {error && <p className="text-red-500 mt-2">{error}</p>}
            <div className="mt-4">
                {campaigns.map((campaign, index) => (
                    <div key={index} className="p-2 border-b">
                        <p>{campaign.campaign_name}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MarketingCampaigns;