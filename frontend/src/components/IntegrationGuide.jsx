import React from 'react';

const IntegrationGuide = () => {
    return (
        <div className="mb-8">
            <h2 className="text-2xl font-bold mb-4">Integration Guide</h2>
            <p className="mb-4">
                To integrate with MarkAI, follow these steps:
            </p>
            <div className="bg-gray-100 p-4 rounded">
                <pre className="whitespace-pre-wrap">
{`1. Generate an API key.
2. Install the MarkAI SDK:
   npm install markai-sdk
3. Use the key in your application:
   const MarkAi = require('markai-sdk');
   const client = new MarkAi('YOUR_API_KEY');
   client.chat([{ role: 'user', content: 'Hello' }]);
4. Test your integration.`}
                </pre>
            </div>
        </div>
    );
};

export default IntegrationGuide;