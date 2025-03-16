from flask import Blueprint, request, jsonify
from .services import create_invoice, process_payment

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/invoices', methods=['POST'])
def create_invoice_route():
    data = request.json
    invoice = create_invoice(data)
    return jsonify(invoice), 201

@billing_bp.route('/payments', methods=['POST'])
def process_payment_route():
    data = request.json
    result = process_payment(data)
    return jsonify(result), 200