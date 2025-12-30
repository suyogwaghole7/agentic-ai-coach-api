# Agentic AI Coach API (FastAPI)

An agentic AI application that:
1. Classifies a user task (intent)
2. Creates a step-by-step plan
3. Returns a structured response via an API

This project was built as part of the **Digital Product School – AI Engineering Challenge (Option 1)**.


## Features

- FastAPI backend with Swagger UI
- Agent-style reasoning (intent → plan → final answer)
- REST API endpoints
- Production-ready deployment on Render

### API Endpoints
- `GET /` – Root endpoint
- `GET /health` – Health check
- `POST /agent` – Agentic task processing
- `GET /docs` – Swagger UI


## Project Structure

agentic-ai-coach-api/
├── app/
│ ├── main.py
│ ├── agent.py
│ └── schemas.py
├── requirements.txt
├── README.md
└── .gitignore


## Run Locally (Windows)


### 1. Clone the repository

git clone https://github.com/suyogwaghole7/agentic-ai-coach-api.git
cd agentic-ai-coach-api

2. Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the FastAPI application
uvicorn app.main:app --reload

5. Open Swagger UI
Open the following URL in your browser:
http://127.0.0.1:8000/docs
Example API Usage
POST /agent
Request Body
{
  "task": "Create a study plan for learning FastAPI",
  "context": "Beginner, 2 weeks"
}
Response

{
  "intent": "Learning plan creation",
  "plan": [
    "Understand FastAPI basics",
    "Build simple endpoints",
    "Practice with Swagger UI"
  ],
  "final_answer": "Here is a structured learning plan for FastAPI..."
}
Health Check
GET /health
{
  "status": "ok"
}

## Production Deployment
The application is deployed using Render.

Live API URL:
https://agentic-ai-coach-api.onrender.com

Available routes
/ – API status message

/health – Health check

/agent – Agent execution

/docs – Swagger UI

### Notes
The virtual environment (.venv) is excluded from version control using .gitignore

All required files to run and deploy the application are included in this repository

The application can be run locally or accessed via the deployed production URL

