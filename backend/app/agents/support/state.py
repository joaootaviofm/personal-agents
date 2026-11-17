from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    message : str
    intent : str
    reply : str
    messages : Annotated[list, add_messages]