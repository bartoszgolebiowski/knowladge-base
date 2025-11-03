# VPC Logs

## **VPC Flow Logs**

### **Core Functionality**

- Captures information about IP traffic going to and from network interfaces within your VPC.
- Can be enabled at the VPC, subnet, or Elastic Network Interface (ENI) level.
- Provides valuable insights for monitoring and troubleshooting network connectivity issues within your VPC.
- Captures traffic for AWS-managed interfaces like ELB, RDS, ElastiCache, Redshift, WorkSpaces, NAT Gateway, Transit Gateway, etc.

### **Flow Log Destinations**

- **Amazon S3:** For long-term storage and batch analysis.
- **Amazon CloudWatch Logs:** For real-time monitoring, alerting, and querying.
- **Kinesis Data Firehose:** For streaming data to other AWS services like Amazon Elasticsearch Service.

### **VPC Flow Log Format (Example)**

`version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status`

### **Information Derived from Flow Logs**

- **Source Address & Destination Address:** Identify problematic IPs, potential attacks, or misconfigured sources/destinations.
- **Source Port & Destination Port:** Pinpoint issues related to specific services or applications.
- **Action (ACCEPT/REJECT):** Indicates whether traffic was allowed or denied by Security Groups or Network ACLs (NACLs).
- **Usage Patterns & Security Analysis:** Enables analytics on network traffic volume, detection of malicious behavior (port scans), and compliance auditing.

### **Querying and Analyzing Flow Logs**

- **Amazon Athena on S3:** For running SQL queries on flow logs stored in S3.
- **CloudWatch Logs Insights:** For performing interactive log analysis and creating queries for flow logs in CloudWatch Logs.

### **Troubleshooting Security Groups and NACLs with Flow Logs**

- **Inbound Request Analysis:**
    - **REJECT (Inbound):** Could be a NACL or Security Group denying the incoming traffic.
    - **ACCEPT (Inbound) and REJECT (Outbound):** Indicates a NACL is blocking the return traffic (NACLs are stateless, Security Groups are stateful).
- **Outbound Request Analysis:**
    - **REJECT (Outbound):** Could be a NACL or Security Group denying the outgoing traffic.
    - **ACCEPT (Outbound) and REJECT (Inbound):** Indicates a NACL is blocking the returning response.

### **VPC Flow Log Architectures**

- **CloudWatch Contributor Insights:** Analyze top talkers (IP addresses, ENIs) by network traffic volume.
- **CloudWatch Metrics & Alarms:** Create metric filters to track specific traffic patterns (e.g., SSH/RDP attempts) and trigger alarms via SNS for potential security incidents.
- **S3 Storage & Athena/QuickSight:** Store flow logs in S3 for long-term analysis using SQL with Athena and visualize the data with QuickSight.

### **Troubleshooting Scenario: Unexpected ACCEPT Logs for NAT Gateway Inbound Traffic**

- **The Issue:** VPC Flow Logs show `Action = ACCEPT` for inbound traffic from public IPs to your VPC, even though NAT Gateways are not supposed to accept unsolicited inbound traffic from the internet.
- **Possible Cause:** The Security Group or NACLs associated with the NAT Gateway's ENI might be allowing the inbound traffic. However, the NAT Gateway itself will drop this unsolicited traffic.
- **Verification using CloudWatch Logs Insights:***(where `xxx.xxx` represents the first two octets of your VPC CIDR and `PUBLIC_IP_ADDRESS` is the external IP you are investigating)*
    
    `filter dstAddr like "xxx.xxx" and srcAddr != "169.254.%"
    | filter srcAddr like "PUBLIC_IP_ADDRESS"
    | stats sum(bytes) as bytesTransferred by srcAddr, dstAddr`
    
- **Expected Result:** You will likely see log entries with the destination address being the private IP address of the NAT Gateway's ENI, indicating that the traffic was allowed by the security group/NACL associated with the NAT Gateway. However, you won't see further traffic beyond the NAT Gateway's private IP, confirming that the unsolicited internet traffic was dropped by the NAT Gateway itself.