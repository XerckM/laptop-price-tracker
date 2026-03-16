from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.core.database import engine
from app.models import Base

app = FastAPI(title="Laptop Price Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(health_router)
app.include_router(products_router)


@app.get("/")
def root():
    return {"message": "Laptop Price Tracker API is running"}
