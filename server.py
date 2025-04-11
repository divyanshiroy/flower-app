import flwr as fl

if __name__ == '__main__':
    strategy = fl.server.strategy.FedAvg()
    fl.server.start_server(server_address='0.0.0.0:8080', strategy=strategy)
