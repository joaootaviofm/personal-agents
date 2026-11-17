from fastapi import APIRouter

from app.schemas.support import SupportMessageRequest, SupportReplyResponse
from app.services.support import send_support_message 

router = APIRouter(prefix="/support", tags=["support"])

@router.post("/messages", response_model=SupportReplyResponse)
def send_message(body : SupportMessageRequest) -> SupportReplyResponse:
    reply = send_support_message(body.message)
    return SupportReplyResponse(reply=reply)