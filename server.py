import flwr as fl
import os

if __name__ == "__main__":
    strategy = fl.server.strategy.FedAvg()
    port = os.environ.get("PORT", 10000)  # Default to 10000 if PORT not set
    fl.server.start_server(server_address=f"0.0.0.0:{port}", strategy=strategy)
