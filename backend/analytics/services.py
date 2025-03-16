import pandas as pd
from ..shared.database import db

def get_usage_analytics(user_id):
    query = f"SELECT * FROM usage_logs WHERE user_id = {user_id}"
    df = pd.read_sql(query, db.engine)
    return df.describe().to_dict()