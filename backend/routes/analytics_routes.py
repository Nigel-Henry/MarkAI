from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

analytics_routes = Blueprint('analytics_routes', __name__)

@analytics_routes.route('/api/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM users")
    users_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM tasks")
    tasks_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM tickets")
    tickets_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM users WHERE last_login > datetime('now', '-7 days')")
    active_users = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM requests")
    total_requests = c.fetchone()[0]
    
    conn.close()

    return jsonify({
        "users_count": users_count,
        "tasks_count": tasks_count,
        "tickets_count": tickets_count,
        "active_users": active_users,
        "total_requests": total_requests
    })
