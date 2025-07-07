from fastapi import HTTPException, Header, status
import uuid

USERS = {"alice": "password123", "bob": "secret"}
TOKENS = {}  # token -> username mapping

def authenticate_user(username: str, password: str) -> str:
    if USERS.get(username) == password:
        token = str(uuid.uuid4())
        TOKENS[token] = username
        return token
    raise HTTPException(status_code=401, detail="Invalid username or password")

def get_current_user(token: str = Header(..., alias="Authorization")) -> str:
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    raw_token = token.split(" ")[1]
    user = TOKENS.get(raw_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user
