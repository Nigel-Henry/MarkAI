from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import stripe
import os

payment_routes = Blueprint('payment_routes', __name__)

# Load Stripe API key from environment variable
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@payment_routes.route('/api/create-payment-intent', methods=['POST'])
@jwt_required()
def create_payment_intent():
    try:
        amount = request.json.get('amount')
        if not amount:
            return jsonify({"error": "Amount is required"}), 400

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
        )

        return jsonify({"client_secret": intent.client_secret})
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500