from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from models.version_model import Version

version_routes = Blueprint('version_routes', __name__)

@version_routes.route('/api/versions', methods=['POST'])
@jwt_required()
def create_version():
    version_number = request.json.get('version_number')
    version = Version(version_number=version_number)
    db.session.add(version)
    db.session.commit()
    return jsonify({"message": "Version created successfully!"})

@version_routes.route('/api/versions', methods=['GET'])
@jwt_required()
def get_versions():
    versions = Version.query.all()
    return jsonify({"versions": [version.to_dict() for version in versions]})
