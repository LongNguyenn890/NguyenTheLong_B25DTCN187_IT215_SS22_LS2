from sqlalchemy import Column, String, Integer

from database import Base

class MedicalModel(Base):
    __tablename__ = "medicals"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)