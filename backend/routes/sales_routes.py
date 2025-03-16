from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

sales_routes = Blueprint('sales_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@sales_routes.route('/api/sales', methods=['POST'])
@jwt_required()
def create_sale():
    try:
        sale_amount = request.json.get('sale_amount')
        sale_date = request.json.get('sale_date')

        if not sale_amount or not sale_date:
            return jsonify({"error": "Missing sale_amount or sale_date"}), 400

        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO sales (sale_amount, sale_date) VALUES (?, ?)", 
                      (sale_amount, sale_date))
            conn.commit()

        return jsonify({"message": "Sale created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sales_routes.route('/api/sales', methods=['GET'])
@jwt_required()
def get_sales():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM sales")
            sales = c.fetchall()

        sales_list = [dict(row) for row in sales]
        return jsonify({"sales": sales_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500