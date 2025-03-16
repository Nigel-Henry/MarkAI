from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

customer_routes = Blueprint('customer_routes', __name__)

@customer_routes.route('/api/customers', methods=['POST'])
@jwt_required()
def create_customer():
    customer_name = request.json.get('customer_name')
    customer_email = request.json.get('customer_email')
    
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers (customer_name, customer_email) VALUES (?, ?)", 
              (customer_name, customer_email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Customer created successfully!"})

@customer_routes.route('/api/customers', methods=['GET'])
@jwt_required()
def get_customers():
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()

    return jsonify({"customers": customers})