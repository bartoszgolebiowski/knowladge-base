# SNS FanOut

# **AWS Solution Architect Professional - SNS Plus SQS Fan-Out Pattern**

## **Core Concept**

- **One-to-Many Distribution:** Send a single message to an SNS topic, which then distributes it to multiple subscribed SQS queues.
- **Overcoming Direct Integration Issues:** Avoids problems associated with sending messages individually to each SQS queue (e.g., application crashes, delivery failures, difficulty in adding new queues).

## **Architecture**

1. **Producer:** Sends a message once to an **SNS Topic**.
2. **SNS Topic:** Acts as a central point for message distribution.
3. **Subscribed SQS Queues:** Multiple SQS queues are subscribed to the SNS topic.
4. **Consumers:** Each subscribed SQS queue receives a copy of every message published to the SNS topic.

**Example:** A "Buying Service" sends a single message to an SNS topic. Two SQS queues ("Fraud Service Queue" and "Shipping Service Queue") are subscribed to this topic and each receives the message.

## **Benefits**

- **Fully Decoupled Model:** Producers and consumers are independent of each other.
- **No Data Loss (with SQS):** SQS provides message persistence, delayed processing, and retries.
- **Scalability:** Easily add more SQS queues as subscribers to the SNS topic over time without modifying the producer.

## **Security Considerations**

- **SQS Queue Access Policy:** The SQS queue's access policy must explicitly allow the SNS topic to write messages to it. This is crucial for the fan-out pattern to work.
- **Cross-Region Delivery:** SNS topics in one AWS region can deliver messages to SQS queues in other regions, provided the necessary security permissions are in place.

## **Use Cases**

- **Distributing S3 Events to Multiple Queues:**
    - **Problem:** S3 event notifications have a limitation of one rule per event type and prefix combination.
    - **Solution:** Configure the S3 event to send notifications to an SNS topic. Subscribe multiple SQS queues to this topic to process the same S3 event for different purposes. Other subscriber types (e.g., Lambda, email) can also be added.
- **Direct SNS to S3 via Kinesis Data Firehose (KDF):**
    - SNS can directly integrate with KDF.
    - Producer sends to SNS Topic -> SNS sends to KDF -> KDF delivers to S3 (or other supported KDF destinations).
    - This allows for persistent storage of SNS messages.

## **Fan-Out with SNS FIFO (First-In, First-Out)**

- **Ordering and Deduplication:** SNS now supports FIFO topics, providing message ordering (by message group ID) and deduplication (using deduplication ID or content-based).
- **Subscriber Limitation:** Currently, only SQS FIFO queues can subscribe to SNS FIFO topics to maintain the FIFO order.
- **Throughput:** SNS FIFO throughput is the same as SQS FIFO.
- **Use Case:** When you need fan-out with guaranteed message order and deduplication for downstream SQS FIFO queues.

## **Message Filtering in SNS**

- **Purpose:** Allows subscribers to receive only a subset of messages published to a topic based on message attributes.
- **Filter Policy:** A JSON policy defined at the subscription level.
- **Default Behavior:** If no filter policy is set, the subscriber receives all messages.
- **Example:**
    - **SNS Topic:** Receives transaction messages with attributes like `order_number`, `product`, `quantity`, and `state`.
    - **SQS Queue for "Placed" Orders:** Subscribed to the topic with a filter policy: `{"state": ["Placed"]}`. This queue will only receive messages where the `state` attribute is "Placed".
    - **SQS Queue for "Canceled" Orders:** Subscribed with a filter policy: `{"state": ["Canceled"]}`.
    - **Email Subscription for "Canceled" Orders:** Also uses the `{"state": ["Canceled"]}` filter policy.
    - **SQS Queue for All Messages:** Subscribed without any filter policy.

## **Exam Relevance**

- The SNS plus SQS fan-out pattern is a common and important architecture pattern for building scalable and resilient applications on AWS.
- Understand the benefits, security implications, and various use cases, including S3 event handling and integration with Kinesis Data Firehose.
- Be aware of SNS FIFO capabilities and its limitations on subscriber types.
- Message filtering in SNS is a powerful feature for routing relevant messages to specific subscribers and is likely to be tested in various scenarios.