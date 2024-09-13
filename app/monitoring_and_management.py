from edge_server import EdgeServer

class MonitoringAndManagement:
    def __init__(self, edge_servers, load_balancer):
        self.edge_servers = edge_servers
        self.load_balancer = load_balancer

    def monitor_performance(self):
        print(f"Monitoring performance of {len(self.edge_servers)} edge servers.")

    def deploy_edge_server(self, location="New Location"):
        edge_server = EdgeServer()
        self.edge_servers.append(edge_server)
        self.load_balancer.update_servers(self.edge_servers)
        print(f"Deployed new edge server at {location}")

    def autoscale(self):
        if len(self.edge_servers) < 10:
            print("Auto-scaling: Deploying new edge server.")
            self.deploy_edge_server()
        else:
            print("No need to scale at this time.")
