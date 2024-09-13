import random

class LoadBalancer:
    def __init__(self, edge_servers):
        self.edge_servers = edge_servers

    def select_server(self):
        if not self.edge_servers:
            raise Exception("No edge servers available")
        # Basic random selection load balancing
        return random.choice(self.edge_servers)

    def update_servers(self, new_servers):
        self.edge_servers = new_servers
