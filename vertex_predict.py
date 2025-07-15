from google.cloud import aiplatform
import os

PROJECT = os.getenv("PROJECT_ID")
LOCATION = os.getenv("REGION")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")

def predict_from_vertex(instance: dict):
    aiplatform.init(project=PROJECT, location=LOCATION)
    endpoint = aiplatform.Endpoint(endpoint_name=ENDPOINT_ID)

    prediction = endpoint.predict(instances=[instance])
    return prediction.predictions[0]
