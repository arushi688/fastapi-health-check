import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")

settings = Settings()