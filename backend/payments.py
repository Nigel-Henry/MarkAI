from flask import Blueprint, request, jsonify
import stripe
import os
from config import Config  # Ensure Config is imported from the correct module

bp = Blueprint('payments', __name__)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', Config.STRIPE_SECRET_KEY)

@bp.route('/api/subscribe', methods=['POST'])
def create_subscription():
    try:
        data = request.json
        if not data or 'email' not in data:
            return jsonify({'error': 'Email is required'}), 400

        customer = stripe.Customer.create(email=data['email'])
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'price': 'price_free_tier'}],  # Free tier
        )
        return jsonify(subscription)
    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500