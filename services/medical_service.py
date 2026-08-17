from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.medical_schema import MedicalRegisterRequest, MedicalLoginRequest
from models.medical_model import MedicalModel
from security.password import gen_hashed_password, verify_password
from security.gen_jwt import generate_access_token



def register(data: MedicalRegisterRequest, db: Session):
    existing_username = db.query(MedicalModel).filter(MedicalModel.username == data.username).first()
    
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tài khoản đã tồn tại"
        )
        
    new_staff = MedicalModel(
        username = data.username,
        hashed_password = gen_hashed_password(data.password),
        role = data.role
    )
    
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff

def login(data: MedicalLoginRequest, db: Session) -> dict:
    staff_db = db.query(MedicalModel).filter(MedicalModel.username == data.username).first()
    
    if staff_db is None or not verify_password(data.password, staff_db.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Thông tin đăng nhập không chính xáo"
        )
        
    return generate_access_token(staff_db.username, staff_db.role)
