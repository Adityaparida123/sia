from fastapi import FastAPI
from ml.demand.demand_model import predict_demand
from ml.delay.delay_model import predict_delay
from llm.chatbot import ask_chatbot
from llm.insights import generate_insight
from integrations.maps import get_routes
from integrations.weather import get_weather

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Service API Running"}


@app.get("/predict-demand")
def demand():
    return predict_demand()


@app.post("/predict-delay")
def delay(distance: int, traffic: int, weather: int):
    return predict_delay(distance, traffic, weather)


@app.post("/chat")
def chat(prompt: str):
    return {"reply": ask_chatbot(prompt)}


@app.get("/insights")
def insights():
    sample_data = {"inventory": 120, "shipments": 15, "delays": 3}
    return {"insight": generate_insight(sample_data)}


@app.get("/routes")
def routes(origin: str, destination: str):
    return get_routes(origin, destination)


@app.get("/weather")
def weather(city: str):
    return get_weather(city)
