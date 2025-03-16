from datetime import datetime, timedelta

class PaymentService:
    @staticmethod
    def create_subscription(user_id, plan):
        return {
            "user_id": user_id,
            "plan": plan,
            "expires_at": datetime.now() + timedelta(days=30),
            "status": "active"
        }