from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from guardrails import gate_message
from prompts import SYSTEM_PROMPT
from llama_client import LlamaClient

app = FastAPI()

# allow local static frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = LlamaClient(
    base_url="http://localhost:11434",
    model="llama3.2:3b"
)

class ChatReq(BaseModel):
    message: str

class ChatRes(BaseModel):
    allowed: bool
    reply: str

@app.post("/chat", response_model=ChatRes)
def chat(req: ChatReq):
    allowed, reason = gate_message(req.message)
    if not allowed:
        return ChatRes(allowed=False, reply=reason)

    # health question allowed -> ask model with strict prompt
    reply = client.chat(SYSTEM_PROMPT, req.message)

    # final safety: if model drifts into non-health, we still refuse
    # (lightweight check)
    allowed2, reason2 = gate_message(req.message)
    if not allowed2:
        return ChatRes(allowed=False, reply=reason2)

    return ChatRes(allowed=True, reply=reply)