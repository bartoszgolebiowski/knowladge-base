# Kinesis Data Firehose

# **Amazon Kinesis Data Firehose**

## **Purpose and Goals**

- To **store data into target destinations**.
- Acts as a data delivery service.

## **Key Concepts**

- **Producers:** Applications or services that send data to Kinesis Data Firehose.
    - Can be the same applications that send data to Kinesis Data Streams.
    - Kinesis Data Firehose can also read from Kinesis Data Streams, Amazon CloudWatch, or AWS IoT (Kinesis Data Streams is the most common source).
- **Batch Writes:** Firehose accumulates data into batches before writing to the destination for efficiency.
- **Near Real-time:** Data delivery is not instantaneous due to buffering.

## **Sources**

- Applications
- Kinesis Data Streams (most common)
- Amazon CloudWatch
- AWS IoT

## **Transformation (Optional)**

- **AWS Lambda:** Can be used to perform small modifications or data transformations on records before delivery.

## **Destinations (Remember these!)**

- **AWS:**
    - **Amazon S3:** Very important.
    - **Amazon Redshift:** Data is first written to S3, then copied to Redshift using a COPY command.
    - **Amazon OpenSearch Service:**
- **Third-Party Partners:** (Examples: Datadog, Splunk, New Relic, MongoDB - you don't need to memorize all partners).
- **Custom Destinations:** Any destination with a valid HTTP endpoint.

## **Failure Handling and Archiving**

- **Backup to S3:** Option to send all data or only failed data (processing or delivery failures) to a backup S3 bucket. This ensures no data loss.

## **Management and Scaling**

- **Fully Managed:** No administration required.
- **Near Real-time:** Delivery based on buffer time and buffer size.
- **Automatic Scaling:** Scales throughput up or down automatically based on demand.

## **Use Cases (Remember these!)**

- Loading data into **Amazon Redshift**, **Amazon S3**, **Amazon OpenSearch Service**, or **Splunk**.

## **Key Features**

- **Automatic Scaling:** Handles varying data throughput.
- **Data Format Support:** Supports various data formats.
- **Data Conversion:** Can convert data formats (e.g., JSON to Parquet/ORC for S3).
- **Data Transformation:** Integration with AWS Lambda for custom transformations (e.g., CSV to JSON).
- **Compression (for S3):** Supports GZIP, ZIP, and SNAPPY compression. GZIP is the only supported compression for Redshift loading.
- **Pay-per-use:** Only pay for the amount of data that flows through Firehose. No upfront provisioning costs.

## **Important Note for the Exam**

- **Spark Streaming and Kinesis Client Library (KCL) CANNOT read directly from Kinesis Data Firehose.** They only read from Kinesis Data Streams.

## **Delivery Diagram Highlights**

- **Source (e.g., Kinesis Data Streams) -> Kinesis Data Firehose -> (Optional Data Transformation via Lambda) -> Destination (e.g., S3, Redshift, OpenSearch).**
- **Redshift Destination:** Data flows through S3 first.
- **Source Record Backup:** Option to deliver all source records to a separate S3 bucket.
- **Failure Archiving:** Option to archive transformation and delivery failures to S3.
- **No Data Loss:** Firehose is designed to ensure data reaches its target or is archived in case of failures.

## **Buffer Sizing**

- Firehose buffers incoming records based on **buffer size** and **buffer time**.
- **Buffer Size:** When the accumulated data reaches the defined size, the buffer is flushed.
- **Buffer Time:** If the buffer size is not reached within the defined time, the buffer is flushed anyway.
- **Automatic Buffer Size Adjustment:** Firehose can automatically increase buffer size for higher throughput.
- **Buffer Time Minimum:** 1 minute.

## **Kinesis Data Streams vs. Firehose**

| **Feature** | **Kinesis Data Streams** | **Kinesis Data Firehose** |
| --- | --- | --- |
| Producer/Consumer | Requires custom code | Producers send directly; managed delivery |
| Real-time/Near Real-time | Real-time (ms latency) | Near real-time (buffering) |
| Scaling | Manual shard management | Fully managed, autoscaling |
| Destinations | Flexible (consumers decide) | Specific AWS and third-party services |
| Data Storage | 1-365 days, replay capability | No data storage in Firehose |
| Data Transformation | Consumer responsibility | Serverless via Lambda |
| Management | Requires scaling and monitoring | Fully managed, no administration |
| Lambda Integration | Can be a consumer | Can be used for transformation |
| KPL Support | Yes | Yes |
| KCL Support | Yes (for consumers) | No (cannot read from Firehose) |
| Pricing | Per shard provisioned, data in/out | Per data volume through Firehose |

## **Use Case Considerations**

- **Kinesis Data Streams:** Use when you need real-time processing by custom applications, data replay, and multiple consumers.
- **Kinesis Data Firehose:** Use when your primary goal is to reliably deliver streaming data to specific destinations like S3, Redshift, OpenSearch, or Splunk with automatic scaling and optional transformation.
- Consider the **real-time vs. near real-time** requirement of your application.