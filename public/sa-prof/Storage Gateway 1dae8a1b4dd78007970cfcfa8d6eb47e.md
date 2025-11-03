# Storage Gateway

Alright, let's dive into AWS Storage Gateway and how it bridges your on-premises world with the AWS cloud. Here's a breakdown in markdown format:

## **AWS Storage Gateway: Bridging On-Premises and AWS Cloud Storage**

AWS Storage Gateway is a hybrid cloud service that connects your on-premises applications to AWS cloud storage.**1** It enables seamless and secure integration between your local environment and AWS storage services like S3, FSx for Windows File Server, EBS, and Glacier.**2**

**Key Use Cases:**

- **Disaster Recovery:** Backing up on-premises data to the cloud for recovery purposes.
- **Backup and Restore:** Facilitating cloud migration or extending on-premises storage to AWS.
- **Tiered Storage:** Utilizing AWS for colder, less frequently accessed data while keeping frequently used data on-premises.
- **On-Premises Cache:** Caching frequently accessed data locally for low-latency access while the bulk of the data resides in AWS.

**Types of Storage Gateway:**

There are four main types of Storage Gateway, each catering to different storage needs:

### **1. Amazon S3 File Gateway**

- **Purpose:** Provides on-premises applications with file-based access to Amazon S3 buckets using standard NFS (Network File System) or SMB (Server Message Block) protocols.
- **How it works:** The gateway translates file system operations into S3 object requests (HTTPS). To the application server, it appears as a regular file share.
- **S3 Compatibility:** Supports various S3 storage classes (Standard, IA, One Zone-IA, Intelligent-Tiering) but not Glacier directly. However, lifecycle policies can be used to archive objects to Glacier.
- **Caching:** Frequently used data is cached locally on the gateway for faster access.
- **Security:** Requires IAM roles for each file gateway to access the S3 bucket. Supports Active Directory integration for SMB user authentication.
- **Use Case:** Exposing S3 objects to on-premises application servers that require file protocol access.

### **2. Amazon FSx File Gateway**

- **Purpose:** Enables low-latency, local access to Amazon FSx for Windows File Server file systems from on-premises SMB clients.
- **Benefit:** Provides a local cache of frequently accessed data, improving performance for on-premises users accessing the FSx file share.
- **Native Compatibility:** Offers Windows and native file system compatibility (SMB, NTFS) and integrates with Active Directory.
- **Use Case:** Group file shares and home directories that need to be accessed with low latency from on-premises while being managed by Amazon FSx for Windows File Server.

### **3. Volume Gateway**

- **Purpose:** Presents block storage volumes to on-premises application servers using the iSCSI protocol, with the backend storage in Amazon S3.
- **Backup Mechanism:** Volumes are backed up as EBS snapshots stored in S3, allowing for restoration of on-premises volumes or creation of new EBS volumes in AWS.
- **Types of Volume Gateway:**
    - **Cached Volumes:** Frequently accessed data is cached locally for low latency, while the entire dataset is stored in S3.
    - **Stored Volumes:** The entire dataset resides on-premises, with asynchronous backups taken to Amazon S3 on a scheduled basis.
- **Use Case:** Backing up on-premises server volumes to AWS for disaster recovery and restore scenarios.

### **4. Tape Gateway**

- **Purpose:** Provides a virtual tape library (VTL) in the cloud, backed by Amazon S3 and Glacier, for companies still using tape backup systems.
- **Integration:** Works with leading backup software vendors using the iSCSI interface.
- **Storage Tiers:** Virtual tapes are initially stored in S3 and can be archived to Glacier and Glacier Deep Archive for long-term, cost-effective storage.
- **Use Case:** Replacing or augmenting physical tape backup infrastructure with a cloud-based solution for archiving data.

**Deployment Options:**

- **Virtual Machine (VM):** Storage Gateway is typically deployed as a VM on your on-premises infrastructure (e.g., VMware, Hyper-V).
- **Hardware Appliance:** AWS also offers a physical Storage Gateway Hardware Appliance for environments without existing virtualization infrastructure. This appliance comes pre-configured with the necessary CPU, memory, network, and SSD cache resources.

**Conceptual Architecture:**

The general architecture involves:

1. **On-Premises:** Deployment of a Storage Gateway (VM or hardware appliance).
2. **Storage Gateway Service:** The AWS service that manages the connection and data transfer between the on-premises gateway and AWS storage.
3. **AWS Cloud:** The target AWS storage services (S3, FSx, EBS, Glacier).

**Summary Table:**

| **Gateway Type** | **Protocol** | **Backend Storage in AWS** | **Primary Use Case** |
| --- | --- | --- | --- |
| **S3 File Gateway** | NFS, SMB | Amazon S3 | File-based access to S3 for on-premises applications. |
| **FSx File Gateway** | SMB | Amazon FSx for Windows File Server | Low-latency on-premises access to FSx for Windows File Server file shares. |
| **Volume Gateway** | iSCSI | Amazon S3 (backed by EBS snapshots) | Block-level storage and backup of on-premises volumes to AWS. |
| **Tape Gateway** | iSCSI VTL | Amazon S3, Glacier | Cloud-based virtual tape library for backup and archival. |

Understanding the different types of Storage Gateway and their respective use cases is crucial for designing hybrid cloud solutions on AWS and is a likely topic for the AWS Solution Architect Professional exam.