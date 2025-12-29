# Agentic AI Coach API (FastAPI)

A simple agentic application that:
1) classifies the user task (intent),
2) creates a step-by-step plan,
3) returns a structured answer via an API.

## Features
- FastAPI server with Swagger UI at `/docs`
- `GET /health` health check
- `POST /agent` returns `intent`, `plan`, `final_answer`

## Run locally (Windows)

### 1) Create and activate venv
```bat
py -m venv .venv
.venv\Scripts\activate
