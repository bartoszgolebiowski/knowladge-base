# Backup

As an AWS Solution Architect Professional, let's detail how AWS Backup works specifically for Amazon EC2 instances:

AWS Backup provides a streamlined and centralized way to protect your EC2 instances by automating the creation and management of backups.**1** Here's a breakdown of the process:

**1. Resource Selection:**

- When configuring an AWS Backup Plan, you specify the EC2 instances you want to protect. You can do this in several ways:
    - **Instance ID:** Select individual EC2 instances by their unique identifier.
    - **Tags:** Define a tag-based policy where any EC2 instance with a specific tag (and value) will automatically be included in the backup plan. This is highly dynamic and recommended for managing backups at scale.
    - **Resource Groups:** Select an AWS Resource Group that contains your EC2 instances.

**2. Backup Plan Definition:**

- You define a **Backup Plan** that dictates the backup schedule, retention policy, and the target **Backup Vault** where the backups will be stored.
    - **Schedule:** You can set a recurring schedule (e.g., daily, weekly) or define a custom cron expression for more granular control over when backups are taken.
    - **Retention Policy:** You specify how long the backups should be retained (e.g., days, weeks, months, years, or indefinitely). AWS Backup automatically manages the lifecycle of your backups according to this policy.
    - **Backup Vault:** This is a secure, isolated storage container managed by AWS Backup where your EC2 backups (recovery points) are stored. You can have multiple Backup Vaults for different compliance or organizational needs
    - **Copy to Regions (Optional):** Within the Backup Plan, you can configure policies to automatically copy backups to another AWS Region for disaster recovery.

**3. Backup Execution:**

- Once the Backup Plan is associated with your EC2 instances, AWS Backup automatically initiates backups according to the defined schedule.
- For EC2 instances, AWS Backup primarily works by creating **Amazon Machine Images (AMIs)**. An AMI is a snapshot of your instance's root volume, configuration settings, and optionally, data volumes.
- During the backup process:
    - AWS Backup coordinates with the EC2 service to create an AMI of the selected instance(s).
    - If you've configured it, data volumes (EBS volumes attached to the instance) are also included in the AMI.
    - The resulting AMI is stored in the AWS Backup Vault.

**4. Backup Management:**

- AWS Backup provides a central console to monitor the status of your backup jobs (creating, completed, failed).
- You can view your recovery points (AMIs created by AWS Backup) within the Backup Vault
- AWS Backup handles the retention of these recovery points based on your defined policy, automatically deleting them when they expire.

**5. Restore Process:**

- When you need to restore an EC2 instance from an AWS Backup recovery point:
    - You select the desired recovery point from the AWS Backup console or using the AWS CLI/SDK.
    - AWS Backup uses the stored AMI to launch a new EC2 instance.
    - You can configure various restore options, such as the instance type, VPC, subnet, and security groups for the restored instance.
    - AWS Backup ensures that the restored instance retains the original configuration (within the limitations mentioned in the AWS documentation, such as the key pair).

**Key Considerations for EC2 Backups with AWS Backup:**

- **Consistency:** AWS Backup strives for application-consistent backups. For databases and other stateful applications, it's often recommended to use pre- and post-backup scripts (configured within the Backup Plan) to ensure data integrity during the snapshot process.
- **Cost:** You are charged for the storage used in the Backup Vault and any cross-region data transfer if you are copying backups to another region.
- **IAM Permissions:** AWS Backup uses IAM roles to access your EC2 resources and perform backup and restore operations. Ensure the necessary permissions are in place.
- **User Data:** AWS Backup does not automatically back up user data that is used during the initial launch of an EC2 instance. If this is critical, you might need to include it in the instance volumes or handle it separately.

In summary, AWS Backup simplifies EC2 backup management by providing a policy-driven approach to automatically create and retain AMIs, offering a reliable solution for recovery and disaster recovery scenarios.