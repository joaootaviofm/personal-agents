from app.agents.support.graph import graph 

def send_support_message(message : str) -> str:
    result = graph.invoke({"message" : message, "intent" : "", "reply": ""})
    return result["reply"]