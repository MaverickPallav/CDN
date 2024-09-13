from content_delivery_network import ContentDeliveryNetwork

if __name__ == "__main__":
    # Initialize CDN
    cdn = ContentDeliveryNetwork()

    # Add DNS domain mapping
    cdn.dns_server.add_domain_mapping("example.com", "192.168.1.10")

    # Deploy edge servers
    cdn.monitoring_and_management.deploy_edge_server("New York")
    cdn.monitoring_and_management.deploy_edge_server("San Francisco")

    # Serve content
    cdn.serve_content("example.com")

    # Monitor performance
    cdn.monitoring_and_management.monitor_performance()
