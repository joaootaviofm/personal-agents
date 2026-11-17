# ---- CLASSIFY PROMPT ----
CLASSIFY_PROMPT = """Classify this customer support message.
Reply with exactly one word: refund, exchange, or other.

Message:
{message}
"""

# ---- RESPOND PROMPT ----
RESPOND_PROMPT = """You are a support agent. Write a short reply to the customer.
Do not promise a refund. A refund is handled by a person.
The intent is already decided: {intent}

Customer message:
{message}
"""