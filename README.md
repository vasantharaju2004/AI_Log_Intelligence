# AI Log Intelligence Platform

An AI-powered full-stack log analysis system that ingests application logs, detects anomalies using machine learning, and provides root-cause explanations through an intelligent analysis layer.

This project simulates how modern observability and AIOps platforms (like Datadog or Splunk) analyze logs to help engineers debug incidents faster.

---

## 🚀 Features

- Manual log ingestion via UI or API
- Centralized log storage
- Anomaly detection using Machine Learning
- AI-powered root cause analysis with safe fallback
- Interactive React dashboard
- Fully containerized using Docker & Docker Compose

---

## 🏗️ Architecture Overview

Frontend (React + Tailwind)
↓
Backend API (FastAPI)
↓
Log Storage (In-memory)
↓
ML Anomaly Detection
↓
LLM / Rule-based Explanation



---

## 🧰 Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn (Isolation Forest)
- Pydantic
- Uvicorn

### Frontend
- React (Vite)
- Tailwind CSS

### DevOps
- Docker
- Docker Compose

---

## 📂 Project Structure

ai_log_intelligence/
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── models/
│ │ └── services/
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ ├── Dockerfile
│ └── package.json
│
├── docker-compose.yml
└── README.md



---

## ▶️ How to Run (Docker)

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
git clone https://github.com/<your-username>/ai-log-intelligence.git
cd ai-log-intelligence
docker-compose up --build
Access
Frontend: http://localhost:5173

Backend API Docs: http://localhost:8000/docs


🧪 How It Works
User submits logs via UI or API

Logs are stored in backend memory

Machine learning model detects anomalies

AI or fallback logic generates explanations

Frontend displays logs, anomalies, and analysis

⚠️ Limitations
Logs are stored in-memory (no database)

AI explanation depends on API quota

Manual log ingestion (auto ingestion can be added)

🔮 Future Improvements
Persistent storage (PostgreSQL / MongoDB)

Automated log ingestion middleware

Vector embeddings + RAG

Kubernetes deployment

Authentication & RBAC

👨‍💻 Author
Vasanth Kandolu
B.Tech Civil Engineering, NITK
Aspiring Software / Platform Engineer
