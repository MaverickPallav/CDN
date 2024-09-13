from content_delivery_network import ContentDeliveryNetwork

if __name__ == "__main__":
    # Initialize CDN
    cdn = ContentDeliveryNetwork()

    # Serving content
    print("Serving content from CDN:")
    cdn.serve_content("example.com")
    
    # Test prefetching content
    print("\nPrefetching content:")
    cdn.prefetch_content(["example.com", "test.com"])
    
    # Test invalidating content
    print("\nInvalidating content:")
    cdn.invalidate_content("example.com")
    
    # Test monitoring and auto-scaling
    print("\nMonitoring and Auto-scaling:")
    cdn.monitoring_and_management.monitor_performance()
    cdn.monitoring_and_management.autoscale()

    # Add DNS domain mapping
    print("\nAdding DNS Domain Mapping:")
    cdn.dns_server.add_domain_mapping("example.com", "192.168.1.10")
    
    # Deploy edge servers
    print("\nDeploying Edge Servers:")
    cdn.monitoring_and_management.deploy_edge_server("New York")
    cdn.monitoring_and_management.deploy_edge_server("San Francisco")

    # Serve content again to check newly deployed servers
    print("\nServing content again:")
    cdn.serve_content("example.com")

    # Monitor performance after deploying new edge servers
    print("\nMonitoring performance after deployment:")
    cdn.monitoring_and_management.monitor_performance()
