from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import os

communication_routes = Blueprint('communication_routes', __name__)

@communication_routes.route('/api/send_email', methods=['POST'])
@jwt_required()
def send_email():
    email = request.json.get('email')
    message = request.json.get('message')
    if not email or not message:
        return jsonify({"error": "Email and message are required"}), 400

    msg = MIMEText(message)
    msg['Subject'] = 'Verification Code'
    msg['From'] = os.getenv('EMAIL_FROM', 'marklasfar@gmail.com')
    msg['To'] = email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_FROM', 'marklasfar@gmail.com'), os.getenv('EMAIL_PASSWORD'))
            server.sendmail(os.getenv('EMAIL_FROM', 'marklasfar@gmail.com'), email, msg.as_string())
        return jsonify({"message": "Email sent!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@communication_routes.route('/api/send-sms', methods=['POST'])
@jwt_required()
def send_sms():
    phone_number = request.json.get('phone_number')
    message = request.json.get('message')
    if not phone_number or not message:
        return jsonify({"error": "Phone number and message are required"}), 400

    try:
        client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        client.messages.create(
            body=message,
            from_=os.getenv('TWILIO_PHONE_NUMBER', '+01000071403'),
            to=phone_number
        )
        return jsonify({"message": "SMS sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
