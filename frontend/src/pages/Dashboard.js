import React from 'react';
import Rewards from '../components/Rewards';

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-3xl font-bold mb-8">Dashboard</h1>   <div>
      <h1>Dashboard</h1>
    </div>
      <div className="grid grid-cols-2 gap-8">
        <Rewards />
      </div>
    </div>



import React from 'react';
import Chat from '../components/Chat';
import FileManager from '../components/FileManager';

function Dashboard() {
    return (
        <div>
            <h1>Dashboard</h1>
            <Chat />
            <FileManager />
        </div>
    );
}
  );
}; 




export default Dashboard;


