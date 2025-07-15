from google.cloud import bigquery
import os
from datetime import datetime

BQ_TABLE = os.getenv("BQ_TABLE_ID")  # Format: project.dataset.table

client = bigquery.Client()

def log_to_bigquery(instance: dict, prediction: float):
    row = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": instance,
        "prediction": prediction
    }
    errors = client.insert_rows_json(BQ_TABLE, [row])
    if errors:
        raise RuntimeError(f"BigQuery insert failed: {errors}")
