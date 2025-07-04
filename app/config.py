import os
from pathlib import Path

from dotenv import load_dotenv


dotenv_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path)

class Config:
    BOT_API = os.getenv("BOT_API")