from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

campaign_routes = Blueprint('campaign_routes', __name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@campaign_routes.route('/api/campaigns', methods=['POST'])
@jwt_required()
def create_campaign():
    campaign_name = request.json.get('campaign_name')
    if not campaign_name:
        return jsonify({"error": "Campaign name is required"}), 400

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO campaigns (campaign_name) VALUES (?)", (campaign_name,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Campaign created successfully!"})

@campaign_routes.route('/api/campaigns', methods=['GET'])
@jwt_required()
def get_campaigns():
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM campaigns")
            campaigns = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"campaigns": campaigns})