class EdgeServer:
    def __init__(self):
        self.stored_content = {}

    def store_content(self, url, content):
        self.stored_content[url] = content

    def serve_content(self, ip_address, url):
        content = self.stored_content.get(url)
        if content:
            print(f"Serving content to {ip_address} for URL {url}")
        else:
            print(f"Content for URL {url} not found on edge server.")
