# GuardDuty

## **How GuardDuty Works:**

- **Intelligent Analysis:** Utilizes machine learning algorithms, anomaly detection, and third-party threat intelligence data.
- **Easy Enablement:** Can be enabled with a single click.
- **Free Trial:** Offers a 30-day free trial period.
- **No Software Installation:** It's a fully managed service, requiring no software deployment.

## **Input Data Sources:**

![image.png](image%2013.png)

GuardDuty analyzes various data sources to identify potential threats:**5**

**Always Analyzed:**

- **CloudTrail Event Logs:** Monitors management and data events for unusual API calls and unauthorized deployments.
    - **Management Events:** Examples include `CreateVPC`, `CreateSubnet`, etc.
    - **S3 Data Events:** Examples include `GetObject`, `ListObjects`, `DeleteObject`, etc.
- **VPC Flow Logs:** Examines network traffic for unusual patterns and suspicious IP addresses.
- **DNS Logs:** Detects potentially compromised EC2 instances sending encoded data within DNS queries.

**Optional Features (Can be Enabled):**

- **EKS Audit Logs:** Monitors Kubernetes API server activity for suspicious actions.
- **RDS and Aurora Login Events:** Analyzes database login attempts for unusual patterns.
- **EBS Volume Data:** Inspects EBS volume snapshots for potential malware or sensitive data exposure.
- **Lambda Network Activity:** Monitors network traffic originating from or destined for Lambda functions.
- **S3 Data Events:** Provides deeper analysis of S3 object access patterns.
- **EKS Runtime Monitoring:** Detects threats within container workloads at runtime.

## **Findings and Automation:**

- **Findings Generation:** When GuardDuty detects a potential threat based on its analysis, it generates a finding.
- **Amazon EventBridge Integration:** Findings automatically create events in Amazon EventBridge.
- **Automated Responses:** EventBridge rules can be configured to trigger automated actions based on GuardDuty findings, such as:
    - Invoking AWS Lambda functions.
    - Sending notifications via Amazon SNS topics.
    - Targeting any other service supported by EventBridge.

## **Cryptocurrency Attack Detection:**

- GuardDuty has specific logic and dedicated findings to detect cryptocurrency-related attacks.

## **Delegated Administrator for AWS Organizations:**

![image.png](image%2014.png)

- **Centralized Management:** In an AWS Organization, a member account can be designated as the GuardDuty Delegated Administrator.
- **Organization-Wide Control:** This designated account has full permissions to enable and manage GuardDuty across all accounts within the Organization.
- **Management Account Configuration:** The designation of the Delegated Administrator can only be done through the Organization's Management Account.