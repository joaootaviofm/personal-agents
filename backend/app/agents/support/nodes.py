from app.agents.support.state import State
from typing import Literal 
from app.agents.support.prompts import (CLASSIFY_PROMPT, RESPOND_PROMPT)
from app.integrations.openrouter import get_model
from app.agents.support.tools import get_order 

def classify(state: State) -> dict:
    response = get_model().invoke(CLASSIFY_PROMPT.format(message=state["message"]))
    intent = response.content.strip().lower()
    if intent not in {"refund", "exchange", "other"}:
        intent = "other"
    return { "intent" : intent }

def respond(state: State) -> dict:
    model = get_model().bind_tools([get_order])
    history = state.get("messages")
    if history:
        response = model.invoke(history)
    else:
        response = model.invoke(
            RESPOND_PROMPT.format(intent=state["intent"], message=state["message"])
        )
    update = {"messages" : [response]}
    if not response.tool_calls:
        update["reply"] = response.content.strip()
    return update


def escalate(state: State) -> dict:
    return {"reply": "A refund needs a person. I forwarded your case."}

# Route 
def route(state: State) -> Literal["respond", "escalate"]:
    if state["intent"] == "refund":
        return "escalate"
    return "respond"