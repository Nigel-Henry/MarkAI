from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

subscription_routes = Blueprint('subscription_routes', __name__)

@subscription_routes.route('/api/subscribe', methods=['POST'])
@jwt_required()
def subscribe():
    user_id = get_jwt_identity()
    plan = request.json.get('plan')  # 'basic', 'pro', 'enterprise'
    
    if plan not in ['basic', 'pro', 'enterprise']:
        return jsonify({"error": "Invalid plan selected"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO subscriptions (user_id, plan) VALUES (?, ?)", 
                      (user_id, plan))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": f"Subscribed to {plan} plan successfully!"})