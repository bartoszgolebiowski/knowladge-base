# VPC Peering

Alright, let's break down this crucial lecture on VPC Peering for the AWS Solution Architect Professional exam. Here's a structured summary in markdown format:

## **VPC Peering**

VPC peering allows you to create a networking connection between two VPCs, enabling them to communicate with each other privately as if they were within the same network. This communication happens over the internal AWS network.

**Key Concepts:**

- **Non-Overlapping CIDR Blocks:** For a VPC peering connection to be established, the CIDR blocks of the two VPCs must not overlap. This is a fundamental requirement.
- **Route Table Updates:** After establishing a VPC peering connection, you must update the route tables in each of the involved VPC subnets to direct traffic destined for the peer VPC's CIDR block to the VPC peering connection.
- **Non-Transitive Nature:** VPC peering connections are not transitive. If VPC A is peered with VPC B, and VPC A is also peered with VPC C, instances in VPC B cannot directly communicate with instances in VPC C. A direct peering connection between VPC B and VPC C is required for that communication.
- **Inter-Region and Cross-Account Peering:** VPC peering can be established between VPCs in different AWS Regions and between VPCs in different AWS accounts. The same requirements (non-overlapping CIDR, route table updates) apply.
- **Security Group Referencing:** Once a VPC peering connection is active, security groups in one peered VPC can reference security groups in the other peered VPC (even across accounts). This allows for granular security rules based on peer VPC security group membership.

**Longest Prefix Match for Routing:**

VPC routing decisions utilize the longest prefix match. When traffic needs to be routed, the route in the route table with the most specific destination CIDR block (the one with the highest `/` number) will be chosen.

- **Example:** If VPC A is peered with VPC B (CIDR `10.0.0.0/16`) and VPC C (also CIDR `10.0.0.0/16`), and you want specific traffic to `10.0.0.77/32` to go to VPC B, while all other `10.0.0.0/16` traffic goes to VPC C, you can achieve this by creating a route in VPC A's subnet route table with a destination of `10.0.0.77/32` pointing to the VPC B peering connection. This more specific route will take precedence over the `10.0.0.0/16` route to VPC C.

**Invalid VPC Peering Configurations:**

- **Overlapping IPv4 CIDR Blocks:** If any of the IPv4 CIDR blocks defined for two VPCs overlap, a VPC peering connection cannot be established. This holds true even if only one CIDR block overlaps when multiple CIDR blocks are associated with a VPC.
- **Overlapping IPv6 CIDR Blocks:** Similarly, if any IPv6 CIDR blocks overlap between two VPCs, peering is not allowed, even if their IPv4 CIDR blocks are different.
- **Transitive VPC Peering:** As emphasized, VPC peering is not transitive. Connections must be explicitly established between each pair of VPCs that need to communicate.
- **No Edge-to-Edge Routing:** This is a critical concept:
    - A VPC peered with another VPC **does not** extend the connectivity of other network connections associated with either VPC.
    - **Site-to-Site VPN Connection:** If VPC A is peered with VPC B, and VPC A has a VPN connection to your corporate network, VPC B **cannot** access the corporate network through the VPC A peering connection.
    - **Direct Connect Connection:** Same limitation as VPN.
    - **Internet Gateway (IGW):** If VPC A is peered with VPC B, instances in VPC B **cannot** access the internet through the Internet Gateway attached to VPC A.
    - **NAT Gateway:** If VPC A is peered with VPC B, instances in VPC B **cannot** use the NAT Gateway in VPC A to access the internet.
    - **Gateway VPC Endpoints (S3, DynamoDB):** If VPC A is peered with VPC B, instances in VPC B **cannot** access S3 or DynamoDB through the Gateway VPC Endpoint configured in VPC A.

**Example of an Invalid Configuration:**

A common scenario is trying to create a central VPC with a NAT Gateway connected to an Internet Gateway, and then peering other VPCs to this central VPC to provide internet access. **This configuration will not work** due to the "no edge-to-edge routing" rule for NAT Gateways over VPC peering. Private subnets in the peered VPCs will not be able to route traffic through the NAT Gateway in the central VPC to the Internet Gateway.

Understanding these limitations of VPC peering, especially the non-transitive nature and the lack of edge-to-edge routing, is crucial for the AWS Solution Architect Professional exam. The next lecture will likely discuss solutions to the central NAT Gateway scenario.