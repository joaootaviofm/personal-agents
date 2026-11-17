from langgraph.graph import END, START, StateGraph

from app.agents.support.nodes import classify, escalate, respond, route
from app.agents.support.state import State

from langgraph.prebuilt import ToolNode, tools_condition
from app.agents.support.tools import get_order

builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("respond", respond)
builder.add_node("escalate", escalate)
builder.add_node("tools", ToolNode([get_order]))

builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route)
builder.add_conditional_edges("respond", tools_condition)
builder.add_edge("escalate", END)

graph = builder.compile()