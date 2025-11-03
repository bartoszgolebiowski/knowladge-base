# AWS Directory Services

## **Microsoft Active Directory (AD)**

- **Function:**
    - Centralized database of objects (users, computers, printers, file shares, security groups).
    - Provides centralized security management for Microsoft environments.
- **Organization:**
    - Objects are grouped into trees.
    - A collection of trees forms a forest.
- **Domain Controller:**
    - Stores user credentials and authenticates users across connected machines.
    - Enables synchronized logins.
- **ADFS (Active Directory Federation Services):**
    - Provides Single-Sign-On (SSO) across applications.
    - Uses SAML for authentication with third-party applications (e.g., Console, Dropbox, Office 365).
    - Authentication flow: User accesses URL, is authenticated against AD, receives SAML token, and exchanges it with AWS for console sign-in.

## **AWS Directory Services**

AWS offers three managed directory services:

### **1. AWS Managed Microsoft AD**

- **Function:**
    - Microsoft AD in the AWS cloud.
    - Allows local user management in AWS.
    - Supports MFA.
    - Requires a trust relationship with on-premises AD for connectivity.
- **Architecture:**
    - Deployed in a VPC across multiple Availability Zones (AZs) for high availability.
    - Supports seamless domain join for EC2 instances.
    - Integrates with AWS services like RDS for SQL Server, WorkSpaces, and QuickSight.
    - Can be standalone or joined to on-premise AD.
    - Supports automated backups and multi-region replication.
- **Integration:**
    - Two-way forest trust with on-premises AD (requires Direct Connect or VPN).
    - Integrates with RDS for SQL Server, WorkSpaces, QuickSight, Connect, WorkDocs, and SSO.
    - Supports traditional AD applications (e.g., .NET, SharePoint, SQL Server).
- **Trust Relationship:**
    - Requires Direct Connect or VPN connection to on-premises AD.
    - Supports one-way and two-way forest trusts.
    - Forest trust is not replication; users are managed independently.
    - Solution Architecture can include EC2 windows instances to replicate on premise AD, for DR or latency reduction.

### **2. AD Connector**

- **Function:**
    - Proxy service to connect AWS applications to on-premises AD.
    - No caching capability.
    - Users are managed solely on-premises.
    - Supports MFA.
    - Requires VPN or Direct connect.
- **Architecture:**
    - Acts as a gateway for authentication requests.
    - Does not integrate with services like RDS for SQL Server or provide seamless domain join.
    - Relies on continuous connectivity to on-premises AD.
- **Authentication Flow:**
    - User provides credentials via a custom sign-in page.
    - AD Connector proxies the request to on-premises AD for LDAP authentication.
    - AD Connector performs STS AssumeRole to provide temporary AWS credentials.

### **3. Simple AD**

- **Function:**
    - Inexpensive, basic AD-compatible service.
    - Powered by Samba 4.
    - Suitable for small user bases (500-5,000 users).
- **Limitations:**
    - Does not support MFA.
    - Does not integrate with RDS for SQL Server or SSO.
    - Cannot be joined with on-premises AD.
    - Limited AD features and LDAP compatibility.
- **Use Cases:**
    - Lower-cost alternative for basic AD functionality.

## **Key Differences Summary**

- **AWS Managed Microsoft AD:**
    - Full Microsoft AD in AWS.
    - Highest level of integration.
    - Supports trust relationships.
- **AD Connector:**
    - Proxy to on-premises AD.
    - Relies on connectivity.
    - no user managment inside of the aws cloud.
- **Simple AD:**
    - Basic, inexpensive AD-compatible service.
    - Limited functionality.
    - No trust relationships.

These notes should provide a solid overview of Microsoft AD and AWS Directory Services for the AWS Solution Architect Professional exam.