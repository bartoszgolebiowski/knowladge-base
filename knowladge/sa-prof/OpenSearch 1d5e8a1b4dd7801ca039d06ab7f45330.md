# OpenSearch

# **AWS Solution Architect Professional - Amazon OpenSearch Notes**

## **Overview**

- **Renamed Service:** Amazon OpenSearch is the new name for Amazon Elasticsearch Service.
- **Key Terminology Update:**
    - Elasticsearch is now **OpenSearch**.
    - Kibana is now **OpenSearch Dashboards**.
- **Managed Service:** Amazon OpenSearch Service is a managed version of the open-source OpenSearch project, a fork of Elasticsearch. This fork was necessary due to changes in Elasticsearch's licensing.
- **Deployment Options:**
    - **Managed Cluster:** Users define the instance types and configurations.
    - **Serverless Cluster:** A simpler, serverless option for using Amazon OpenSearch.
- **Use Cases:**
    - Log Analytics
    - Real-time Application Monitoring
    - Security Analytics
    - Full-Text Search
    - Clickstream Analytics
    - Indexing

## **Components**

- **OpenSearch:** Provides the core search and indexing capabilities.
- **OpenSearch Dashboards (formerly Kibana):** Offers real-time dashboards and visualizations on data within OpenSearch. It's an alternative to CloudWatch Dashboards with more advanced features.
- **Logstash:** A log ingestion tool. When used with the logs agent, it serves as an alternative to CloudWatch Logs, allowing more control over retention and granularity.

## **Architecture Examples**

### **DynamoDB Integration for Search**

- **Goal:** Enable search functionality on data stored in DynamoDB.
- **Traditional Flow:**
    1. DynamoDB table experiences Create, Update, or Delete operations.
    2. DynamoDB Stream captures these changes.
    3. AWS Lambda function reads the stream and sends data to Amazon OpenSearch for indexing.
    4. A custom application (e.g., on EC2 behind a load balancer) uses the OpenSearch API to search items.
    5. The application then retrieves the full item details directly from the DynamoDB table based on the search results.
- **Newer Flow (Leveraging Kinesis Data Streams):**
    1. DynamoDB table sends changes to a Kinesis Data Stream.
    2. Kinesis Data Firehose reads from the stream and delivers data to Amazon OpenSearch.
- **Rationale:** DynamoDB excels at simple row-level operations, while OpenSearch is optimized for search and indexing. Combining them allows for powerful search capabilities over DynamoDB data.

### **CloudWatch Logs Integration for Analytics**

![image.png](image%2034.png)

- **Goal:** Analyze and visualize application logs stored in CloudWatch Logs using Amazon OpenSearch.
- **Method 1 (Direct Lambda Integration):**
    1. CloudWatch Logs receives application logs.
    2. A CloudWatch Subscription Filter forwards relevant log events to an AWS Lambda function (managed by AWS for OpenSearch integration).
    3. The Lambda function sends the log data in real-time to Amazon OpenSearch.
- **Method 2 (Kinesis Data Firehose Integration):**
    1. CloudWatch Logs receives application logs.
    2. A CloudWatch Subscription Filter forwards log events to a Kinesis Data Firehose delivery stream.
    3. Kinesis Data Firehose (with potential batching) delivers the logs in near real-time to Amazon OpenSearch.

**Key takeaway for the exam:** Understand the renaming of the services, the core components of Amazon OpenSearch, its primary use cases, and common integration patterns with services like DynamoDB and CloudWatch Logs for search and log analytics. Be aware of the different data flow options, including the use of DynamoDB Streams and Kinesis Data Streams.