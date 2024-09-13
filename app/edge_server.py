import zlib
import time

class EdgeServer:
    def __init__(self):
        self.stored_content = {}
        self.cache_ttl = {}

    def store_content(self, url, content, ttl=600):
        compressed_content = zlib.compress(content.encode())
        self.stored_content[url] = compressed_content
        self.cache_ttl[url] = time.time() + ttl

    def serve_content(self, ip_address, url):
        if url in self.cache_ttl and time.time() > self.cache_ttl[url]:
            print(f"Cache expired for {url}")
            del self.stored_content[url]
            del self.cache_ttl[url]
            return False
        
        content = self.stored_content.get(url)
        if content:
            decompressed_content = zlib.decompress(content).decode()
            print(f"Serving content to {ip_address} for URL {url}")
            return True
        else:
            print(f"Content not found on edge server for {url}")
            return False

    def remove_content(self, url):
        if url in self.stored_content:
            del self.stored_content[url]
            del self.cache_ttl[url]
            print(f"Content removed from edge server for {url}")
