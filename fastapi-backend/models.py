from pydantic import BaseModel
from datetime import datetime

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

class HistoryItem(BaseModel):
    timestamp: str
    prompt: str
    response: str
