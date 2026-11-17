from langchain_core.tools import tool


ORDERS = {
    "1001": "Order 1001: shirt, size M, delivered.",
    "1002": "Order 1002: shoes, size 42, shipped.",
}

@tool
def get_order(order_id : str) -> str:
    """Look up and order by its id"""
    order = ORDERS.get(order_id)
    if order is None:
        return f"No order found for id {order_id}."
    return order