from google.cloud import bigquery
from datetime import datetime
import os
import json

BQ_TABLE = os.getenv("BQ_TABLE_ID")  # Format: project.dataset.table
client = bigquery.Client()

def log_to_bigquery(instance: dict, prediction: float):
    try:
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": json.dumps(instance),  # ✅ Convert to JSON string
            "prediction": prediction
        }
        print("📤 Logging to BigQuery:", row)
        errors = client.insert_rows_json(BQ_TABLE, [row])
        if errors:
            print("❌ BigQuery insert error:", errors)
    except Exception as e:
        print("🔥 Exception in BigQuery logging:", str(e))
