# Network Firewall

Okay, let's break down AWS Network Firewall.

## **AWS Network Firewall**

### **Purpose**

- Provides stateful network firewall capabilities to protect your entire Amazon Virtual Private Cloud (VPC).
- Offers Layer 3 (Network) to Layer 7 (Application) protection.
- Inspects traffic in all directions:
    - VPC to VPC
    - Outbound to Internet
    - Inbound from Internet
    - To and from Direct Connect and Site-to-Site VPN connections.

### **Core Functionality**

- **Rule-Based Control:** Define rules to allow, drop, or alert on network traffic based on various criteria.
- **Deep Packet Inspection:** Inspects the actual content of network packets for threats.
- **AWS Gateway Load Balancer Integration (Internal):** Leverages the Gateway Load Balancer infrastructure, but the inspection appliances are managed by AWS.
- **Centralized Management:** Rules can be centrally managed across multiple accounts and VPCs using AWS Firewall Manager.

### **Granular Traffic Control**

- **IP and Port Filtering:** Supports thousands of rules, filtering by source and destination IP addresses (tens of thousands of IPs supported) and ports.
- **Protocol Filtering:** Control traffic based on network protocols (e.g., disable SMB outbound).
- **Domain Filtering:** Allow or deny traffic to specific domain names (e.g., corporate domains, approved software repositories).
- **Pattern Matching:** Supports general pattern matching using regular expressions.
- **Actions:** Configure rules to `ALLOW`, `DROP`, or `ALERT` matching traffic.
- **Active Flow Inspection:** Provides Intrusion Prevention System (IPS) capabilities.
- **Logging and Monitoring:** Rule match logs can be sent to Amazon S3, CloudWatch Logs, and Kinesis Data Firehose for analysis and auditing.

### **Architectures with AWS Network Firewall (Centralized Inspection Model using AWS Transit Gateway)**

The common pattern for implementing AWS Network Firewall for comprehensive protection involves routing all relevant traffic through a dedicated inspection VPC containing the Network Firewall endpoints. This is often facilitated by AWS Transit Gateway.

![image.png](image%2043.png)

**1. North-South Traffic (VPC Egress to Internet):**

1. Traffic originates from instances in a workload VPC.
2. Routes to the **Transit Gateway**.
3. Transit Gateway routes the traffic to the **Inspection VPC**.
4. Traffic passes through the **AWS Network Firewall** in the Inspection VPC.
5. The Network Firewall forwards the inspected traffic back to the **Transit Gateway**.
6. Transit Gateway routes the traffic to the **Egress VPC**.
7. The Egress VPC routes the traffic to the **Internet Gateway** and out to the internet.

**2. North-South Traffic (VPC Ingress from Internet - Not explicitly shown but conceptually similar):**

1. Traffic originates from the internet and enters through an Internet Gateway (likely in an Egress/Ingress VPC).
2. Routes to the **Transit Gateway**.
3. Transit Gateway routes the traffic to the **Inspection VPC**.
4. Traffic passes through the **AWS Network Firewall** for inspection.
5. The Network Firewall forwards the inspected traffic back to the **Transit Gateway**.
6. Transit Gateway routes the traffic to the destination workload VPC.

**3. Traffic to On-Premises (via VPN or Direct Connect):**

1. Traffic originates from instances in a VPC.
2. Routes to the **Transit Gateway**.
3. Transit Gateway routes the traffic to the **Inspection VPC**.
4. Traffic passes through the **AWS Network Firewall**.
5. The Network Firewall forwards the inspected traffic back to the **Transit Gateway**.
6. Transit Gateway routes the traffic to the **VPN connection** or **Direct Connect Gateway**.

**4. East-West Traffic (VPC to VPC):**

1. Traffic originates from instances in a source VPC.
2. Routes to the **Transit Gateway**.
3. Transit Gateway routes the traffic to the **Inspection VPC**.
4. Traffic passes through the **AWS Network Firewall**.
5. The Network Firewall forwards the inspected traffic back to the **Transit Gateway**.
6. Transit Gateway routes the traffic to the destination VPC.

**Key Takeaway:** In these centralized inspection architectures, the **AWS Transit Gateway** acts as the central routing hub, ensuring that all traffic requiring inspection is directed to and from the **AWS Network Firewall** in the dedicated Inspection VPC.**12** This allows for consistent security policy enforcement across your AWS environment.