# CloudTrail SA

# AWS Solution Architect Professional - CloudTrail Deep Dive

## CloudTrail to S3 Delivery

- **CloudTrail to S3:**
    - CloudTrail files can be delivered to S3 every 5 minutes.
    - Encryption:
        - Default: SSE-S3.
        - Custom: SSE-KMS.
    - Lifecycle Policies:
        - Move archived logs to Glacier for cost savings.
    - S3 Events:
        - Trigger SQS, SNS, or Lambda on file delivery.
    - CloudTrail can deliver notifications directly to SNS.
- **S3 Enhancements:**
    - Versioning: Prevent accidental deletions.
    - MFA Delete: Protect against unauthorized deletions.
    - Lifecycle Policies: Transition to S3 IA or Glacier.
    - Object Lock: Ensure immutability.
    - Encryption: SSE-S3 or SSE-KMS.
    - Log File Integrity Validation: Verify file integrity.
- **Use Cases:**
    - Combining CloudTrail with S3 and notifications enables various audit and security use cases.

## Multi-Account, Multi-Region CloudTrail

![image.png](image%204.png)

- **Centralized Logging:**
    - Use a security account to aggregate CloudTrail logs from multiple accounts.
    - CloudTrail in each account (Account A, Account B) delivers logs to the security account's S3 bucket.
- **S3 Bucket Policies:**
    - Required for cross-account log delivery.
    - Allows CloudTrail to write logs to the security account's S3 bucket.
- **Access Control:**
    - Cross-account roles: Allow other accounts to access logs in the security account.
    - S3 bucket policy modifications: Grant read access to specific accounts.
- **Security Benefits:**
    - Centralized security management.
    - Ensured log integrity in a secure environment.

## Alerting on API Calls with CloudTrail and CloudWatch Logs

![image.png](image%205.png)

- **CloudTrail to CloudWatch Logs:**
    - Stream CloudTrail events to CloudWatch Logs.
- **Metric Filters and Alarms:**
    - Create metric filters to detect specific API calls (e.g., terminate instance).
    - Set up CloudWatch alarms to trigger on metric filter matches.
    - Cloudwatch alarms can send notifications to SNS.
- **Use Cases:**
    - Alert on specific API calls.
    - Detect high API call volumes.
    - Monitor denied API calls for security threats.

## Organizational Trail

![image.png](image%206.png)

- **AWS Organizations Integration:**
    - Create an organizational trail in the management account.
    - Monitors all member accounts within the organization.
- **Centralized Log Storage:**
    - Logs are stored in an S3 bucket within the management account.
    - S3 prefixes indicate the originating account.
- **Management Account Responsibility:**
    - The organizational trail is created and managed within the management account.

## CloudTrail Event Reaction Times and Use Cases

- **EventBridge:**
    - Fastest response to CloudTrail events.
    - Triggered by any API call.
    - Ideal for real-time event processing.
- **CloudWatch Logs:**
    - Near real-time streaming.
    - Metric filters for anomaly detection and event counting.
    - Suitable for security monitoring and alerting.
- **Amazon S3:**
    - Log delivery every 5 minutes.
    - Long-term storage and analytics.
    - Cross-account delivery and integrity validation.
    - Good for large scale analysis.

## Summary of CloudTrail Delivery options.

- **EventBridge:** Real Time API call reaction.
- **CloudWatch Logs:** Anomaly detection and event counting.
- **Amazon S3:** Long term storage and large scale analytics.