# Load Balancers

## AWS Load Balancers

AWS offers four types of managed load balancers to distribute incoming application traffic across multiple targets:

1. **Classic Load Balancer (CLB) - Old Generation:**
    - Supports: HTTP, HTTPS, TCP, SSL (Secure TCP).
    - Health Checks: Layer 7 (HTTP) or Layer 4 (TCP/SSL).
    - SSL Certificates: Supports only **one** SSL certificate, but it can have multiple Subject Alternative Names (SANs).
        - Adding/removing SANs requires updating the entire certificate.
        - For multiple distinct SSL certificates, multiple CLBs are needed.
    - TCP to TCP Traffic: Traffic goes directly to EC2 instances (transiting through CLB).
    - Two-way SSL Authentication: Happens at the EC2 instance level.
    - Recommendation: Generally recommended to use newer generation load balancers due to limitations.
2. **Application Load Balancer (ALB) - V2, New Generation:**
    
    ![image.png](image%2026.png)
    
    - Supports: HTTP, HTTPS, WebSocket.
    - Layer 7 load balancing (application level).
    - Load balancing across multiple machines in a target group.
    - Load balancing to multiple containers on the same machine (with dynamic port mapping), making it ideal for ECS.
    - Supports HTTP/2.
    - Rules and Redirects:
        - HTTP to HTTPS redirection at the ALB level.
        - Content-based routing based on path, headers, query strings, etc.
    - Targets:
        - EC2 instances (often in Auto Scaling Groups).
        - ECS tasks.
        - Lambda functions (HTTP request translated to JSON event).
        - IP addresses (private IPs).
    - Multiple target groups per ALB.
    - Health checks at the target group level.
3. **Network Load Balancer (NLB) - New Generation:**
    
    ![image.png](image%2027.png)
    
    - Supports: TCP, TLS (Secure TCP), UDP.
    - Layer 4 load balancing (transport level).
    - High performance, handles millions of requests per second.
    - Low latency (around 100 milliseconds).
    - Static IPs: One static IP per Availability Zone. Supports assigning Elastic IPs if the NLB is public.
    - Use Cases: Extreme performance for TCP or UDP traffic.
    - Targets:
        - EC2 instances.
        - IP addresses (private IPs, on-premises servers).
        - Application Load Balancers (chaining for ALB features with NLB static IPs).
    - Zonal DNS Name:
        
        ![image.png](image%2028.png)
        
        - **Regional DNS Name (default):** Resolves to all NLB node IPs across enabled AZs.
        - **Zonal DNS Name:** Resolves to a single IP address of an NLB node in a specific AZ (e.g., `nlb-dns-name.us-east-1a.elb.amazonaws.com`).
        - **Use Case for Zonal DNS:** Minimize latency and data transfer costs by ensuring traffic from an instance in a specific AZ goes to the NLB node in the same AZ. Requires application-specific logic to resolve the correct zonal DNS name based on the instance's AZ.
4. **Gateway Load Balancer (GWLB) - Introduced in 2020:**
    
    ![image.png](image%2029.png)
    
    - Operates at Layer 3 (Network Layer - IP Protocol).
    - Used to deploy, scale, and manage third-party network virtual appliances (NVAs) in AWS.
    - Use Cases: Firewall, Intrusion Detection and Prevention Systems (IDPS), Deep Packet Inspection (DPI), Payload Manipulation.
    - Combines:
        - **Transparent Network Gateway:** Single entry/exit point for all traffic.
        - **Load Balancer:** Distributes traffic to NVAs.
    - Protocol: Uses GENEVE protocol on port 6081.
    - Traffic Flow: User -> GWLB -> Target Group (NVAs) -> GWLB -> Application.
    - Targets:
        - EC2 instances.
        - IP addresses (private IPs).

**Internal vs. External ELBs:**

- Some load balancer types (ALB, NLB, CLB) can be configured as:
    - **Internal (Private):** Only accessible within the VPC.
    - **External (Public):** Accessible from the internet.

**Recommendation:** Favor using the newer generation load balancers (ALB, NLB, GWLB) over the Classic Load Balancer for their enhanced features and long-term support.