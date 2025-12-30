from fastapi import FastAPI
from app.schemas import AgentRequest, AgentResponse
from app.agent import run_agent

app = FastAPI(title="Agentic AI Coach API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Agentic AI Coach API is running. Visit /docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/agent", response_model=AgentResponse)
def agent(req: AgentRequest):
    intent, plan, final_answer = run_agent(req.task, req.context)
    return AgentResponse(
        intent=intent,
        plan=plan,
        final_answer=final_answer
    )
