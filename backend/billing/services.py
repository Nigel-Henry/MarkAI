from .models import Billing
from ..database import SessionLocal

def create_billing_record(user_id, amount, currency):
    db = SessionLocal()
    new_billing = Billing(user_id=user_id, amount=amount, currency=currency)
    db.add(new_billing)
    db.commit()
    db.close()

def get_billing_records(user_id):
    db = SessionLocal()
    billings = db.query(Billing).filter(Billing.user_id == user_id).all()
    db.close()
    return billings