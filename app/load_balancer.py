import random

class LoadBalancer:
    def __init__(self, edge_servers):
        self.edge_servers = edge_servers

    def select_server(self, client_location=None):
        if client_location:
            # In a real implementation, choose based on proximity
            print(f"Selecting closest edge server for {client_location}")
        return random.choice(self.edge_servers)

    def update_servers(self, new_servers):
        self.edge_servers = new_servers
