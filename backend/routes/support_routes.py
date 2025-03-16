from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

support_routes = Blueprint('support_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@support_routes.route('/api/support/tickets', methods=['POST'])
@jwt_required()
def create_ticket():
    ticket_message = request.json.get('ticket_message')
    if not ticket_message:
        return jsonify({"error": "Ticket message is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tickets (ticket_message) VALUES (?)", (ticket_message,))
            conn.commit()
        return jsonify({"message": "Ticket created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@support_routes.route('/api/support/tickets', methods=['GET'])
@jwt_required()
def get_tickets():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tickets")
            tickets = c.fetchall()
        return jsonify({"tickets": [dict(ticket) for ticket in tickets]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500