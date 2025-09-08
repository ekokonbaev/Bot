import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    SUPABASE_URL: str = os.getenv('SUPABASE_URL')
    SUPABASE_KEY: str = os.getenv('SUPABASE_KEY')
    # ADMIN_ID может отсутствовать в окружении во время разработки
    ADMIN_ID: int | None = (lambda v: int(v) if v and v.isdigit() else None)(os.getenv('ADMIN_ID'))
    ADMIN_PIN: str = os.getenv('ADMIN_PIN', '')

    def __post_init__(self):
        if not self.BOT_TOKEN:
            raise ValueError("❌ BOT_TOKEN не задан в переменных окружения! Проверьте файл .env")
        if not self.SUPABASE_URL:
            print("⚠️ SUPABASE_URL не задан - будет использоваться in-memory хранилище")
        if not self.SUPABASE_KEY:
            print("⚠️ SUPABASE_KEY не задан - будет использоваться in-memory хранилище")

config = Config()