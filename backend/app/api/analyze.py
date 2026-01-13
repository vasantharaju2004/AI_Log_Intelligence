from fastapi import APIRouter
from app.api.logs import LOG_STORAGE
from app.services.anomaly_detector import LogAnomalyDetector
from app.services.llm_service import LLMService

# api for log analyzing with ML logic
router = APIRouter()

#  through ML Isolation forest in logs it detect anomaly logs
detector = LogAnomalyDetector()

# through OpenAI chatgpt explains the anomaly log in plain english.
llm = LLMService()

@router.post("/analyze")
def analyze_logs():
    if len(LOG_STORAGE) < 3:
        return {
            "status":"error",
            "message":"Not enough logs to analyze"
        }
    
    messages = [log.message for log in LOG_STORAGE]
    
    
    detector.train(messages)
    predictions = detector.detect(messages)

    results = []
    anomaly_messages = []

    for log , pred in zip(LOG_STORAGE, predictions):
        is_anomaly = True if pred ==-1 else False


        results.append({
            "message": log.message,
            "level":log.level,
            "anomaly": is_anomaly
        })

        if is_anomaly:
            anomaly_messages.append(log.message)
    
    explaination = None
    if anomaly_messages:
        explaination = llm.explain_incident(anomaly_messages)
    
    return {
        "total_logs": len(results),
        "anomalies_detected": sum(1 for r in results if r["anomaly"]),
        "results": results,
        "root_cause_analysis": explaination
    }