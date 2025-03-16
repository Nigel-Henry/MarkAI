from datetime import datetime
from ..shared.database import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    plan = db.Column(db.String(50))
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    roles = db.Column(db.JSON)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    permissions = db.Column(db.JSON)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    credits = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)