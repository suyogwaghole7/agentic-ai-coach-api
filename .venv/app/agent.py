from typing import List, Optional

def classify_intent(task: str) -> str:
    t = task.lower()
    if any(k in t for k in ["deploy", "render", "fastapi", "api", "github"]):
        return "Software engineering / deployment"
    if any(k in t for k in ["model", "ml", "accuracy", "f1", "precision", "recall"]):
        return "Machine learning / evaluation"
    if any(k in t for k in ["health", "clinical", "spirometry", "pft", "patient"]):
        return "Healthcare / clinical reasoning"
    return "General problem solving"

def make_plan(intent: str) -> List[str]:
    if intent == "Software engineering / deployment":
        return [
            "Create the FastAPI endpoint and test locally",
            "Freeze dependencies into requirements.txt",
            "Deploy to Render with correct start command",
            "Test live endpoint (/docs) and capture screenshots",
            "Document steps in README for reproducibility",
        ]
    if intent == "Machine learning / evaluation":
        return [
            "Define target and features",
            "Split data into train/test",
            "Train a baseline model",
            "Evaluate with suitable metrics",
            "Iterate and re-evaluate",
        ]
    if intent == "Healthcare / clinical reasoning":
        return [
            "Identify clinical question and context",
            "List key parameters and red flags",
            "Interpret findings logically",
            "Suggest next steps and escalation criteria",
            "Summarize actionable recommendation",
        ]
    return [
        "Clarify the goal and constraints",
        "Break the task into steps",
        "Solve step-by-step",
        "Validate the result",
        "Suggest next actions",
    ]

def generate_answer(task: str, plan: List[str], context: Optional[str]) -> str:
    lines = [f"You asked: {task.strip()}"]
    if context:
        lines.append(f"Context: {context.strip()}")
    lines.append("\nPlanned steps:")
    for i, step in enumerate(plan, 1):
        lines.append(f"{i}. {step}")
    lines.append("\nIf you share your constraints, I can tailor this into an exact checklist.")
    return "\n".join(lines)

def run_agent(task: str, context: Optional[str] = None):
    intent = classify_intent(task)
    plan = make_plan(intent)
    final_answer = generate_answer(task, plan, context)
    return intent, plan, final_answer
