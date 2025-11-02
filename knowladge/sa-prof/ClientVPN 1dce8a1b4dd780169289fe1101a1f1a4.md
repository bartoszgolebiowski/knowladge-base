# ClientVPN

## **AWS Site-to-Site VPN**

### **Core Concepts**

- Connects on-premises data centers to AWS VPCs over the public internet.
- Enables access using private IP addresses, secured by encryption.

### **Setup Components**

- **On-premises:**
    - Software or hardware VPN appliance.
    - Publicly accessible IP address for the VPN appliance.
- **AWS:**
    - **Virtual Private Gateway (VGW):** Attached to the VPC (VPC-level resource).
    - **Customer Gateway (CGW):** Configured with the public IP of the on-premises VPN appliance.
    - **VPN Connection:** Established between the VGW and CGW.
- **Redundancy:** Two VPN tunnels are automatically created for high availability.
- **Encryption:** All communication is encrypted using IPSec.
- **Acceleration (Optional):** AWS Global Accelerator can be used to improve performance for worldwide networks.

## **Route Propagation**

### **Scenario**

- Corporate data center and VPC with non-overlapping CIDRs.
- Site-to-site VPN connection established (VGW on VPC, CGW on-premises).

### **Requirement**

- Instances in private subnets need to communicate through the VGW.
- On-premises servers need to communicate through the CGW.

### **Route Table Configuration**

- **VPC Route Table (Subnet Level):** Route traffic destined for the corporate data center CIDR to the VGW.
- **On-premises Router:** Route traffic destined for the VPC private subnet CIDR to the CGW.

### **Routing Options**

- **Static Routing:**
    - Manual configuration of route table entries on both the VPC and on-premises.
    - Requires manual updates if network changes occur.
- **Dynamic Routing (BGP - Border Gateway Protocol):**
    - Automatic sharing of routes between networks.
    - eBGP (external BGP) is used over the internet.
    - Requires specifying the Autonomous System Number (ASN) for both the CGW (custom ASN) and the VGW (custom ASN).
    - Enabling BGP automatically updates route tables.

## **Internet Access Scenarios**

### **On-premises to Internet via VPC**

- **Scenario 1 (NAT Gateway):** On-premises server -> CGW -> VGW -> NAT Gateway -> Internet Gateway -> https://www.google.com/search?q=Google.com
    - **Result: No.** NAT Gateway restricts traffic originating from site-to-site VPN or Direct Connect.
- **Scenario 2 (NAT Instance):** On-premises server -> CGW -> VGW -> NAT Instance -> Internet Gateway -> https://www.google.com/search?q=Google.com
    - **Result: Yes.** Full control over the NAT Instance allows for custom routing.

### **VPC to Internet via On-premises**

- **Scenario 3 (On-premises NAT):** Instance in private subnet -> VGW -> CGW -> On-premises NAT -> https://www.google.com/search?q=Google.com
    - **Result: Yes.** Valid setup, especially if on-premises NAT provides existing packet filtering and security rules.

## **VPN CloudHub**

### **Concept**

- Connects multiple Customer Gateways together through a single Virtual Private Gateway.
- Supports up to 10 Customer Gateways per VGW.

### **Use Cases**

- **Low-cost hub-and-spoke model:** For primary network connectivity between multiple data center locations.
- **Secondary/Failover Network:** Provides redundancy if primary connections between customer networks fail.

### **Functionality**

- Secure communication between connected sites via established VPN connections.
- Traffic traverses the public internet, secured by IPSec encryption.

### **Example**

- Customer networks in New York, Los Angeles, and Miami connecting through a central VGW.
- If a direct connection between New York and Los Angeles fails, traffic can fail over to the VPN CloudHub.

## **Multiple VPC Connections**

### **Challenge**

- Connecting multiple VPCs to a single on-premises data center using separate site-to-site VPN connections can become complex to manage.

### **AWS Recommendation (VPN-based)**

- Create a separate VPN connection for each VPC.

### **Alternative Solutions**

- **Direct Connect Gateway:** Recommended by AWS for simpler management (covered in Direct Connect lectures).
- **Shared Services VPC:**
    - Establish a single VPN connection between the on-premises data center and a Shared Services VPC.
    - Replicate services or deploy proxies from on-premises to the Shared Services VPC.
    - Utilize VPC peering between other VPCs and the Shared Services VPC.
    - **Benefit:** Reduces the number of VPN connections required.
    - **Limitation:** VPC peering is not transitive (VPC A cannot directly access the on-premises data center; it communicates through the Shared Services VPC).