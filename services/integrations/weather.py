import os
from pathlib import Path

import requests
from dotenv import load_dotenv

SERVICES_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=SERVICES_ROOT / ".env")

API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_WEATHER_API_KEY")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url, timeout=30)
    return response.json()
