from dotenv import load_dotenv
import os


class ENV:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), "../..", ".env")
        if os.path.exists(dotenv_path):
            load_dotenv()

        self.FASTAPI_KEY = os.getenv("FASTAPI_KEY")
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")



env = ENV()