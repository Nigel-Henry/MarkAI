from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

ticket_routes = Blueprint('ticket_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@ticket_routes.route('/api/tickets', methods=['POST'])
@jwt_required()
def create_ticket():
    try:
        ticket_title = request.json.get('ticket_title')
        ticket_description = request.json.get('ticket_description')

        if not ticket_title or not ticket_description:
            return jsonify({"error": "Both title and description are required"}), 400

        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tickets (ticket_title, ticket_description) VALUES (?, ?)", 
                      (ticket_title, ticket_description))
            conn.commit()

        return jsonify({"message": "Ticket created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ticket_routes.route('/api/tickets', methods=['GET'])
@jwt_required()
def get_tickets():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tickets")
            tickets = c.fetchall()

        return jsonify({"tickets": [dict(ticket) for ticket in tickets]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500