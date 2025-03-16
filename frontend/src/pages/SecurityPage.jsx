import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SecurityPage = () => {
    const [logs, setLogs] = useState([]);
    const [security, setSecurity] = useState({});

    useEffect(() => {
        const fetchLogs = async () => {
            try {
                const response = await axios.get('/api/security/logs');
                setLogs(response.data.logs);
            } catch (error) {
                console.error('Error fetching security logs:', error);
            }
        };
        fetchLogs();

        const fetchSecurity = async () => {
            try {
                const response = await axios.get('/api/security/check');
                setSecurity(response.data);
            } catch (error) {
                console.error('Error fetching security:', error);
            }
        };
        fetchSecurity();


    }, []);


    


    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-8">Security Logs</h1>
            <ul>
                {logs.map((log, index) => (
                    <li key={index} className="bg-white p-4 rounded-lg shadow mb-4">
                        <p>{log}</p>
                    </li>
                ))}
            </ul>
        </div>


        <div className="p-8">
        <h1 className="text-3xl font-bold mb-8">Security</h1>
        <div className="bg-white p-4 rounded-lg shadow">
            <h2 className="text-xl font-bold">Security Threats</h2>
            <p>{security.threats}</p>
        </div>
    </div>




    );
};

export default SecurityPage;



