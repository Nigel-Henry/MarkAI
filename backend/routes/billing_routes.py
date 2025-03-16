from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

billing_routes = Blueprint('billing_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@billing_routes.route('/api/billing', methods=['POST'])
@jwt_required()
def create_billing():
    billing_amount = request.json.get('billing_amount')
    user_id = request.json.get('user_id')
    
    if not billing_amount or not user_id:
        return jsonify({"error": "Missing billing_amount or user_id"}), 400

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO billing (billing_amount, user_id) VALUES (?, ?)", 
              (billing_amount, user_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Billing created successfully!"}), 201

@billing_routes.route('/api/billing', methods=['GET'])
@jwt_required()
def get_billing():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM billing")
    billing = c.fetchall()
    conn.close()

    return jsonify({"billing": [dict(row) for row in billing]}), 200