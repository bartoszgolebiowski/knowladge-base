# Kinesis Data Stream

# **Amazon Kinesis Data Streams**

## **Purpose and Goals**

- Collect and store streaming data in **real time**.

## **Key Concepts**

- **Real-time Data:** Data created and used immediately (e.g., website clickstreams, IoT device data, server metrics and logs).
- **Producers:** Applications or services that send data into Kinesis Data Streams.
    - **Applications (Custom Code):** Required for sending data from websites or devices.
    - **Kinesis Agent:** Installed on servers to send metrics and logs.
- **Consumers:** Applications or services that process data from Kinesis Data Streams in real time.
    - **Applications (Custom Code)**
    - **Lambda Functions**
    - **Amazon Data Firehose** (covered in a later lecture)
    - **Managed Service for Apache Flink** (for stream analytics)

## **Features**

- **Data Retention:** Up to 365 days.
- **Data Persistence:** Enables reprocessing and replaying of data by consumers.
- **Immutable Data:** Data cannot be deleted once sent; it expires based on the retention period.
- **Data Size Limit:** Up to 1 MB per record.
- **Ordered Data:** Data points with the same **Partition ID** are guaranteed to be in order. This allows for temporal relationships between related data.
- **Security:**
    - **At-rest Encryption:** KMS encryption.
    - **In-flight Encryption:** HTTPS encryption.
- **Optimized Libraries:**
    - **Kinesis Producer Library (KPL):** For building high-throughput producer applications.
    - **Kinesis Client Library (KCL):** For building optimized consumer applications.

## **Capacity Modes**

### **1. Provisioned Mode**

- You choose the number of **shards** for your stream.
- **Shard:** Represents the capacity of the stream. More shards = higher throughput.
- **Inbound Capacity (per shard):** 1 MB per second OR 1,000 records per second.
- **Outbound Capacity (per shard):** 2 MB per second.
- **Scaling:** Can be done manually (increase or decrease the number of shards).
- **Monitoring:** Requires monitoring throughput to adjust the number of shards as needed.
- **Pricing:** Pay per shard provisioned per hour.

### **2. On-Demand Mode**

- No need to provision or manage capacity.
- **Default Capacity:** Approximately 4,000 records per second or 4 MB in.
- **Automatic Scaling:** Kinesis Data Streams automatically scales based on observed throughput over the past 30 days.
- **Pricing:** Pay per stream per hour and for the amount of data ingested and retrieved.

## **Key Takeaway for the Exam**

- The keyword "**real time**" is crucial when identifying use cases for Kinesis Data Streams.