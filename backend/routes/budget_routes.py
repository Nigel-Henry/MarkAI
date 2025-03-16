from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

budget_routes = Blueprint('budget_routes', __name__)

DATABASE = 'knowledge.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@budget_routes.route('/api/budgets', methods=['POST'])
@jwt_required()
def create_budget():
    data = request.get_json()
    budget_name = data.get('budget_name')
    budget_amount = data.get('budget_amount')

    if not budget_name or not budget_amount:
        return jsonify({"error": "Invalid input"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO budgets (budget_name, budget_amount) VALUES (?, ?)", 
                      (budget_name, budget_amount))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Budget created successfully!"}), 201

@budget_routes.route('/api/budgets', methods=['GET'])
@jwt_required()
def get_budgets():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM budgets")
            budgets = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"budgets": [dict(row) for row in budgets]}), 200