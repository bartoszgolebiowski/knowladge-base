# S3 Leans

# **Amazon S3 Storage Lens - Summary Notes**

## **Purpose and Goals**

- **Centralized Storage Analysis:** Provides a single view to understand, analyze, and optimize object storage across an entire AWS Organization.
- **Anomaly Detection:** Helps discover unusual storage patterns and potential issues.
- **Cost Efficiency Identification:** Enables identification of opportunities to reduce storage costs.
- **Protection Best Practices Enforcement:** Facilitates the application of data protection best practices across the organization.
- **Usage and Activity Metrics:** Offers 30-day usage and activity metrics.
- **Aggregation Levels:** Data can be aggregated at the organization, account, region, bucket, or even prefix level.
- **Dashboards:** Provides a default dashboard and allows the creation of custom dashboards.
- **Data Export:** Metrics and reports can be exported to an S3 bucket in CSV or Parquet format.

## **Key Components**

- **Organization-Wide Visibility:** Aggregates data across all linked accounts in an AWS Organization.
- **Multi-Level Analysis:** Enables drilling down into specific accounts, regions, buckets, or prefixes.
- **Report Generation:** Creates reports summarizing storage usage, cost, and protection metrics.
- **Actionable Insights:** Provides insights to optimize costs, improve security, and manage storage effectively.

## **Default Dashboard**

- **Pre-configured:** Offers summarized insights and trends for both free and advanced metrics without requiring specific setup.
- **Cross-Region and Cross-Account:** Displays data aggregated across multiple AWS regions and accounts by default.
- **Non-Deletable (but Disablable):** The default dashboard cannot be deleted but can be disabled if needed.
- **Customizable Filtering:** Allows filtering data by region, account, bucket, storage class, etc., through a centralized configuration.
- **Key Information:** Presents metrics like total storage, object count, average object size, and the number of buckets and accounts.

## **Available Metrics**

### **Summary Metrics (Free & Advanced)**

- **Storage Bytes:** Total size of storage used.
- **Object Counts:** Total number of objects stored.
- **Use Cases:** Identify fast-growing or underutilized buckets and prefixes.

### **Cost Optimization Metrics (Advanced)**

- **Non-Current Version Storage Bytes:** Storage consumed by non-current versions of objects (for buckets with versioning enabled).
- **Incomplete Multi-Part Upload Storage Bytes:** Storage used by incomplete multi-part uploads.
- **Use Cases:** Identify buckets with failed multi-part uploads and objects that can be transitioned to lower-cost storage classes.

### **Data Protection Metrics (Advanced)**

- **Versioning Enabled Bucket Counts:** Number of buckets with versioning enabled.
- **MFA Delete Enabled Bucket Counts:** Number of buckets with MFA Delete enabled.
- **SSCKMS Enabled Bucket Counts:** Number of buckets using SSE-KMS encryption.
- **Cross-Region Replication Rules Counts:** Number of CRR rules configured.
- **Use Cases:** Identify buckets not following data protection best practices.

### **Access Management Metrics (Advanced)**

- **Object Ownership Settings:** Information about the object ownership settings of buckets.
- **Use Cases:** Identify which object ownership settings are in use.

### **Event Metrics (Advanced)**

- **S3 Event Notifications Configuration:** Number of buckets with S3 event notifications configured.
- **Use Cases:** Understand the adoption of S3 event notifications.

### **Performance Metrics (Advanced)**

- **S3 Transfer Acceleration Enabled Bucket Counts:** Number of buckets with S3 Transfer Acceleration enabled.
- **Use Cases:** Track the usage of S3 Transfer Acceleration.

### **Activity Metrics (Advanced)**

- **All Requests:** Total number of requests made to S3.
- **Get Requests:** Number of GET requests.
- **Put Requests:** Number of PUT requests.
- **Bytes Downloaded:** Amount of data downloaded.
- **Use Cases:** Understand the type and volume of activity on your S3 storage.

### **HTTP Status Code Metrics (Advanced)**

- Metrics for various HTTP status codes (e.g., 200 OK, 403 Forbidden).
- **Use Cases:** Gain insights into the success and error rates of requests.

## **Free vs. Advanced Metrics**

| **Feature** | **Free Metrics** | **Advanced Metrics & Recommendations** |
| --- | --- | --- |
| **Availability** | Automatically available to all customers | Paid feature |
| **Number of Usage Metrics** | ~28 | Additional metrics (activity, advanced cost/protection, status codes) |
| **Data Query Availability** | 14 days | 15 months |
| **Prefix-Level Metrics** | No | Yes |
| **CloudWatch Metric Publishing** | No | Yes (at no additional charge) |
| **Recommendations** | Basic usage insights | Advanced cost and performance optimization recommendations |

## **Key Takeaways**

- S3 Storage Lens provides a centralized view for optimizing S3 across your organization.
- The default dashboard offers immediate, cross-account, and cross-region insights.
- Understand the difference between free and paid metrics to leverage the appropriate level of detail.
- It helps in identifying cost savings, security vulnerabilities, and usage patterns in your object storage.
- Remember it covers object storage metrics, including encryption status and more.