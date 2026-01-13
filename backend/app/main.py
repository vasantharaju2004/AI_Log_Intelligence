from fastapi import FastAPI
from app.api.logs import router as logs_router
from app.api.analyze import router as analyze_router

app = FastAPI(title="AI Log Intelligence")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(logs_router)
app.include_router(analyze_router)


# connecting  backend with frontend server >> npm (React+Vite)
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





