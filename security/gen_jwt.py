from datetime import datetime, timezone, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


def generate_access_token(username: str, role: str):
    now = datetime.now(timezone.utc)
    expire_time = now + timedelta(minutes=20)
    payload = {
        "sub": username,
        "role": role,
        "iat": now.timestamp(),
        "exp": expire_time
    }
    
    return jwt.encode(payload, SECRET_KEY, "HS256")

def decode_jwt(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])