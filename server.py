# server.py
import threading
import flwr as fl
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Flower Server is running."}

def start_flower():
    strategy = fl.server.strategy.FedAvg()
    fl.server.start_server(server_address="0.0.0.0:8080", strategy=strategy)

# Start Flower in a background thread
threading.Thread(target=start_flower).start()

# This file will now serve both FastAPI (port 10000) and Flower (port 8080)
