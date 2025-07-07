from fastapi import APIRouter, Depends
from models import PromptRequest, PromptResponse
from auth import get_current_user
from utils import generate_response, store_history

router = APIRouter()

@router.post("/prompt/", response_model=PromptResponse)
def submit_prompt(data: PromptRequest, user: str = Depends(get_current_user)):
    response = generate_response()
    store_history(user, data.prompt, response)
    return {"response": response}
