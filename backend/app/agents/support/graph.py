from langgraph.graph import END, START, StateGraph

from app.agents.support.nodes import classify, escalate, respond, route
from app.agents.support.state import State

builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("respond", respond)
builder.add_node("escalate", escalate)

builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route)
builder.add_edge("respond", END)
builder.add_edge("escalate", END)

graph = builder.compile()