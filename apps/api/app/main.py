from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.database import engine
from app.models import Base

app = FastAPI(title="Laptop Price Tracker API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Laptop Price Tracker API is running"}
