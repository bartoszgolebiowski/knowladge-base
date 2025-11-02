# PrivateLink

## AWS PrivateLink (VPC Endpoint Services)

**Core Concept:**

- Provides the most secure and scalable way to expose services privately to thousands of VPCs (within your account or other accounts).
- Enables private connectivity without relying on:
    - VPC peering complexities
    - Internet Gateways
    - NAT Gateways/Instances
    - Public route tables

**Benefits:**

- **Enhanced Security:** Limits network exposure to a single PrivateLink connection.
- **Scalability:** Easily extend service access to numerous VPCs.
- **Simplified Networking:** Eliminates the need for complex routing configurations associated with peering or public internet access.

**How it Works (Service Provider Perspective):**

1. Create your application service within a **Service VPC**.
2. Deploy a **Network Load Balancer (NLB)** in the Service VPC to front your application.
3. On the **Customer VPC** side, an **Elastic Network Interface (ENI)** will be created.
4. **AWS PrivateLink** establishes a private connection between the ENI in the Customer VPC and the NLB in the Service VPC.
5. Customers access your service by communicating with the ENI in their VPC.
6. Traffic flows privately from the ENI to the NLB and then to your application service.

**Scalability and Fault Tolerance:**

- Highly scalable by creating one NLB and multiple ENIs for each consuming VPC.
- To achieve fault tolerance, ensure the NLB spans multiple Availability Zones (AZs), and corresponding ENIs are also in multiple AZs within the customer VPCs.

**PrivateLink for Amazon S3 with Direct Connect:**

![image.png](image%2038.png)

- **Problem:** Accessing an S3 bucket from a Corporate Data Center over a Direct Connect connection.
- **Option 1 (Public VIF):** Traffic travels from Direct Connect to the public S3 URL, but over the private Direct Connect connection.
- **Option 2 (Private Access):** Requires a **Interface VPC Endpoint** for S3 (leveraging PrivateLink).
    - **Gateway Endpoints** are not suitable for Direct Connect access as they only function within a VPC.
    - A **Private VIF** must be created for the Direct Connect connection to route traffic privately through your VPC to the Interface VPC Endpoint for S3.

**Accessing PrivateLink over VPC Peering:**

![image.png](image%2039.png)

- To access an Interface VPC Endpoint in one region from another region for private S3 access:
    1. Create an **Interface VPC Endpoint for S3** in the region where your S3 bucket resides (e.g., `eu-west-1`).
    2. Establish a **VPC Peering** connection between your VPC in another region (e.g., `us-east-1`) containing your EC2 instances and the VPC in the S3 bucket's region.
    3. EC2 instances in the peered VPC can then use the URL of the Interface VPC Endpoint to privately access S3 in the other region.
- **Important:** The Interface VPC Endpoint must be in the **same region** as the S3 bucket.

**Key Takeaway for the Exam:**

- Understand the core benefits and functionality of AWS PrivateLink for secure and scalable private connectivity.
- Differentiate between Gateway Endpoints and Interface VPC Endpoints and their use cases, especially in the context of Direct Connect.
- Grasp how PrivateLink can be accessed across peered VPCs in different regions.