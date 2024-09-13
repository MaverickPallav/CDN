from origin_server import OriginServer
from dns_server import DNSServer
from load_balancer import LoadBalancer
from monitoring_and_management import MonitoringAndManagement

class ContentDeliveryNetwork:
    def __init__(self):
        self.edge_servers = []
        self.origin_server = OriginServer()
        self.dns_server = DNSServer()
        self.load_balancer = LoadBalancer(self.edge_servers)
        self.monitoring_and_management = MonitoringAndManagement(self.edge_servers, self.load_balancer)

    def serve_content(self, url):
        content = self.origin_server.get_content(url)
        selected_edge_server = self.load_balancer.select_server()
        selected_edge_server.store_content(url, content)
        ip_address = self.dns_server.get_ip_address(url)
        selected_edge_server.serve_content(ip_address, url)
