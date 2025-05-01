from dataclasses import dataclass
from datetime import datetime

@dataclass
class ChatLog:
    sender: str
    message: str
    response: str
    timestamp: datetime = datetime.now()
