class DNSServer:
    def __init__(self):
        self.domain_mappings = {}

    def add_domain_mapping(self, url, ip_address):
        self.domain_mappings[url] = ip_address

    def get_ip_address(self, url):
        return self.domain_mappings.get(url, "0.0.0.0")  # Return a default IP if not found
