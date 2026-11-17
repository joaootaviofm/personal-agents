from fastapi import FastAPI 
from app.routers.support import router as support_router

app = FastAPI()

app.include_router(support_router)