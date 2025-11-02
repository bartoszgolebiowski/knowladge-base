# Direct Connection

## **AWS Direct Connect**

### **Core Concepts**

- Provides a dedicated, private network connection from an on-premises network to AWS.
- Establishes a physical Ethernet connection between a customer's data center and an AWS Direct Connect location.
- Offers more reliable and higher-bandwidth connectivity compared to internet-based VPNs.
- Access to AWS services occurs through Virtual Interfaces (VIFs).
- Bypasses public internet service providers, potentially reducing public network costs and increasing stability.
- Redundancy is not built-in; requires setting up a secondary Direct Connect connection or a VPN as a failover.

### **Virtual Interfaces (VIFs)**

- **Public VIF:** Enables connection to public AWS endpoints (e.g., S3, EC2 public IPs, DynamoDB).
- **Private VIF:** Enables connection to private resources within a VPC (e.g., EC2 instances with private IPs, ALB, RDS within a VPC).
- **Transit Virtual Interface:** Enables connection to resources in VPCs attached to a Transit Gateway.
- **VPC Interface Endpoints:** Accessible through a private VIF.

### **Direct Connect Setup**

- **AWS Region:** The AWS region to connect to.
- **Corporate Data Center (Customer Network):** The on-premises location.
- **Direct Connect Location:** A physical AWS facility with:
    - **AWS Cage:** Contains the Direct Connect endpoint.
    - **Customer/Partner Cage:** Contains the customer or partner router.
- **Customer Router/Firewall:** Located in the customer's data center.
- **Private VIF Flow:** Customer Router -> Customer/Partner Router -> Direct Connect Endpoint -> Virtual Private Gateway (VGW) -> Private Subnet -> EC2 Instances.
- **Public VIF Flow:** Customer Router -> Customer/Partner Router -> Direct Connect Endpoint -> AWS Public Services (e.g., S3, Glacier).

### **Connection Types**

- **Dedicated Connections:**
    - Physical Ethernet port dedicated to a single customer.
    - Available in 1 Gbps, 10 Gbps, and 100 Gbps capacities.
    - Request initiated with AWS and provisioned by a Direct Connect partner.
    - Lead time for new connections is typically longer than one month.
- **Hosted Connections:**
    - Provisioned by AWS Direct Connect partners.
    - Available in various speeds (e.g., 50 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps).
    - Capacity can often be added or removed on demand.
    - Request made through the AWS Direct Connect partner.
    - Lead times for new connections are generally longer than one month.

### **Encryption**

- Data in transit over a Direct Connect connection is private but **not inherently encrypted**.
- To encrypt data, a VPN connection (IPsec) can be established over the Direct Connect link, typically using a public VIF.
- VPN over Direct Connect provides an extra layer of security but adds complexity and might not be as efficient as encrypting a public internet connection.

### **Link Aggregation Groups (LAG)**

- Logically groups multiple dedicated Direct Connect connections into a single, higher-bandwidth connection.
- Increases bandwidth and provides failover capabilities (active-active mode).
- Supports up to four dedicated connections per LAG.
- Connections within a LAG must:
    - Be dedicated connections.
    - Have the same bandwidth.
    - Terminate at the same AWS Direct Connect connection endpoint.
- A minimum number of connections required for the LAG to be active can be configured (default is one).

### **Direct Connect Gateway**

- Enables a single Direct Connect connection to interface with multiple VPCs across different AWS Regions within the same or across different AWS accounts.
- Simplifies connectivity management for large-scale deployments.
- Requires creating a Direct Connect Gateway and associating private VIFs from different VPCs to it.
- The Direct Connect connection's private VIF connects to the Direct Connect Gateway.
- The gateway then routes traffic to the associated VPCs.

### **Direct Connect Gateway and Transit Gateway**

- Transit Gateway serves as a central hub to connect VPCs, VPN connections, and Direct Connect connections.
- To connect a Direct Connect connection to a Transit Gateway, a Direct Connect Gateway is required.
- The private VIF of the Direct Connect connection attaches to the Direct Connect Gateway, which in turn associates with the Transit Gateway.
- This allows traffic from the Direct Connect connection to reach any VPC or VPN connected to the Transit Gateway.