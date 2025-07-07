import random
from datetime import datetime

RESPONSES = [
    "Interesting... Let's explore that idea.",
    "Let me think...",
    "Hmm, good question!",
    "That’s something worth pondering.",
    "Here’s a thought..."
]

HISTORY = {}  # username -> list of HistoryItem dicts

def generate_response() -> str:
    return random.choice(RESPONSES)

def store_history(user: str, prompt: str, response: str):
    item = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }
    HISTORY.setdefault(user, []).append(item)
