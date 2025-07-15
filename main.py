from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import Literal
import os

from vertex_predict import predict_from_vertex
from bq_logger import log_to_bigquery

app = FastAPI()

# Optional: Add token-based auth
API_SECRET_TOKEN = os.getenv("API_TOKEN")

def verify_token(authorization: str = Header(...)):
    expected = f"Bearer {API_SECRET_TOKEN}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="Unauthorized")
#this
# Input schema
class InputData(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/predict")
async def predict(data: InputData, authorized: None = Depends(verify_token)):
    try:
        instance = data.dict()
        prediction = predict_from_vertex(instance)
        log_to_bigquery(instance, prediction)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
