from pydantic import BaseModel, ConfigDict
from typing import Literal

class MedicalRegisterRequest(BaseModel):
    username: str
    password: str
    role: Literal["doctor", "pharmacist"]
    

class MedicalLoginRequest(BaseModel):
    username: str
    password: str
    
    
class MedicalResponse(BaseModel):
    id: int
    username: str
    role: str
    
    model_config = ConfigDict(from_attributes=True)
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str