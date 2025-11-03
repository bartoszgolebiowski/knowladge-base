# S3 Security

## **S3 Encryption**

- **SSE-S3 (Server-Side Encryption with Amazon S3-Managed Keys):**
    - Encrypts S3 objects using keys handled and managed by AWS.
    - Simplest server-side encryption option.
- **SSE-KMS (Server-Side Encryption with AWS KMS-Managed Keys):**
    - Leverages AWS Key Management Service (KMS) to manage encryption keys.
    - **Benefits:**
        - **Auditing:** Every API call using SSE-KMS appears in KMS and CloudTrail for audit purposes.
        - **Enhanced Security for Public Buckets:** Even if a bucket or object is public, SSE-KMS encryption prevents anonymous users from reading it as they lack access to the KMS key.
    - **IAM Permissions:** Requires `kms:GenerateDataKey` permission for uploading objects with SSE-KMS.
- **SSE-C (Server-Side Encryption with Customer-Provided Keys):**
    - You manage your own encryption keys and pass them to Amazon S3 for server-side encryption.
- **Client-Side Encryption:**
    - You manage your own encryption keys and perform the encryption on the client side before uploading to S3.
    - Decryption also happens client-side.
- **Glacier Encryption:**
    - All data in Glacier is automatically encrypted using AES-256 with AWS-managed keys.

## **Encryption in Transit**

- Amazon S3 exposes two endpoints:
    - **HTTP:** Non-encrypted (not the default).
    - **HTTPS:** Encrypted using SSL/TLS certificates (default).
- **Recommendation:** Always use HTTPS for secure data transfer.
- **Requirement:** HTTPS is mandatory when using the SSE-C encryption scheme.
- **Forcing HTTPS:** Use a bucket policy with the `aws:SecureTransport` condition to mandate HTTPS for all requests to the bucket.

## **S3 Events**

- **S3 Access Logs:**
    - Provide detailed records of all requests made to a bucket.
    - Delivery can take hours.
    - Delivered to another S3 bucket.
    - "Best effort" delivery, may be incomplete.
    - Valuable for understanding access patterns.
- **S3 Event Notifications:**
    - Send notifications when specific events occur in a bucket.
    - **Trigger Events:** Object creation, removal, restoration, replication events.
    - **Destinations:** SNS, SQS queue, Lambda.
    - Typically delivered within seconds (can take a minute or two).
    - A notification is sent for every object if versioning is enabled.
    - Without versioning, simultaneous writes to the same object might result in only one notification.
- **Trusted Advisor:**
    - Checks bucket permissions, helping identify publicly accessible buckets.
- **Amazon EventBridge:**
    - Requires enabling CloudTrail object-level logging on S3.
    - Can trigger targets like Lambda functions, SQS, SNS based on S3 events.

## **S3 Security - Securing a Bucket**

- **User-Based Security:**
    - **IAM Policies:** Attach policies to IAM users or groups to grant permissions to specific S3 buckets.
- **Resource-Based Security:**
    - **Bucket Policies:** Bucket-wide rules defined in the S3 console.
        - Crucial for cross-account access, allowing other AWS accounts to access the bucket without assuming roles and relinquishing their own permissions.
    - **Object ACLs (Access Control Lists):** Finer-grained control at the object level (less common, less emphasized in the exam).
    - **Bucket ACLs (Access Control Lists):** Bucket-level access control (less common, less emphasized in the exam).
- **Exam Focus:** Expect more questions on S3 bucket policies as the primary method for resource-based access control.

## **S3 Bucket Policies - Details**

- Use S3 bucket policies to:
    - Grant public access to the bucket.
    - Force objects to be encrypted at upload.
    - Grant cross-account access.
- **Conditions:** Allow you to control access based on various factors:
    - **`SourceIp`:** Condition based on the public or Elastic IP address of the requester.
    - **`VpcSourceIp`:** Condition based on the private IP address of the requester, **only when using a VPC endpoint.**
    - **`SourceVpc` or `SourceVpce`:** Condition based on the VPC ID or VPC endpoint ID. Useful for granting private access to S3 buckets only from specific VPCs or VPC endpoints (not based on IP addresses).
    - **`CloudFront Origin Identity`:** Condition to allow only a specific CloudFront distribution (with a defined origin identity) to access the S3 bucket.
    - **Multifactor Authentication:** Condition requiring MFA for access.
- **Recommendation:** Review example S3 bucket policies for a deeper understanding.

## **Pre-Signed URLs**

- Generated using the AWS SDK or CLI for both downloads (GET) and uploads (PUT).
- Signed with your IAM credentials.
- Anyone with the pre-signed URL has the exact permissions you had when creating it.
- **Validity:** Default of one hour, configurable using the `expires-in` argument.
- Users accessing the URL inherit the permissions of the URL creator (for GET or PUT actions).
- **Use Cases:**
    - Allowing logged-in users to download premium content on demand.
    - Dynamically granting access to a changing list of users for file downloads.
    - Providing temporary upload access to a specific location in a bucket without granting persistent permissions.

## **VPC Endpoint Gateway for S3**

- Provides private connectivity between your VPC and S3 without traversing the public internet.
- **Scenario 1: EC2 in a Public Subnet Accessing S3 (Public Access):**
    - EC2 instance with a public IP goes through an Internet Gateway to access the public S3 endpoint.
    - Bucket policy can use `AWS:SourceIP` condition based on the public or Elastic IP of the EC2 instance.
- **Scenario 2: EC2 in a Private Subnet Accessing S3:**
    - **Option 1 (Less Ideal):** Instance goes through a NAT Gateway in the public subnet, then through the Internet Gateway to the public S3 endpoint.
    - **Option 2 (Better):** Use a **VPC Endpoint Gateway for S3**.
        - Traffic remains entirely within the AWS network, ensuring private connectivity.
        - EC2 instances in the private subnet can directly access S3 through the VPC endpoint.
        - **Bucket Policy Conditions with VPC Endpoint:**
            - **`AWS:SourceVpce`:** Allows access only from specified VPC endpoint IDs.
            - **`AWS:SourceVpc`:** Allows access from all VPC endpoints within a specific VPC ID.
- **Key Takeaways for VPC Endpoints:**
    - `SourceIP`: For public IP-based restrictions.
    - `SourceVpc` / `SourceVpce`: For restricting access based on VPC or VPC endpoint when using private connectivity.

## **S3 Security - Object Lock and Glacier Vault Lock**

- Enable a **WORM (Write Once, Read Many)** model.
- **S3 Object Lock:**
    - Prevents deletion of an object version for a specified retention period.
    - Ensures data immutability for compliance and data retention requirements.
- **Glacier Vault Lock:**
    - Locks the vault policy, preventing future edits.
    - Ensures that any object placed in the Glacier vault can never be deleted.
    - Strong mechanism for demonstrating compliance to auditors.
- **Core Concept:** Write an object, lock it (either the object itself or the vault), and it cannot be deleted.

**Key Exam Preparation Points:**

- Pay close attention to the details discussed for each security mechanism.
- Understand the nuances of bucket policies and the different condition keys.
- Differentiate between public and private access scenarios and how VPC endpoints play a role.
- Grasp the purpose and functionality of Object Lock and Glacier Vault Lock for data immutability.