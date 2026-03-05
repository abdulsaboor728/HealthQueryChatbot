import re
from typing import Tuple

HEALTH_KEYWORDS = [
    # general health topics
    "symptom", "pain", "fever", "cough", "cold", "flu", "sore", "throat", "headache",
    "nausea", "vomit", "diarrhea", "constipation", "rash", "itch", "allergy",
    "blood pressure", "hypertension", "diabetes", "asthma", "cholesterol",
    "sleep", "insomnia", "diet", "nutrition", "exercise", "workout",
    "anxiety", "stress", "depression", "mental health",
    "medicine", "medication", "dose", "side effect", "antibiotic",
    "vitamin", "supplement", "hydration", "water",
    "injury", "sprain", "strain", "burn", "wound",
    "pregnancy", "period", "menstruation",
    "infection",
]

# red-flag / emergency signals -> do NOT answer, escalate
EMERGENCY_PATTERNS = [
    r"chest pain",
    r"trouble breathing|can't breathe|cannot breathe|shortness of breath",
    r"stroke|face droop|slurred speech|one side weak",
    r"seizure|fit",
    r"suicid(al|e)|kill myself|self harm",
    r"severe bleeding|bleeding won't stop",
    r"loss of consciousness|passed out|fainted",
    r"severe allergic|anaphylaxis|throat closing",
]

def is_emergency(text: str) -> bool:
    t = text.lower()
    return any(re.search(p, t) for p in EMERGENCY_PATTERNS)

def is_health_topic(text: str) -> bool:
    t = text.lower()
    # simple keyword gate (fast + decent for first version)
    return any(k in t for k in HEALTH_KEYWORDS)

def gate_message(user_text: str) -> Tuple[bool, str]:
    """
    Returns (allowed, reason_message).
    """
    if is_emergency(user_text):
        return (False,
                "I’m not able to help with urgent or emergency situations. "
                "If this might be an emergency, call your local emergency number or seek immediate medical care.")
    if not is_health_topic(user_text):
        return (False,
                "I can only answer general health-related questions. Please ask a health question (symptoms, wellness, medication info, etc.).")
    return (True, "")