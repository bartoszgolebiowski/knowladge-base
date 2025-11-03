# Outpost

# AWS Outposts

AWS Outposts is a fully managed service that extends AWS infrastructure, AWS services, APIs, and tools to customer premises. It is designed for organizations that need to run workloads on-premises due to latency requirements, local data processing needs, or data residency obligations, while still leveraging the benefits of the AWS cloud.

## Hybrid Cloud Challenges Addressed by Outposts

- **Inconsistent IT Management:** Traditional hybrid cloud often involves managing separate infrastructure stacks with different tools, APIs, and skill sets for on-premises and cloud environments.
- **Complexity:** Managing two distinct IT environments can be complex and inefficient.

## AWS Outposts Solution

- **Server Racks On-Premises:** AWS installs and manages racks of servers (Outposts racks) within your on-premises data center.
- **Same AWS Infrastructure and Services:** These racks offer the same AWS infrastructure services, APIs, and tools that are available in the AWS cloud.
- **Consistent Experience:** Developers and IT teams can use familiar AWS tools (Console, CLI, APIs) to build, deploy, and manage applications on Outposts, providing a consistent hybrid experience.
- **Preloaded AWS Services:** Outposts racks come preloaded with a selection of AWS services that can be run locally on-premises.

## Outposts Architecture

- **Outposts Racks in Customer Data Center:** Physical server racks owned, managed, and installed by AWS within the customer's physical location.
- **Extension of AWS Regions:** Outposts are an extension of an AWS Region. You choose a parent AWS Region when ordering an Outpost.
- **Connectivity to AWS Region:** Outposts require a connection back to the parent AWS Region for management, control plane functions, and access to the full range of AWS services.

## Customer Responsibilities

- **Physical Security:** Customers are responsible for the physical security and environmental conditions (power, cooling, networking) of the Outposts racks within their data center.

## Benefits of Using Outposts

- **Low Latency Access to On-Premises Systems:** Enables workloads that require very low latency to interact with local on-premises systems, databases, or equipment.
- **Local Data Processing:** Allows processing of sensitive data locally on-premises, ensuring it never leaves the customer's environment.
- **Data Residency:** Helps meet regulatory or compliance requirements for data to reside within specific geographic boundaries or the customer's own data center.
- **Simplified Migration:** Facilitates a phased migration strategy from on-premises to Outposts and then, when ready, from Outposts to the AWS cloud, using consistent tools and processes.
- **Fully Managed Service:** AWS handles the installation, monitoring, patching, and upgrades of the Outposts infrastructure.
- **Extensive Service Support (Current):** A growing number of AWS services can be run on Outposts, including:
    - Amazon EC2
    - Amazon EBS
    - Amazon S3 (via S3 Outposts)
    - Amazon EKS (for Kubernetes)
    - Amazon ECS (for containers)
    - Amazon RDS (relational databases)
    - Amazon EMR (for big data processing)

## Amazon S3 on AWS Outposts (Example)

- **Local Object Storage:** S3 on Outposts allows you to use the S3 APIs to store and retrieve data locally on your Outposts rack.
- **Reduced Data Transfers:** Keeps data close to on-premises applications, minimizing the need to transfer large datasets to AWS regions.
- **S3 Outposts Storage Class:** A specific S3 storage class designed for use on Outposts.
- **Default Encryption:** Data stored on S3 Outposts is encrypted by default using SSE-S3.

### Accessing Data on S3 Outposts

1. **S3 Access Points:** You can create S3 Access Points on your S3 Outposts to manage security and provide granular access control for EC2 instances within your VPC to the local S3 storage.
2. **DataSync for Cloud Synchronization:** AWS DataSync can be used to synchronize data between your S3 on Outposts and a standard Amazon S3 bucket in the cloud for backup, DR, or access from cloud-based applications.

AWS Outposts represents a significant step in bridging the gap between on-premises infrastructure and the AWS cloud, offering a truly consistent hybrid cloud experience for organizations with specific on-premises requirements.