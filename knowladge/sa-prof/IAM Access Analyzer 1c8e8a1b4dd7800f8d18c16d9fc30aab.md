# IAM Access Analyzer

**IAM Access Analyzer: Key Concepts**

![image.png](image.png)

- **Purpose:**
    - Identifies resources shared externally, highlighting potential security risks.
    - Analyzes resource policies to detect unintended external access.
- **Scope:**
    - Covers resources like S3 buckets, IAM roles, KMS keys, Lambda functions and layers, SQS queues, and Secrets Manager secrets.
- **Zone of Trust:**
    - Defines trusted AWS accounts or organizations.
    - Flags any external access outside this zone as a "finding."
- **External Sharing Detection:**
    - Analyzes resource policies that grant access to external entities (accounts, users, IPs, etc.).
    - Alerts on access that deviates from the defined zone of trust.
- **Policy Validation:**
    - Validates IAM policies against grammar and best practices.
    - Provides warnings, errors, and recommendations for policy improvement.
- **Policy Generation:**
    - Generates IAM policies based on CloudTrail logs (up to 90 days).
    - Creates fine-grained permissions tailored to actual access activity.
    - This helps create least privilege policies.
- **Workflow:**
    - CloudTrail logs are analyzed by IAM Access Analyzer.
    - Policies are generated reflecting observed API calls.
- **Benefits:**
    - Reduces the risk of unintended external access.
    - Enhances security posture through policy validation and generation.
    - Simplifies the creation of least privilege IAM policies.

**In essence:**

IAM Access Analyzer helps you understand who has access to your AWS resources, validates your IAM policies, and can even help you create better ones based on real-world usage.