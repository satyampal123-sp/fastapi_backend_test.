from fastapi import APIRouter, Depends
from auth import get_current_user
from utils import HISTORY
from models import HistoryItem

router = APIRouter()

@router.get("/history/", response_model=list[HistoryItem])
def get_history(user: str = Depends(get_current_user)):
    return HISTORY.get(user, [])
