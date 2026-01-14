🧠 AI Log Intelligence Platform

An AI-assisted log analysis and anomaly detection platform that ingests application logs, detects abnormal patterns using Machine Learning, and provides human-readable root cause explanations.

This project simulates how modern observability and AIOps platforms (such as Datadog, Splunk, or New Relic) help engineers diagnose production issues efficiently.

🚀 Key Highlights

Full-stack system (Backend + Frontend)

Machine Learning–based anomaly detection

AI-assisted explanation with safe fallback

Dockerized, production-style setup

Designed with reliability and extensibility in mind

📌 Features

📝 Manual log ingestion via UI or REST API

📦 Centralized log storage

🧠 Unsupervised anomaly detection on logs

🤖 AI-powered root cause explanation (with fallback)

🎨 Interactive dashboard with severity-based visualization

🕒 Timestamped logs with filtering

🐳 Fully containerized using Docker & Docker Compose

🧠 Technologies Used

Category	| Tools |
Programming Language | Python, JavaScript|
Backend Framework     |  FastAPI|
Frontend Framework | React (Vite)|
Machine Learning	|Scikit-learn (Isolation Forest)|
AI Integration |	OpenAI API (optional, with fallback)|
DevOps	Docker, Docker Compose
API Testing	Postman

🏗️ System Architecture

User / Frontend UI
        ↓
FastAPI Backend (Log Ingestion API)
        ↓
In-memory Log Storage
        ↓
ML Anomaly Detection (Isolation Forest)
        ↓
AI / Rule-based Root Cause Explanation
        ↓
Frontend Dashboard Visualization


📂 Project Structure

AI_Log_Intelligence/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes (logs, analyze)
│   │   ├── models/       # Pydantic schemas
│   │   └── services/     # ML & AI logic
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env (ignored)
│
├── frontend/
│   ├── src/
│   │   └── App.jsx       # Dashboard UI
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
└── README.md

🧪 How It Works

Logs are submitted via the frontend or API

Logs are validated and stored in backend memory

Machine Learning model analyzes log patterns

Anomalous logs are identified

AI or fallback logic generates explanations

Frontend displays logs, anomalies, and insights

⚠️ Limitations

Logs are stored in memory (no persistent database)

AI explanation depends on external API quota

Log ingestion is manual (auto ingestion can be added)

🔮 Future Enhancements

Persistent storage (PostgreSQL / MongoDB)

Automated backend log ingestion

Vector embeddings & retrieval-based explanations

Kubernetes-based deployment

Authentication & access control

▶️ Run Locally (Docker)

Prerequisites

Docker

Docker Compose

Steps
```bash
git clone https://github.com/vasantharaju2004/AI_Log_Intelligence.git
cd AI_Log_Intelligence
docker-compose up --build
```
Access

Frontend: http://localhost:5173

Backend API Docs: http://localhost:8000/docs

🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success)
![React](https://img.shields.io/badge/React-Frontend-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Status](https://img.shields.io/badge/Status-Active-success)




👤 Author

Vasanth Kandolu
B.Tech, National Institute of Technology Karnataka
Aspiring Software Engineer

🔗 GitHub: https://github.com/vasantharaju2004

📌 Notes

This project focuses on system design, reliability, and engineering trade-offs, rather than purely model accuracy.
It demonstrates how ML and AI can be integrated responsibly into production-style backend systems.
