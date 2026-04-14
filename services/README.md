# Services Prototype (FastAPI + ML + LLM)

This folder contains a hackathon-friendly service layer with:
- demand forecasting (Prophet)
- delay prediction (RandomForest)
- chatbot + AI insights (Gemini)
- maps and weather integrations

## 1) Setup

From repo root:

```bash
pip install -r services/requirements.txt
```

Create env file:

```bash
copy services\\.env.example services\\.env
```

Update `services/.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
WEATHER_API_KEY=your_openweather_api_key_here
```

## 2) Train ML Models

From repo root:

```bash
cd services
python -m ml.demand.train
python -m ml.delay.train
```

Starter datasets are included:
- `services/ml/demand/sales_data.csv`
- `services/ml/delay/delay_data.csv`

## 3) Run API

From repo root:

```bash
cd services
uvicorn api.service_api:app --reload
```

Server URL: `http://127.0.0.1:8000`

## 4) Endpoints

- `GET /`
- `GET /predict-demand`
- `POST /predict-delay?distance=10&traffic=4&weather=2`
- `POST /chat?prompt=How%20can%20I%20reduce%20delivery%20delays%3F`
- `GET /insights`
- `GET /routes?origin=Kolkata&destination=Bhubaneswar`
- `GET /weather?city=Kolkata`

## 5) Quick curl Examples

```bash
curl http://127.0.0.1:8000/
```

```bash
curl http://127.0.0.1:8000/predict-demand
```

```bash
curl -X POST "http://127.0.0.1:8000/predict-delay?distance=10&traffic=4&weather=2"
```

```bash
curl -X POST "http://127.0.0.1:8000/chat?prompt=Give%20me%203%20tips%20to%20optimize%20inventory"
```

```bash
curl "http://127.0.0.1:8000/routes?origin=Kolkata&destination=Bhubaneswar"
```

```bash
curl "http://127.0.0.1:8000/weather?city=Kolkata"
```

## 6) Backend Integration Notes

Your Express backend can call:
- `http://127.0.0.1:8000/predict-demand`
- `http://127.0.0.1:8000/chat`
- `http://127.0.0.1:8000/routes`
- `http://127.0.0.1:8000/weather`

Then relay the response to frontend UI.

## 7) Postman Import

Import both files in Postman:
- `services/postman_collection.json`
- `services/postman_environment.json`

Select environment: `SIA Services Local`.
