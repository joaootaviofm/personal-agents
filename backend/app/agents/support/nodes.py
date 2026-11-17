from app.agents.support.state import State
from typing import Literal 

def classify(state: State) -> dict:
    text = state["message"].lower()
    if any(word in text for word in ("refund", "money back", "chargeback")):
        intent = "refund"
    elif any(word in text for word in ("exchange", "size", "defect", "broken")):
        intent = "exchange"
    else:
        intent = "other"
    return {"intent": intent}

def respond(state: State) -> dict:
    return {"reply": f"I'll handle your {state['intent']} request."}

def escalate(state: State) -> dict:
    return {"reply": "A refund needs a person. I forwarded your case."}

# Route 
def route(state: State) -> Literal["respond", "escalate"]:
    if state["intent"] == "refund":
        return "escalate"
    return "respond"