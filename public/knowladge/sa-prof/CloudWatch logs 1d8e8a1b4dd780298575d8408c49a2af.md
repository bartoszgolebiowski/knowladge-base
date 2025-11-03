# CloudWatch logs

**Getting Data into CloudWatch Logs:**

- **Agents:**
    - **CloudWatch Logs Agent (Legacy):** A standalone agent specifically designed to push log files to CloudWatch Logs. Needs to be installed and configured on each instance.
    - **CloudWatch Unified Agent:** The more modern and recommended agent. It can collect both logs and metrics from EC2 instances and on-premises servers. It offers more flexibility and features.
    - **SDK:** Allows programmatic pushing of log events from your applications.
- **AWS Service Integrations:** These are direct and often require minimal configuration:
    - **Elastic Beanstalk:** Simplifies log collection from application environments.
    - **ECS:** Provides log drivers (e.g., `awslogs`) to send container logs.
    - **Lambda:** Automatically sends function logs (including `print()` statements) to CloudWatch Logs.
    - **VPC Flow Logs:** Captures information about IP traffic going to and from network interfaces in your VPC.
    - **API Gateway Access Logs:** Records requests made to your APIs.
    - **CloudTrail:** Audit logs of actions taken in your AWS account (can be filtered to send specific events).
    - **Route 53 Query Logs:** Provides detailed information about DNS queries received by Route 53.
- **On-premises Servers:** The CloudWatch Logs Agent and Unified Agent can be installed on any server with network access to AWS.

**CloudWatch Logs Structure and Configuration:**

- **Log Groups:** Logical groupings of log streams, often representing an application or service. You define the names.
- **Log Streams:** Sequences of log events originating from a specific source (e.g., an instance, a container). The naming within a log group is often managed by the service or agent.
- **Log Events:** Individual records within a log stream, typically containing a timestamp and a message.
- **Log Expiration Policies:** Crucial for managing storage costs. You can set retention periods (e.g., 1 day, 7 days, 1 month, never expire). Remember to plan for archiving if you need logs beyond the retention period.
- **KMS Encryption:** Important for securing sensitive log data at rest within CloudWatch Logs. You can use AWS-managed KMS keys or your own Customer Managed Keys (CMK) for more control.

**Exporting CloudWatch Logs:**

- **Amazon S3 Exports:**
    - A manual, point-in-time operation using the `CreateExportTask` API.
    - Logs are encrypted during export (SSE-S3 or SSE-KMS required).
    - **Not real-time**; data can take up to 12 hours to become available.
    - Useful for long-term archival and batch analysis with other tools.
- **CloudWatch Logs Subscriptions:** Provide a **near real-time** stream of log events to various destinations based on defined filters.
    - **AWS Lambda:** Allows for real-time processing and transformation of log events. AWS provides a managed Lambda function for sending to Amazon Elasticsearch Service (now OpenSearch Service). You can also write your own Lambda functions for custom processing or routing.
    - **Kinesis Data Firehose:** Enables near real-time delivery of log data to:
        - **Amazon S3:** For archival and batch processing.
        - **Amazon OpenSearch Service:** For real-time log analytics and visualization.
        - **Splunk:** For integration with existing Splunk deployments.
        - **Redshift:** For data warehousing and analysis.
    - **Kinesis Data Streams:** Provides a highly scalable and durable real-time data streaming platform. You can then use other Kinesis services (Firehose, Analytics) or your own consumers (e.g., EC2 instances with KCL, Lambda) to process the data.

**CloudWatch Logs Metric Filters and Insights:**

- **Metric Filters:**
    - Allow you to define patterns to search for within log events.
    - When a match is found, a CloudWatch metric is incremented based on the filter configuration.
    - Useful for tracking specific events (e.g., errors, specific user actions, security-related events).
    - These metrics can then be used to create CloudWatch Alarms for automated responses.
- **CloudWatch Logs Insights:**
    - A powerful query engine that allows you to interactively analyze your log data directly within CloudWatch.
    - Uses a structured query language.
    - Enables you to perform complex analysis, identify trends, and troubleshoot issues.
    - You can save queries and add their results to CloudWatch Dashboards for continuous monitoring.
    - Provides built-in query examples for common use cases (Lambda, VPC Flow Logs, etc.).

**Multi-Account and Multi-Region Log Aggregation:**

- A crucial architecture for centralized monitoring and security analysis.
- Typically involves sending logs from multiple accounts and regions to a central logging account.
- **Kinesis Data Streams** is often used as the intermediary in the central logging account to receive logs from various sources.
- From the central Kinesis Data Stream, you can then use **Kinesis Data Firehose** to deliver logs to a central S3 bucket for archival or to a central OpenSearch Service cluster for analysis.
- This architecture simplifies management, improves security visibility, and facilitates compliance efforts.

**CloudWatch Agent and Systems Manager Integration:**

- **SSM Run Command:** A convenient way to remotely install and configure the CloudWatch Agent on multiple EC2 instances simultaneously.
- **SSM State Manager:** Allows you to define and maintain a desired state for your EC2 instances, ensuring the CloudWatch Agent is always installed and running.
- **SSM Parameter Store:** You can store the CloudWatch Agent configuration in Parameter Store, allowing instances to retrieve their configuration securely and centrally. This simplifies management and ensures consistent configuration across your fleet.

**Key Considerations for the SA Pro Exam:**

- Understand the different ways to get logs into CloudWatch Logs and when to choose each method.
- Be familiar with the structure of CloudWatch Logs (Log Groups, Log Streams, Log Events).
- Know the implications of log expiration policies and the need for archival.
- Deeply understand CloudWatch Logs Metric Filters and how they can be used to create alarms.
- Master CloudWatch Logs Insights and its querying capabilities.
- Thoroughly understand CloudWatch Logs Subscriptions and the different destination options (Lambda, Kinesis Data Firehose, Kinesis Data Streams) and their respective use cases and real-time vs. near real-time characteristics.
- Be able to design and explain multi-account and multi-region logging architectures.
- Understand the integration between the CloudWatch Agent and Systems Manager for simplified deployment and management.
- Be aware of encryption options for CloudWatch Logs (at rest and during export).