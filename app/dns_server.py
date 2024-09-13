class DNSServer:
    def __init__(self):
        self.domain_mappings = {
            "example.com": "192.168.1.1",
            "test.com": "192.168.1.2"
        }
    
    def add_domain_mapping(self, url, ip_address):
        self.domain_mappings[url] = ip_address

    def get_ip_address(self, url):
        # Simulated DNS resolution
        return self.domain_mappings.get(url, "127.0.0.1")
