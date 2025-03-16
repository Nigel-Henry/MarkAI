import React from 'react';
import IntegrationGuide from '../components/IntegrationGuide';
import SubscriptionPlans from '../components/SubscriptionPlans';

const DevelopersPage = () => {
    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-8">Developers</h1>
            <IntegrationGuide />
            <SubscriptionPlans />
        </div>
    );
};

export default DevelopersPage;