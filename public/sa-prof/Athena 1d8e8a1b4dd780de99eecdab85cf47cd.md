# Athena

# **Amazon Athena - Serverless Interactive Query Service**

## **Purpose and Goals**

- Serverless query service to analyze data stored in Amazon S3 buckets.
- Uses standard SQL to query data files directly in S3 without moving them.
- Built on the Presto engine.

## **Core Concepts**

- **Serverless:** No infrastructure to provision or manage.
- **Direct S3 Querying:** Analyzes data directly in S3 buckets.
- **Standard SQL:** Uses familiar SQL language for querying.
- **Data Format Support:** Supports various formats like CSV, JSON, ORC, Avro, and Parquet.
- **Pay-per-Query:** Pricing based on the amount of data scanned per terabyte.

## **Integration and Usage**

- **Amazon QuickSight:** Commonly used with QuickSight for creating reports and dashboards based on Athena queries.
- **Use Cases:**
    - Ad hoc queries
    - Business intelligence
    - Analytics and reporting
    - Analyzing AWS service logs (VPC Flow Logs, ELB Logs, CloudTrail, etc.)

## **Performance Improvements**

To optimize Athena query performance and reduce costs (since you pay per TB scanned):

1. **Use Columnar Data Formats:**
    - **Recommended Formats:** Apache Parquet and ORC.
    - **Benefits:** Scan only the necessary columns, leading to significant performance and cost savings.
    - **Data Conversion:** Services like AWS Glue can be used to convert data from row-based formats (like CSV) to columnar formats.
2. **Compress Data:**
    - **Benefit:** Reduces the amount of data that needs to be retrieved from S3, leading to faster query execution and lower costs.
    - **Compression Mechanisms:** (Mentioned as "listed right here" in the transcript, actual mechanisms weren't specified, but common ones include Gzip, Snappy, LZO).
3. **Partition Data:**
    - **Concept:** Organize data in S3 using a directory structure that reflects common query filters (e.g., year, month, day).
    - **Example:** `s3://bucket/flight-data/year=1991/month=01/day=01/data.parquet`
    - **Benefits:** When querying with filters on partitioned columns, Athena only scans the relevant S3 prefixes, significantly reducing the amount of data scanned.
4. **Use Larger Files:**
    - **Benefit:** Minimizes overhead associated with processing a large number of small files.
    - **Recommendation:** Aim for larger file sizes (e.g., 128 MB and over) for better performance.

## **Federated Query**

- **Concept:** Allows Athena to query data sources beyond Amazon S3, including relational and non-relational databases, objects, and custom data sources (both on AWS and on-premises).
- **Data Source Connectors:** Uses Lambda functions as Data Source Connectors to interact with other services. One Lambda function is typically used per data source type.
- **Supported Data Sources (Examples):**
    - CloudWatch Logs
    - DynamoDB
    - Amazon RDS (various engines)
    - Amazon Redshift
    - Amazon Aurora
    - SQL Server
    - MySQL
    - HBase on EMR
    - On-premises databases (via JDBC/ODBC)
    - ElastiCache
    - DocumentDB
- **Workflow:**
    1. Athena receives a federated query.
    2. Athena invokes the appropriate Data Source Connector (Lambda function).
    3. The Lambda function executes the query against the external data source.
    4. The results are returned to Athena.
    5. Athena can then process and return the combined results, potentially storing them in S3 for further analysis.
- **Benefits:** Enables querying and joining data across heterogeneous data stores from a single interface.

## **Key Takeaways for the Exam**

- Understand that Athena is a **serverless SQL query engine for S3**.
- Know that you **pay per terabyte of data scanned**.
- Be able to identify and explain **performance optimization techniques**:
    - Columnar data formats (Parquet, ORC)
    - Data compression
    - Data partitioning
    - Using larger files
- Understand the concept and benefits of **Athena Federated Query** for querying data beyond S3 using Data Source Connectors (Lambda functions).
- Recognize common **use cases** for Athena, especially log analysis and ad hoc querying of S3 data.
- When a scenario involves analyzing data in S3 with SQL in a serverless manner, **think of Athena**.