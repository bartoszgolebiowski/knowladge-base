# Step Functions

# **AWS Solution Architect Professional - Step Functions**

## **Purpose and Goals of Step Functions**

- Build serverless visual workflows to orchestrate AWS services, primarily Lambda functions, but also others.
- Represent workflows as state machines.
- Offer features like sequential and parallel actions, conditions, timeouts, and error handling.
- Maximum workflow execution time: **one year** (for Standard Workflows).
- Capability to implement human approval steps.
- **Important Consideration:** Latency can occur between chained Lambda function calls due to information passing.

## **Visual Representation**

- AWS generates a visual graph from the JSON state machine definition.
- Real-time execution status updates (success, failed, canceled, in progress).
- Ability to review the complete execution flow upon completion.

## **Integrations**

- **Optimized Integrations:**
    - AWS Lambda (invoke functions)
    - AWS Batch (run jobs)
    - Amazon ECS (run tasks and wait for completion)
    - Amazon DynamoDB (insert items)
    - Amazon SNS (publish messages)
    - Amazon SQS (publish/send messages)
    - Amazon EMR (launch jobs)
    - AWS Glue (launch jobs)
    - Amazon SageMaker (launch jobs)
    - Step Functions (invoke other workflows)
- **AWS SDK Integration:** Access to **over 200 AWS services** directly from the state machine using standard AWS SDK API calls.

## **Triggering Step Functions**

Multiple ways to initiate a step function state machine:

- AWS Management Console
- AWS SDK
- AWS CLI
- AWS Lambda (using the SDK)
- Amazon API Gateway
- Amazon EventBridge
- AWS CodePipeline
- Step Functions (can invoke other workflows)

## **Applications of Step Functions**

Wide range of use cases, including:

- Processing high-volume messages from SQS with Lambda.
- Training machine learning models involving SageMaker, Lambda, and S3 synchronization.
- Managing batch jobs with Batch and SNS.
- Managing container tasks (e.g., running Fargate tasks based on events).
- General orchestration of tasks and services in AWS.

## **Step Function Tasks**

Key task types to remember for the exam:

- **Lambda Task:** Invokes an AWS Lambda function.
- **Activity Task:** Requires setting up an external HTTP activity worker (e.g., EC2, mobile, on-premise) that polls the Step Functions service for tasks. **Not serverless.**
- **Service Task:** Integrates directly with supported AWS services (Lambda, ECS/Fargate, DynamoDB, Batch, SNS, SQS).
- **Wait Task:** Pauses the workflow for a specified duration or until a specific timestamp.

**Important Note for Exam:** Step Functions **do not directly integrate** with AWS Mechanical Turk. Use **SWF (Simple Workflow Service)** for Mechanical Turk integration.

## **Workflow Types**

### **Standard Workflow**

- **Maximum Duration:** One year.
- **Start Rate:** Approximately 2,000 starts per second.
- **State Transitions:** Approximately 4,000 per second per account.
- **Pricing:** Per state transition.
- **Execution History:** Available for inspection.
- **Execution Semantics:** Exactly-once workflow execution.
- **Use Case:** Longer-running, reliable workflows.

### **Express Workflow**

- **Maximum Duration:** Five minutes.
- **Start Rate:** Over 100,000 starts per second.
- **State Transitions:** Nearly unlimited.
- **Pricing:** Based on the number of executions, duration, and memory consumed (similar to Lambda).
- **Execution History:** Not directly available, but can be inspected via CloudWatch Logs if configured.
- **Execution Semantics:** At-least-once workflow execution.
- **Use Case:** Short-duration, high-throughput workflows.

### **Express Workflow Cases**

- **Synchronous:** Waits for the workflow to complete and returns the result. Useful for orchestrating microservices with immediate responses.
- **Asynchronous:** Starts the workflow and immediately returns a confirmation without waiting for completion. Suitable for tasks that don't require immediate responses or for messaging patterns.

## **Error Handling**

- Implement **retries** and **catch error states** within the state machine definition.
- Use **Amazon EventBridge** to monitor for execution failure events.
- Create EventBridge rules to trigger notifications (e.g., via SNS) upon state machine failures.

## **Solution Architecture with Step Functions**

- Step Functions can be invoked via:
    - SDK and CLI.
    - EventBridge (allowing various AWS services to trigger workflows).
    - API Gateway (using service proxy integration for synchronous or asynchronous invocation).
- Workflows are defined using JSON state machine documents.
- Step Functions provide a visual representation of the workflow.
- Deep integration with various AWS services (Lambda, DynamoDB, SQS, etc.) allows direct interaction without always requiring intermediary Lambda functions.