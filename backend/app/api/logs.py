from fastapi import APIRouter
from app.models.schemas import LogEntry

router = APIRouter()

LOG_STORAGE = []

@router.post("/logs")
def ingest_log(log:LogEntry):
    LOG_STORAGE.append(log)
    return {
        "status":"success",
        "message":"Log received",
        "total_logs": len(LOG_STORAGE),
        "logs":[log for log in LOG_STORAGE]
    }

@router.get("/logs")
def get_logs():
    return {
        "total_logs": len(LOG_STORAGE),
        "logs": [log.dict() for log in LOG_STORAGE]
    }
