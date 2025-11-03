# Budget & Cost Explorer

## AWS Cost Management Tools: Budgets and Cost Explorer

This lecture covered two key AWS services for managing and understanding your cloud costs: AWS Budgets and AWS Cost Explorer. Understanding these tools is essential for the AWS Solution Architect Professional exam.

### AWS Budgets

AWS Budgets allows you to set custom budgets to track your AWS costs, usage, RI utilization, and Savings Plans. You can configure alarms to be notified when your actual or forecasted costs exceed your budget thresholds.

- **Budget Types:**
    - **Usage:** Track consumption of AWS resources (e.g., EC2 instance hours, S3 data transfer).
    - **Cost:** Track the total monetary spend on AWS services.
    - **Reservation:** Track the utilization of your Reserved Instances (EC2, ElastiCache, RDS, Redshift).
    - **Savings Plan:** Track the utilization of your Savings Plans.
- **Notifications:**
    - Up to five SNS notifications can be configured per budget.
- **Granular Filtering:** Budgets can be filtered by various dimensions, including:
    - Service
    - Linked Account
    - Tag
    - Purchase Option
    - Instance Type
    - Region
    - Availability Zone
    - API Operation
- **Pricing:** The first two budgets are free; subsequent budgets incur a cost of two cents per day.

### Budget Actions

Budget Actions enable automated responses when a budget exceeds a defined threshold. This helps prevent unintentional overspending.

- **Action Types:**
    - **Apply IAM Policy:** Attach a specific IAM policy to a user, group, or role to restrict permissions.
    - **Apply Service Control Policy (SCP):** Apply an SCP to an Organizational Unit (OU) to restrict actions within member accounts.
    - **Stop EC2 or RDS Instances:** Automatically stop running EC2 or RDS instances.
- **Execution Modes:**
    - **Automatic:** Actions are executed automatically upon reaching the threshold.
    - **Workflow Approval:** Actions require manual approval before execution.

### Budget Management Architectures

There are two main approaches to managing budgets in AWS Organizations:

- **Centralized Budget Management:**
    - Budgets for all member accounts are created and managed within the management account.
    - Filters (e.g., account ID) are applied to each budget to tailor it to a specific member account.
    - When a budget threshold is breached, notifications (via SNS) can trigger automated actions, such as:
        - A Lambda function moving the breaching account to a more restrictive OU with pre-applied SCPs.
        - Sending email notifications to administrators via SNS.
- **Decentralized Budget Management:**
    - Budgets are managed directly within each member account.
    - CloudFormation StackSets can be used to deploy consistent budgets across multiple member accounts.
    - Each member account can configure notifications and automated actions (e.g., stopping EC2 instances) based on their local budget thresholds.

### AWS Cost Explorer

Cost Explorer is a tool that allows you to visualize, understand, and manage your AWS costs and usage over time.

- **Features:**
    - Create custom reports to analyze cost and usage data.
    - Provides a high-level overview of total costs and usage across all accounts.
    - Offers the ability to drill down and analyze data monthly, hourly, and at the resource level.
    - Helps identify opportunities for cost optimization, such as choosing optimal Savings Plans.
    - Provides cost and usage forecasting up to 12 months based on historical data.
- **Filtering:** Similar granular filtering options as AWS Budgets (service, linked account, tags, etc.).
- **Interface:** Presents data through detailed graphs and reports, making it easy to understand cost trends.

### Key Takeaways for the Exam:

- Understand the different types of budgets you can create in AWS Budgets.
- Know how to configure notifications and the granularity of filtering available.
- Grasp the concept and benefits of Budget Actions for automated cost control.
- Differentiate between centralized and decentralized budget management strategies within AWS Organizations.
- Understand the purpose and capabilities of AWS Cost Explorer for cost visualization, analysis, and forecasting.
- Recognize that Cost Explorer can help in identifying optimal Savings Plan purchases.
- Be aware that the filtering options are consistent between AWS Budgets and Cost Explorer.