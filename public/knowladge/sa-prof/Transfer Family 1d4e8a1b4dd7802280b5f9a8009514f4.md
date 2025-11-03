# Transfer Family

# AWS Transfer Family

## Purpose and Goals

- Enables secure file transfers into and out of Amazon S3 or Amazon EFS using standard protocols.
- Provides an alternative to using S3 APIs or mounting EFS directly.

## Key Concepts

- **Protocol Support:**
    - **FTP (File Transfer Protocol):** Unencrypted.
    - **FTPS (File Transfer Protocol over SSL):** Encrypted in transit.
    - **SFTP (Secure File Transfer Protocol):** Encrypted in transit.
- **Destinations:** Supports transferring files to and from Amazon S3 and Amazon EFS.
- **Fully Managed Infrastructure:** AWS handles scaling, reliability, and high availability.
- **Pricing:** Pay per provisioned endpoint per hour and per GB of data transferred in/out.
- **User Credential Management:**
    - Stored and managed within the Transfer Family service.
    - Integration with external authentication systems: Microsoft Active Directory, LDAP, Okta, Amazon Cognito, custom sources.
- **Use Cases:** File sharing, sharing public datasets, CRM, ERP integrations, etc.

## Architecture

- Users access Transfer Family endpoints using standard FTP clients.
- **Optional DNS (Route 53):** Allows using custom hostnames for the FTP service.
- **IAM Role:** The Transfer Family service assumes an IAM Role to access S3 or EFS for file transfers.
- **Security:** Can be enhanced by integrating with external authentication systems.

## Endpoint Types and Security

- **Public Endpoint:**
    - Endpoint in the AWS cloud with a public DNS name.
    - Public IP address managed by AWS (can change over time - use DNS name).
    - **Security:** Security is managed within the endpoint itself. Cannot use source IP address allow lists in network security groups or NACLs.
- **VPC Endpoint (Internal Access):**
    - Deployed within your VPC.
    - EC2 instances within the VPC can access it privately.
    - Corporate Data Centers (via VPN or Direct Connect) can also access it privately.
    - **Security:** Provides static private IPs. Allows setting up allow lists using Security Groups and Network ACLs to control access to the endpoint.
- **VPC Endpoint (Internet-Facing Access):**
    - Deployed within your VPC.
    - Allows private access from within the VPC and connected networks.
    - Supports attaching an Elastic IP address for public internet access.
    - **Security:** Full control over the Elastic IP. Allows setting up Security Groups to control who from the internet can access the endpoint.

## Key Takeaways for the Exam

- Understand the three supported protocols (FTP, FTPS, SFTP) and their encryption status.
- Know that Transfer Family facilitates file transfers to/from S3 and EFS using these protocols.
- Be aware of the pricing model.
- Recognize the different options for managing user credentials.
- **Crucially, understand the three Endpoint Types and their security implications:**
    - **Public:** Public DNS, dynamic AWS-managed IP, no source IP filtering at network level.
    - **VPC Internal:** Private IPs within your VPC, allows network-level source IP filtering.
    - **VPC Internet-Facing:** Private access + public access via Elastic IP (customer-controlled), allows network-level source IP filtering for public access.
- The exam will likely ask you to choose the appropriate endpoint type based on specific security and access requirements.