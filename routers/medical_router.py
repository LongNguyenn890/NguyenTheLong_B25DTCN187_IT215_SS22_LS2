from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.medical_schema import MedicalRegisterRequest, MedicalResponse, TokenResponse, MedicalLoginRequest
import services.medical_service as medical_services


router = APIRouter(
    prefix="/api/v1",
    tags=["Medicals"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=TokenResponse)
def register(data: MedicalRegisterRequest, db: Session = Depends(get_db)):
    return medical_services.register(data, db)

@router.post("/login", response_model=TokenResponse)
def login(data: MedicalLoginRequest, db: Session = Depends(get_db)):
    access_token = medical_services.login(data, db)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
    

    
    