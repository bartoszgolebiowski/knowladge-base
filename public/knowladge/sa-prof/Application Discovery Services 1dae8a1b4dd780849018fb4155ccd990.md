# Application Discovery Services

Alright, let's consolidate this valuable information about AWS services for on-premises migration. Here's a structured overview in markdown format:

## **AWS Services for On-Premises Migration**

AWS provides a suite of services to aid organizations in planning, executing, and ensuring resilience during and after migrating workloads from on-premises environments to the AWS Cloud.

**1. AWS Application Discovery Service (ADS)**

- **Purpose:** Helps plan migration projects by gathering information about on-premises data centers.
- **Key Functions:**
    - Tracks server utilization data (CPU, memory, disk).
    - Maps application dependencies between servers.
- **Discovery Methods:**
    - **Agentless Discovery (Application Discovery Agentless Connector):** Deployed as an OVA on VMware hosts. Inventories virtual machines, their configuration, and performance history. Works with any OS.
    - **Agent-Based Discovery:** Agents deployed on individual servers (Windows, Linux). Gathers system configuration, performance, running processes, and detailed network connections. Provides a comprehensive map of server communication.
- **Output and Integration:**
    - Data can be exported as CSV.
    - Viewable and tracked within **AWS Migration Hub**.
    - Queryable using **Amazon Athena**.
    - Can be integrated with **AWS QuickSight** for visualization.
    - Supports uploading additional data sources like CMDB exports for enhanced analysis in Athena.

**2. AWS Application Migration Service (MGN)**

- **Evolution:** Replaces AWS Server Migration Service (SMS) and the original CloudEndure Migration service.
- **Purpose:** Simplifies "lift and shift" (re-host) migrations of applications to AWS.
- **Functionality:** Converts physical, virtual, or cloud-based servers to run natively on AWS.
- **Process:**
    1. Create a staging environment in AWS (EC2 instances and EBS volumes).
    2. Install a replication agent on the source server.
    3. The agent continuously replicates data to the staging environment.
    4. Perform a cutover to a production-ready EC2 instance and EBS volumes in AWS.
- **Benefits:** Supports a wide range of platforms, operating systems, and databases. Offers minimal downtime and reduced costs.

**3. AWS Elastic Disaster Recovery (DRS)**

- **Evolution:** Renamed from CloudEndure Disaster Recovery.
- **Purpose:** Provides a way to quickly and easily recover physical, virtual, or cloud-based servers into AWS for disaster recovery.
- **Use Cases:** Protecting critical databases (Oracle, MySQL, SQL Server), enterprise applications (SAP), and mitigating ransomware attacks.
- **Functionality:** Continuous, block-level replication of servers into the AWS cloud.
- **Process:**
    1. Install a replication agent on the source server.
    2. Data is replicated in near real-time to a recovery environment in AWS.
    3. Perform a failover within minutes to create a full production environment in AWS.
    4. Offers a failback mechanism to the original environment when it's available.
- **Architecture:** Similar to MGN, leveraging the same backend technology.

**4. Amazon Linux 2 AMI as a Virtual Machine**

- AWS provides the Amazon Linux 2 AMI in ISO format, allowing it to be run as a virtual machine on various hypervisors (VMware, KVM, VirtualBox, Hyper-V). This can be useful for testing or development purposes in a local environment that mirrors the AWS environment.

**5. AWS Migration Hub**

- **Purpose:** A central location to track the progress of your migration portfolio across multiple AWS and partner tools.
- Integrates with services like ADS and MGN to provide a unified view of your migration activities.

**6. AWS Database Migration Service (DMS)**

- **Purpose:** Replicates databases to AWS (or from AWS to AWS, or AWS to on-premises).
- **Scope:** Specifically for database migration and continuous replication.
- **Supported Databases:** Oracle, MySQL, SQL Server, DynamoDB, and many others.

In summary, AWS offers a comprehensive set of tools to support every stage of the on-premises migration journey, from discovery and planning to the actual migration and ensuring business continuity through disaster recovery. Understanding the purpose and capabilities of each of these services is crucial for designing effective migration strategies on AWS.