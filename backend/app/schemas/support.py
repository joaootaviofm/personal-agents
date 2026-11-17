from pydantic import BaseModel 

class SupportMessageRequest(BaseModel):
    message : str

class SupportReplyResponse(BaseModel):
    reply : str 