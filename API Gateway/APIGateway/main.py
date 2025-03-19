from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.get("/")
async def home():
    return {"service": "Servizio 1", "message": "Risposta dal Servizio 1"}

@app.get("/service2")
async def service2():
    return {"service": "Servizio 2", "message": "Risposta dal Servizio 2"}

@app.get("/service3")
async def service3():
    return {"service": "Servizio 3", "message": "Risposta dal Servizio 3"}

@app.get("/service4")
async def service4():
    return {"service": "Servizio 4", "message": "Risposta dal Servizio 4"}

@app.get("/gateway/{service_name}")
async def gateway(service_name: str):
    service_urls = {
        "service1": "http://127.0.0.1:8000/service1",
        "service2": "http://127.0.0.1:8000/service2",
        "service3": "http://127.0.0.1:8000/service3",
        "service4": "http://127.0.0.1:8000/service4"
    }

    if service_name not in service_urls:
        return {"error": "Servizio non trovato"}

    async with httpx.AsyncClient() as client:
        response = await client.get(service_urls[service_name])
        data = response.json()

    return {"message": "Risposta dal gateway", "data": data}
