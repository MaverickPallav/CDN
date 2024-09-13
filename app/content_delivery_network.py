from edge_server import EdgeServer
from origin_server import OriginServer
from dns_server import DNSServer
from load_balancer import LoadBalancer
from monitoring_and_management import MonitoringAndManagement

class ContentDeliveryNetwork:
    def __init__(self):
        self.edge_servers = [EdgeServer() for _ in range(5)]  # Initial pool of edge servers
        self.origin_server = OriginServer()
        self.dns_server = DNSServer()
        self.load_balancer = LoadBalancer(self.edge_servers)
        self.monitoring_and_management = MonitoringAndManagement(self.edge_servers, self.load_balancer)

    def serve_content(self, url, client_location=None):
        selected_edge_server = self.load_balancer.select_server(client_location)
        ip_address = self.dns_server.get_ip_address(url)
        
        # Try to serve from the edge server
        if not selected_edge_server.serve_content(ip_address, url):
            # Fetch from origin server if not in cache
            content = self.origin_server.get_content(url)
            selected_edge_server.store_content(url, content)
            selected_edge_server.serve_content(ip_address, url)

    def invalidate_content(self, url):
        for server in self.edge_servers:
            server.remove_content(url)

    def prefetch_content(self, urls):
        for url in urls:
            content = self.origin_server.get_content(url)
            for server in self.edge_servers:
                server.store_content(url, content)
