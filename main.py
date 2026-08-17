from fastapi import FastAPI

from database import Base, engine
from models.medical_model import MedicalModel
from routers.medical_router import router as medical_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(medical_router)