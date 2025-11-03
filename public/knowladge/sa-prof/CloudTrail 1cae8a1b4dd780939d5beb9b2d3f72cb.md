# CloudTrail

## AWS CloudTrail

**Purpose:**

- Provides governance, compliance, and audit capabilities for AWS accounts.
- Records a history of events and API calls made within AWS accounts.

**Key Features:**

- **Enabled by Default:** CloudTrail is automatically enabled for all AWS accounts.
- **Event Logging:** Logs events from:
    - AWS Management Console
    - AWS SDK
    - AWS CLI
    - Other AWS services
- **Log Destination:**
    - Logs can be stored in CloudWatch Logs or Amazon S3.
- **Trail Configuration:**
    - Trails can be applied to all regions or a single region.
    - Useful for aggregating event history from multiple regions into a single S3 bucket.

**Use Cases:**

- Auditing and investigating actions within AWS accounts.
- Example: Determining who terminated an EC2 instance.

**Event Types:**

1. **Management Events:**
    - Represent operations performed on resources in AWS accounts.
    - Examples:
        - Configuring security (IAM AttachRolePolicy)
        - Creating a subnet
        - Setting up logging
    - Logged by default.
    - Subcategories:
        - **Read Events:** Do not modify resources (e.g., listing IAM users, EC2 instances).
        - **Write Events:** Modify resources (e.g., deleting a DynamoDB table).
        - Write Events are generally considered more critical due to their potential impact.
2. **Data Events:**
    - Record data operations.
    - Not logged by default due to high volume.
    - Examples:
        - Amazon S3 object-level activity (GetObject, DeleteObject, PutObject)
        - AWS Lambda function execution activity (Invoke API)
    - Subcategories (for S3):
        - Read Event: GetObject
        - Write Events: DeleteObject, PutObject
3. **CloudTrail Insights Events:**
    - Detect unusual activity in AWS accounts.
    - Requires enabling and incurs additional costs.
    - Analyzes Management Events to identify anomalies.
    - Examples of detected anomalies:
        - Inaccurate resource provisioning
        - Hitting service limits
        - Bursts of AWS IAM actions
        - Gaps in periodic maintenance activity
    - Output:
        - Insights Events in the CloudTrail console
        - Optional: Amazon S3, EventBridge Events (for automation, e.g., email notifications)

**Event Retention:**

- Default retention: 90 days in CloudTrail.
- Long-term retention:
    - Store logs in Amazon S3.
    - Use Amazon Athena to analyze logs in S3.

**Workflow:**

1. Management Events, Data Events, and Insights Events are recorded in CloudTrail (90-day retention).
2. For longer retention, logs are sent to S3.
3. Athena is used to query and analyze logs in S3.