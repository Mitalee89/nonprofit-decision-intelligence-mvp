from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api.routes import campaigns
from app.api.routes import health
from app.api.routes import funds
from app.api.routes import donors
from app.api.routes import donations
from app.api.routes import grants


app = FastAPI(
    title="Non-Profit Decision Intelligence MVP",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(health.router)
app.include_router(campaigns.router)
app.include_router(funds.router)
app.include_router(donors.router)
app.include_router(donations.router)
app.include_router(grants.router)