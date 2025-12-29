from pydantic import BaseModel, Field
from typing import List, Optional


class AgentRequest(BaseModel):
    task: str = Field(..., min_length=3)
    context: Optional[str] = None


class AgentResponse(BaseModel):
    intent: str
    plan: List[str]
    final_answer: str
