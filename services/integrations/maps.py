import os
from pathlib import Path

import requests
from dotenv import load_dotenv

SERVICES_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=SERVICES_ROOT / ".env")

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "YOUR_GOOGLE_MAPS_API_KEY")


def get_routes(origin, destination):
    url = (
        "https://maps.googleapis.com/maps/api/directions/json"
        f"?origin={origin}&destination={destination}&alternatives=true&key={API_KEY}"
    )

    response = requests.get(url, timeout=30)
    data = response.json()
    return data.get("routes", [])
