from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

inventory_routes = Blueprint('inventory_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@inventory_routes.route('/api/inventory', methods=['POST'])
@jwt_required()
def create_inventory():
    item_name = request.json.get('item_name')
    item_quantity = request.json.get('item_quantity')

    if not item_name or not item_quantity:
        return jsonify({"error": "Item name and quantity are required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO inventory (item_name, item_quantity) VALUES (?, ?)", 
                      (item_name, item_quantity))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Inventory item created successfully!"}), 201

@inventory_routes.route('/api/inventory', methods=['GET'])
@jwt_required()
def get_inventory():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM inventory")
            inventory = c.fetchall()
            inventory_list = [dict(row) for row in inventory]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"inventory": inventory_list}), 200