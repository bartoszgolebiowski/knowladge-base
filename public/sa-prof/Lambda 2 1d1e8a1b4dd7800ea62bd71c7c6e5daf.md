# Lambda 2

## AWS Lambda in a VPC

![image.png](image%2023.png)

This lecture explains how deploying Lambda functions within an Amazon Virtual Private Cloud (VPC) affects network connectivity and how to manage it.

**Default Lambda Deployment:**

- By default, Lambda functions run in the AWS cloud, outside your VPC.
- They have access to the public internet.
- They can access public AWS service APIs (e.g., DynamoDB public endpoint) directly.
- They **cannot** directly access private resources within your VPC (e.g., private RDS databases).

**Lambda Deployment in a VPC:**

- When you deploy a Lambda function within your VPC:
    - It is associated with a **security group** to control inbound and outbound traffic.
    - It is deployed within the **subnets** you specify in your VPC.
    - It can then access private resources within those subnets (e.g., private RDS).
- **Internet Access:**
    - Lambda functions deployed in **private subnets** **do not** have direct internet access by default.
    - To enable internet access for Lambda in a private subnet, you need to use a **NAT Gateway** or a **NAT Instance** deployed in a **public subnet**. The Lambda function's traffic will be routed through the NAT device to an Internet Gateway.
    - Lambda functions deployed in **public subnets** **do not** automatically have internet access. They still require a NAT device in a public subnet for outbound internet connectivity.
- **Accessing Public AWS Services (e.g., DynamoDB):**
    - **Option 1 (Via NAT Gateway):** Traffic from the Lambda function in a private subnet can be routed through a NAT Gateway and an Internet Gateway to reach the public API of DynamoDB.
    - **Option 2 (VPC Endpoint):** For keeping traffic within the AWS network, you can create a **VPC Endpoint for DynamoDB**. This allows the Lambda function within your VPC to access DynamoDB directly without going through the internet.

**Important Note:** CloudWatch Logs access for Lambda functions deployed in a VPC (even in private subnets without NAT or an Internet Gateway) will still work. This functionality is embedded within the Lambda service.

## Lambda IP Addresses

- **Default (Non-VPC) Deployment:** Lambda functions get a **random public IP address** from AWS's pool when accessing the internet. The target API sees traffic from a dynamic IP.
- **Fixed IP Address for Outbound Traffic (VPC Deployment):**
    1. Deploy the Lambda function in a **private subnet**.
    2. Configure the private subnet to route outbound traffic to a **NAT Gateway** deployed in a **public subnet**.
    3. Attach a **fixed Elastic IP address (EIP)** to the NAT Gateway.
    4. All internet-bound traffic from the Lambda function will now originate from the **static Elastic IP address** of the NAT Gateway.
- **Benefit:** This architecture provides a consistent and predictable source IP address for your Lambda functions when they access external APIs, allowing you to implement network security measures like IP whitelisting on the API side.

## Lambda Invocation Types

- **Synchronous Invocation:**
    - Invoked via: CLI, SDK, API Gateway.
    - The invoker waits for the Lambda function to execute and return a response immediately.
    - Error handling (retries, exponential backoff) must be implemented on the client-side.
    - **Example:** SDK invoking a Lambda function and waiting for the result. API Gateway proxying a request to Lambda and returning the response to the client.
- **Asynchronous Invocation:**
    - Invoked via: SNS, S3, EventBridge.
    - Lambda queues the event for processing and returns a success response immediately to the invoker **without waiting** for the function to complete.
    - Lambda handles retries on errors (up to three attempts in total). This means the Lambda function might be executed multiple times for the same event.
    - **Idempotency:** It's crucial for asynchronous Lambda functions to be **idempotent** (producing the same result regardless of how many times they are executed for the same event) to avoid unintended side effects from retries.
    - **Dead-Letter Queue (DLQ):** You can configure a DLQ (SNS topic or SQS queue) to receive events that failed to be processed successfully after all retry attempts.
    - **Example:** A new file in S3 triggers a Lambda function asynchronously.

## Lambda Architectures: S3 to SNS vs. S3 to SNS to SQS to Lambda

This section compares two seemingly similar architectures for processing files uploaded to S3:

**Architecture 1: S3 -> SNS -> Lambda**

![image.png](image%2024.png)

- **Invocation:** S3 event directly triggers an SNS notification, which immediately invokes the Lambda function.
- **Concurrency:** High concurrency potential. Each S3 event can trigger a separate Lambda invocation almost instantaneously.
- **Latency:** Low latency between file upload and Lambda invocation.
- **Reliability (Without DLQ):** Potential for data loss if Lambda function fails and retries don't succeed.
- **Error Handling:** Requires configuring a DLQ on the Lambda function to capture failed invocations.
- **Scalability:** Scales very quickly with the number of S3 events.

**Architecture 2: S3 -> SNS -> SQS -> Lambda**

![image.png](image%2025.png)

- **Invocation:** S3 event triggers an SNS notification, which sends a message to an SQS queue. Lambda function polls the SQS queue and processes messages in batches.
- **Concurrency:** Lambda concurrency will scale based on the number of messages in the SQS queue and the configured scaling of the Lambda function. It might be slightly less immediate than the direct SNS trigger.
- **Latency:** Higher potential latency due to messages being queued in SQS before Lambda processes them.
- **Reliability:** Higher reliability. Messages are persisted in SQS until successfully processed by Lambda. Failed processing attempts can leave messages in the queue for further investigation or reprocessing.
- **Error Handling:** SQS offers built-in mechanisms for handling failed messages (e.g., Dead-Letter Queues). Lambda can also have its own DLQ for failures after receiving messages from SQS.
- **Scalability:** Scales based on SQS queue size and Lambda's ability to consume messages. Batch processing can be more efficient for certain workloads.

**Key Trade-offs:**

| Feature | S3 -> SNS -> Lambda | S3 -> SNS -> SQS -> Lambda |
| --- | --- | --- |
| **Invocation** | Immediate, per event | Batched, polled from SQS |
| **Latency** | Lower | Potentially higher |
| **Concurrency** | Higher, immediate scaling | Scaled by SQS queue size & Lambda config |
| **Reliability** | Lower without DLQ | Higher (message persistence in SQS) |
| **Error Handling** | DLQ on Lambda required for persistence | SQS DLQ and Lambda DLQ options |
| **Efficiency** | Can be less efficient for many small events | Batch processing can be more efficient |