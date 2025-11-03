# Basic VPC

Alright, let's solidify these VPC fundamentals. Here's a breakdown of the key concepts covered in the lecture, presented in a structured markdown format:

## **VPC Basics Recap**

This section revisits essential VPC concepts that are crucial for understanding more advanced topics and for the AWS Solution Architect Professional exam.

**1. CIDR Blocks (Classless Inter-Domain Routing):**

- Represent a range of IP addresses.
- Defined as `IP Address/Number`, where the number indicates the number of fixed bits in the network prefix, determining the size of the IP range.
- Example: `192.168.0.0/26` represents 64 IP addresses from `192.168.0.0` to `192.168.0.63`.
- Used extensively in AWS for defining VPCs, subnets, security groups, route tables, etc.

**2. Private IP Addresses:**

- IP addresses that are only accessible within a private network.
- Defined by specific ranges:
    - `10.0.0.0` - `10.255.255.255` (`10.0.0.0/8`) - Large networks.
    - `172.16.0.0` - `172.31.255.255` (`172.16.0.0/12`) - Medium-sized networks.
    - `192.168.0.0` - `192.168.255.255` (`192.168.0.0/16`) - Small or home networks.
- Any IP address outside these ranges is considered a public IP address.

**3. Virtual Private Cloud (VPC):**

- A logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
- Defined by a list of one or more CIDR blocks.
- CIDR blocks for a VPC cannot be changed after creation.
- Each CIDR block within a VPC must have a minimum size of `/28` (16 IP addresses) and a maximum size of `/16` (65,536 IP addresses).
- VPCs are inherently private; only private IP CIDR ranges are allowed within a VPC.

**4. Subnets:**

- Partitions of a VPC into one or more segments.
- Defined by a CIDR block that is a subset of the VPC's CIDR block.
- Instances within a subnet receive a private IP address from the subnet's CIDR range.
- The first four and the last IP addresses in each subnet's CIDR block are reserved by AWS for networking purposes.

**5. Route Tables:**

- Control the destination of network traffic leaving subnets.
- Associated with one or more subnets.
- Contain a set of routing rules (routes) that specify where traffic should be directed based on the destination IP address range.
- The most specific route (longest prefix match, highest `/` number) is always followed.

**6. Internet Gateway (IGW):**

- A horizontally scaling, highly available VPC component that allows communication between instances in your VPC and the internet.
- Acts as a network address translation (NAT) service for instances with a public IPv4 or IPv6 address.
- **Public Subnets:** Subnets associated with a route table that directs internet-bound traffic (`0.0.0.0/0` for IPv4 or `::/0` for IPv6) to an Internet Gateway. Instances in public subnets must have a public IP address to communicate with the internet.

**7. NAT (Network Address Translation):**

- Allows instances in private subnets to connect to the internet or other AWS services but prevents the internet from initiating connections with those instances.
- **NAT Instance:**
    - An EC2 instance deployed in a public subnet that is configured to forward internet traffic from instances in private subnets.
    - Requires manual management for high availability and scaling.
    - Bandwidth is limited by the instance type.
    - Failover must be self-managed.
    - Source/destination check must be disabled on the NAT Instance.
    - Assigned an Elastic IP address, so all outbound traffic appears to originate from this IP.
- **NAT Gateway:**
    - A managed service that provides NAT for instances in private subnets.
    - Highly available within a single Availability Zone (AZ). Can be deployed in multiple AZs for cross-AZ resilience.
    - Scales automatically with bandwidth demands.
    - Assigns an Elastic IP address to each NAT Gateway.

**8. Network ACLs (NACLs):**

- Stateless firewalls that operate at the subnet level.
- Apply to all instances within the associated subnet.
- Support both `allow` and `deny` rules.
- Stateless nature requires explicit rules for both inbound and outbound traffic.
- Provide a quick and cost-effective way to block specific IP addresses.

**9. Security Groups:**

- Stateful firewalls that operate at the instance level.
- Apply to individual EC2 instances (and other supported resources).
- Only support `allow` rules.
- Stateful nature automatically allows return traffic for allowed inbound or outbound connections.
- Allow referencing other security groups within the same region (including peered VPCs and cross-account).

**10. VPC Flow Logs:**

- Enable capturing information about the IP traffic going to and from network interfaces in your VPC.
- Can be created at the VPC, subnet, or Elastic Network Interface (ENI) level.
- Helpful for troubleshooting network connectivity issues and security analysis.
- Flow log data can be sent to CloudWatch Logs or Amazon S3.

**11. Bastion Hosts:**

- Public-facing EC2 instances in a public subnet used to securely SSH into private EC2 instances (a two-hop SSH connection).
- Require self-management for high availability, security, and patching.
- Increasingly being replaced by AWS Systems Manager (SSM) Session Manager for more secure remote access without SSH.

**12. IPv6:**

- The next-generation Internet Protocol designed to address the limitations of IPv4 address space.
- Offers a vastly larger address space (3.4 x 10^38 addresses).
- All IPv6 addresses are public. The sheer number makes scanning for open ports extremely difficult.
- **VPC Support:**
    - You can associate an IPv6 CIDR block with your VPC.
    - Internet Gateways support IPv6 traffic.
    - Instances in public subnets can be assigned IPv6 addresses from the VPC's CIDR.
    - Route tables in public subnets need a route for `::/0` (all IPv6 traffic) to the Internet Gateway.
    - **Egress-Only Internet Gateway:** Provides IPv6-only outbound internet access for instances in private subnets. Route tables in private subnets direct `::/0` traffic to the Egress-Only Internet Gateway.

This foundational knowledge of VPC concepts is essential for tackling more complex networking scenarios and questions on the AWS Solution Architect Professional exam. The subsequent lectures will delve deeper into specific aspects of VPC.