import React, { useState } from 'react';
import axios from 'axios';

const SupportTickets = () => {
    const [ticketMessage, setTicketMessage] = useState('');
    const [tickets, setTickets] = useState([]);
    const [error, setError] = useState(null);

    const handleCreateTicket = async () => {
        try {
            const response = await axios.post('/api/support/tickets', { ticket_message: ticketMessage });
            setTickets([...tickets, response.data]);
            setTicketMessage('');
            setError(null);
        } catch (error) {
            console.error('Error creating ticket:', error);
            setError('Failed to create ticket. Please try again.');
        }
    };

    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">Support Tickets</h2>
            {error && <p className="text-red-500 mb-4">{error}</p>}
            <textarea
                value={ticketMessage}
                onChange={(e) => setTicketMessage(e.target.value)}
                className="w-full p-2 border rounded mb-4"
                placeholder="Enter your ticket message..."
            />
            <button onClick={handleCreateTicket} className="bg-blue-500 text-white p-2 rounded">
                Create Ticket
            </button>
            <div className="mt-4">
                {tickets.map((ticket, index) => (
                    <div key={index} className="p-2 border-b">
                        <p>{ticket.ticket_message}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SupportTickets;