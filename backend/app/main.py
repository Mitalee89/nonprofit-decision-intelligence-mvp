from fastapi import FastAPI

from app.core.database import create_db_and_tables

from app.api.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(health_router)