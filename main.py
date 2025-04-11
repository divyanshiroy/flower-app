import flwr as fl

def fit_config(rnd):
    return {"epochs": 1}

# Start Flower server
fl.server.start_server(
    config=fl.server.ServerConfig(num_rounds=1),
    strategy=fl.server.strategy.FedAvg(
        on_fit_config_fn=fit_config
    ),
)
