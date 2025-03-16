import React, { useState } from 'react';
import APIKeyGenerator from '../components/APIKeyGenerator';
import IntegrationGuide from '../components/IntegrationGuide';

const IntegrationsPage = () => {
    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-8">Integrations</h1>
            <APIKeyGenerator />
            <IntegrationGuide />
        </div>
    );
};

export default IntegrationsPage;