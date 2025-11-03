# SQS

# **AWS Solution Architect Professional - Amazon SQS (Simple Queue Service)**

## **Purpose and Goals**

- **Serverless Managed Queue:** No infrastructure provisioning required.
- **IAM Integration:** Fully integrated for security and access control.
- **Extreme Scale (Standard Queues):** Handles virtually unlimited throughput without manual scaling.
- **Decoupling:** Enables independent scaling and fault tolerance between services.
- **Asynchronous Processing:** Facilitates non-blocking communication and task execution.

## **Key Characteristics**

- **Message Size Limit:** Maximum message size is **256 KB**.
- **Handling Large Payloads:** For larger files, store them in Amazon S3 and send the S3 object key through SQS. Consumers retrieve the key and then the object from S3.
- **Consumers:** Messages can be read by:
    - EC2 instances (often managed by Auto Scaling Groups).
    - AWS Lambda functions (using event source mappings).
- **Write Buffer for DynamoDB:** SQS can act as a buffer to absorb write traffic to DynamoDB, preventing potential throttling issues. An application can then consume messages from SQS and write to DynamoDB at a controlled pace.

## **SQS FIFO (First-In, First-Out) Queues**

- **Ordered Delivery:** Messages are received and processed in the exact order they were sent.
- **Limited Scale:** Due to ordering constraints, throughput is limited to:
    - 300 messages per second without batching.
    - Up to 3,000 messages per second with batching.

## **Dead Letter Queues (DLQs)**

- **Purpose:** To handle messages that cannot be processed successfully by consumers after a certain number of attempts.
- **Workflow:**
    1. Consumer fails to process a message within the visibility timeout.
    2. The message is returned to the queue.
    3. This process repeats.
    4. A **maximum receives threshold** can be set on the source queue.
    5. If the threshold is exceeded, SQS moves the message to the designated Dead Letter Queue.
- **Benefits:**
    - **Debugging:** Provides a repository of problematic messages for analysis.
    - **Failure Isolation:** Prevents failing messages from repeatedly impacting the main queue.
    - **Delayed Processing:** Allows time to investigate and potentially reprocess failed messages.
- **FIFO DLQ Requirement:** A DLQ for a FIFO queue must also be a FIFO queue.
- **Standard DLQ Requirement:** A DLQ for a standard queue must also be a standard queue.
- **Message Expiration:** Ensure messages in the DLQ are processed before their retention period expires (consider setting a long retention period, e.g., 14 days).

## **Redrive to Source Feature**

- **Purpose:** Facilitates the reprocessing of messages from the Dead Letter Queue back to the original source queue after debugging and fixing any issues.
- **Workflow:**
    1. Inspect and debug messages in the DLQ.
    2. Fix the consumer code or understand the reason for processing failures.
    3. Use the "redrive to source" feature to move the messages back to the original SQS queue.
    4. Consumers can then re-attempt processing the messages without being aware of their journey to the DLQ.

## **Idempotency**

- **Importance:** Crucial for consumers processing messages from SQS because messages can be delivered more than once (especially in standard queues) due to potential failures or timeouts.
- **Definition:** An operation is idempotent if performing it multiple times has the same effect as performing it once.
- **Example (Non-Idempotent):** Inserting a new row into DynamoDB for each received SQS message will result in duplicate entries if the same message is processed twice.
- **Example (Idempotent):** Performing an "upsert" (update if exists, insert if not) into DynamoDB using a unique primary key ensures that only one record exists for a given message, even if processed multiple times.

## **Lambda as an SQS Consumer**

- **Event Source Mapping:** Lambda can be configured to read messages from an SQS queue using an event source mapping.
- **Long Polling (Default):** The event source mapper uses long polling to efficiently retrieve messages and minimize costs and latency.
- **Batching:** You can configure a batch size (1 to 10 messages) for each Lambda invocation. Larger batches can improve efficiency but require the Lambda function to handle multiple messages.
- **Visibility Timeout Recommendation:** The recommended queue visibility timeout should be at least **six times** the timeout of your Lambda function to prevent premature message redelivery if the Lambda function takes longer to process the batch.
- **Dead Letter Queues with Lambda:**
    - **SQS-Level DLQ:** To handle messages that Lambda fails to process from the SQS queue, you need to configure a DLQ **at the SQS queue level**, not within the Lambda function itself.
    - **Lambda Destinations:** A newer Lambda feature allows you to configure destinations (including SQS queues or SNS topics) for events that Lambda fails to process asynchronously. However, for messages read from an SQS queue via event source mapping, the DLQ is configured on the SQS queue.

## **Solution Architecture Example: Decoupling with SQS**

- **Components:**
    - **Clients:** Generate work requests.
    - **SQS Request Queue:** Holds incoming work requests.
    - **Work Processors:** Consume messages from the request queue and perform the work.
    - **SQS Response Queue (Optional):** Used by work processors to send results back to clients.
    - **Clients (Reading Response Queue):** Retrieve results.
- **Benefits:**
    - **Decoupling:** Clients and work processors can scale independently.
    - **Fault Tolerance:** If a work processor fails, other processors can pick up the messages.
    - **Load Balancing:** Horizontal scaling of work processors to handle increased load.
    - **Scalability:** SQS itself scales seamlessly.

## **General SQS Considerations**

- SQS is a versatile service with numerous architectural patterns.
- Look for keywords like "decoupling" and "at least once delivery" in exam questions, as SQS is often a suitable solution in these scenarios.