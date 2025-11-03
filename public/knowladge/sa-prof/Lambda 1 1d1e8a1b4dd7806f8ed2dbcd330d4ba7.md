# Lambda 1

## AWS Lambda

This lecture covers the fundamentals and key integrations of AWS Lambda, a serverless compute service.

### Integrations

Lambda seamlessly integrates with various AWS services to enable event-driven architectures:

- **API Gateway:** Invokes Lambda functions in response to REST API requests.
- **Kinesis:** Processes data streams in real-time.
- **DynamoDB:** Triggers Lambda functions based on changes in DynamoDB tables (via DynamoDB Streams).
- **S3:** Executes Lambda functions in response to S3 events (e.g., object creation).
- **Internet of Things (IoT):** Processes data and events from IoT devices.
- **EventBridge:** Acts as a target for events from various AWS services and custom applications, enabling rule-based invocation of Lambda.
- **CloudWatch Logs:** Can be configured as a trigger for Lambda functions based on log events.
- **SNS (Simple Notification Service):** Invokes Lambda functions in response to SNS notifications.
- **Cognito:** Executes Lambda functions at different stages of the user authentication process (pre- and post-authentication hooks).
- **SQS (Simple Queue Service):** Processes messages from SQS queues.

### Common Architectures

- **Serverless Thumbnail Creation:**
    - New image uploaded to S3 triggers a Lambda function.
    - Lambda creates a thumbnail and stores it back in S3.
    - Metadata (image name, size, creation date) can be stored in DynamoDB.
- **Serverless Cron Jobs:**
    - EventBridge can be configured with a time-based rule (schedule) to trigger a Lambda function at regular intervals (e.g., every hour).

### Supported Languages and Runtimes

- **Directly Supported Languages:** Node.js (JavaScript), Python, Java, C# (.NET Core, PowerShell), Ruby.
- **Custom Runtime API:** Enables support for other languages (e.g., Rust, Golang) by implementing the Lambda Runtime API.
- **Containers on Lambda:** Allows deploying Lambda functions as container images. However, for general container workloads, **ECS or Fargate are generally preferred** from an exam perspective. Remember that Lambda containers must implement the Lambda Runtime API.
- **Key Languages to Remember:** Node.js and Python are particularly important.

### Lambda Limits

Understanding Lambda's limitations is crucial for determining its suitability for specific use cases:

- **Memory (RAM):** Up to 10 GB.
- **CPU:** Provisioned proportionally to the allocated RAM. Approximately 2 vCPUs at 1800 MB RAM and 6 vCPUs at 10 GB RAM.
- **Timeout:** Maximum execution duration of **15 minutes**.
- **Temporary Storage (/tmp):** 10 GB per invocation.
- **Deployment Package Size:**
    - Zipped: 50 MB.
    - Unzipped (including layers): 250 MB.
- **Concurrent Executions:** Default soft limit of 1000 per region (can be increased).
- **Container Image Size:** Maximum of 10 GB.
- **Invocation Payload Size:**
    - Synchronous: 6 MB.
    - Asynchronous: 256 KB.

### Concurrency Management

- **Concurrent Executions:** The number of Lambda function instances running simultaneously. Lambda scales automatically up to the regional concurrency limit.
- **Reserved Concurrency:** Allows dedicating a specific number of concurrent executions to a function, ensuring its availability and preventing throttling due to other Lambda functions consuming all regional concurrency.
- **Throttling:** Occurs when the number of concurrent invocations exceeds the configured concurrency limit (either regional or reserved). Throttled requests can be retried. Excessive throttling may warrant a quota increase request.
- **Concurrency Issues (Without Reservation):** Without reserved concurrency, a surge in traffic to one Lambda-integrated service (e.g., ALB) can consume all available concurrency, leading to throttling of other Lambda functions (e.g., behind API Gateway or invoked via SDK/CLI). Reserving concurrency for critical functions mitigates this risk.

### Deployment with CodeDeploy

- **Traffic Shifting:** AWS CodeDeploy can be used to manage traffic shifts between different versions or aliases of a Lambda function.
- **Integration with SAM:** This feature is directly integrated within the AWS Serverless Application Model (SAM) framework.
- **Deployment Strategies:**
    - **Linear:** Gradually shifts traffic over a specified duration (e.g., 10% every N minutes).
    - **Canary:** Shifts a small percentage of traffic (e.g., 10%) for a short period (e.g., 5 minutes). If no issues, all traffic is shifted.
    - **All-at-Once:** Immediate shift of all traffic to the new version.
- **Pre- and Post-Traffic Hooks:** Allow running custom code (Lambda functions) to perform health checks or other validation steps before or after traffic is shifted to the new version, enabling automated rollback in case of failures.

### Monitoring

- **CloudWatch Logs:** Provides detailed execution logs for Lambda functions. Ensure the Lambda execution role has permissions to write to CloudWatch Logs.
- **CloudWatch Metrics:** Offers metrics related to Lambda function invocations, errors, latency, timeouts, concurrency, etc.
- **AWS X-Ray:** Enables tracing of Lambda function invocations to understand the flow of requests and identify performance bottlenecks. To use X-Ray:
    - Enable X-Ray in the Lambda function configuration.
    - Ensure the Lambda execution role has necessary X-Ray permissions.
    - Implement tracing logic in the Lambda function code using the AWS SDK.

## Deep Dive into AWS Lambda Reserved Concurrency

Reserved concurrency in AWS Lambda provides a mechanism to allocate a specific number of concurrent execution slots to a particular Lambda function. This ensures that the function always has the capacity to handle a certain level of traffic without being impacted by the concurrency usage of other Lambda functions within the same AWS account and region.

Here's a more detailed explanation of reserved concurrency:

**Purpose and Benefits:**

- **Guaranteed Capacity:** Reserved concurrency guarantees that the specified number of Lambda function instances will always be available to handle invocations for that particular function. This is crucial for critical functions that require predictable performance and availability.
- **Prevention of Throttling:** By reserving concurrency, you prevent a function from being throttled due to exceeding the regional concurrency limit or contention with other Lambda functions. This ensures consistent performance even during periods of high overall Lambda usage in your account.
- **Isolation:** Reserved concurrency effectively isolates the concurrency pool of a function. Even if other functions in your account experience a surge in invocations, the reserved function will maintain its allocated capacity.
- **Predictable Costs:** While you are not charged for idle reserved concurrency, you are paying for the compute resources consumed during invocations within the reserved limit. This can help in forecasting and managing costs for critical workloads.
- **Prioritization:** Reserved concurrency implicitly prioritizes a function by ensuring it has dedicated resources.

**How it Works:**

- You configure reserved concurrency at the **function level**.
- You specify the **number of concurrent executions** you want to reserve for that function.
- When an invocation request arrives for a function with reserved concurrency, Lambda first checks if the current number of concurrent executions for that function is below the reserved limit.
- If it is below the limit, a new instance is provisioned (if necessary) to handle the invocation.
- If the number of concurrent executions has reached the reserved limit, subsequent invocation requests will be throttled with a `TooManyRequestsException`.

**Use Cases for Reserved Concurrency:**

- **Critical APIs:** Functions powering public-facing APIs that require low latency and high availability. Throttling these APIs can directly impact user experience.
- **Business-Critical Background Jobs:** Functions performing essential background tasks that must complete reliably and within a specific timeframe.
- **Stateful Applications:** Functions that maintain state across invocations and rely on consistent instance availability.
- **Downstream Dependencies with Rate Limits:** Functions interacting with downstream services that have strict rate limits. Reserving concurrency can help control the invocation rate and prevent overwhelming these dependencies.
- **Performance-Sensitive Workloads:** Functions where consistent performance is paramount, and any throttling or delay is unacceptable.

**Considerations and Best Practices:**

- **Capacity Planning:** Accurately estimate the required reserved concurrency based on expected peak load and performance requirements. Over-provisioning can lead to underutilized reserved capacity, while under-provisioning can still result in throttling during high traffic.
- **Monitoring:** Monitor the `ConcurrentExecutions` and `Throttles` metrics for functions with reserved concurrency in CloudWatch to ensure the reserved capacity is appropriate.
- **Regional Limits:** Reserved concurrency counts towards your account's overall regional concurrency limit. You cannot reserve more concurrency than your account's limit allows.
- **Cost Implications:** While you don't pay for idle reserved concurrency, you are committing to having that capacity available. Consider the cost implications of reserving a large amount of concurrency.
- **Integration with Auto Scaling:** Reserved concurrency is a form of manual capacity management. For more dynamic scaling based on actual demand, consider combining it with provisioned concurrency (which pre-initializes function instances) and auto-scaling configurations, if applicable for your workload.
- **Trade-off with On-Demand Scaling:** While reserved concurrency guarantees capacity, Lambda's on-demand scaling is generally efficient for handling fluctuating workloads. Carefully evaluate whether the guaranteed capacity of reserved concurrency outweighs the potential cost savings and flexibility of purely on-demand scaling.

**Example Scenario:**

Imagine you have a critical API endpoint implemented as a Lambda function. During peak hours, this function experiences significant traffic. Without reserved concurrency, a sudden surge in invocations across all your Lambda functions could exhaust your regional concurrency limit, leading to throttling of your critical API.

By configuring reserved concurrency for this API function (e.g., reserving 500 concurrent executions), you ensure that up to 500 concurrent requests to your API can be handled without being affected by the traffic patterns of other less critical Lambda functions in your account. If the number of concurrent requests exceeds 500, only those exceeding requests will be throttled.

In summary, reserved concurrency is a powerful tool for ensuring the availability and predictable performance of critical AWS Lambda functions by dedicating a specific amount of concurrent execution capacity to them. Careful planning and monitoring are essential to effectively utilize this feature.