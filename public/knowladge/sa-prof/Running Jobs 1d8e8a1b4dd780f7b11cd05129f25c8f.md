# Running Jobs

# **Viewing Running Jobs on AWS - Architectural Strategies**

![image.png](image%2035.png)

## **Ineffective Strategy (Avoid)**

- **Provisioning an EC2 Instance for Long-Running CRON Jobs:**
    - **Pros:** Familiar to those with CRON experience.
    - **Cons:**
        - **Not Highly Available:** Single point of failure.
        - **Not Scalable:** Limited by the instance's capacity.
        - **Poor Reliability:** Job failure if the EC2 instance goes down.
    - **Recommendation:** As a Solution Architect, you should **not** recommend this approach for production workloads.

## **Effective Strategies**

1. **Amazon EventBridge and Lambda:**
    - **Concept:** Serverless CRON jobs. EventBridge rules trigger Lambda functions on a schedule.
    - **Pros:**
        - **Serverless:** No infrastructure to manage.
        - **Scalable:** Lambda automatically scales based on invocations.
        - **Highly Available:** Lambda functions run across multiple AZs.
    - **Cons:**
        - **Execution Time Limits:** Lambda functions have maximum execution durations.
        - **Resource Limits:** Lambda functions have limitations on memory and compute.
    - **Use Case:** Suitable for short to medium duration, event-driven tasks. AWS often recommends this approach when feasible.
2. **Reactive Workflows with Lambda:**
    - **Concept:** Trigger Lambda functions in response to events within AWS services.
    - **Event Sources:**
        - **Amazon EventBridge:** For reacting to events across various AWS services.
        - **Amazon S3:** Object creation, deletion events, etc.
        - **API Gateway:** Invoking Lambda upon API requests.
        - **Amazon SQS & SNS:** Processing messages and notifications.
        - **Others:** Many other AWS services can trigger Lambda functions.
    - **Pros:**
        - **Event-Driven:** Only runs when needed, optimizing resource utilization.
        - **Scalable and Highly Available:** Inherits Lambda's benefits.
        - **Decoupled Architecture:** Services react to events without direct dependencies.
    - **Use Case:** Ideal for processing data changes, responding to API calls, and building asynchronous workflows.
3. **AWS Batch:**
    - **Concept:** Managed service for running batch computing workloads in the AWS Cloud.
    - **Integration with EventBridge:** EventBridge can trigger Batch jobs on a schedule.
    - **Pros:**
        - **Designed for Longer Running Jobs:** Handles workloads exceeding Lambda's limitations.
        - **Full Docker Container Support:** Allows running any containerized application.
        - **Scalability:** Automatically scales compute resources based on job queue.
    - **Use Case:** Suitable for longer-duration, containerized batch jobs, including scheduled tasks.
4. **AWS Fargate:**
    - **Concept:** Serverless compute engine for containers.
    - **Integration with EventBridge:** EventBridge can target Fargate tasks to run containers on a schedule or in response to events.
    - **Pros:**
        - **Serverless Containers:** No need to manage underlying EC2 instances.
        - **Quick Container Execution:** Efficiently runs containerized workloads.
    - **Cons:**
        - **More Barebones than Batch:** Offers less built-in job management and scalability features compared to AWS Batch.
    - **Use Case:** Running containerized applications and tasks, potentially for scheduled jobs triggered by EventBridge.
5. **AWS EMR (Elastic MapReduce):**
    - **Concept:** Managed Hadoop framework for big data processing.
    - **Step Execution:** Allows defining a series of steps for data processing workflows.
    - **Clustering:** Provisions and manages clusters of EC2 instances for distributed processing.
    - **Pros:**
        - **Designed for Big Data:** Handles large-scale data processing and analytics.
        - **Scalable:** Easily scale the cluster size based on workload.
        - **Cost-Effective for Big Data:** Pay-as-you-go for the cluster duration.
    - **Use Case:** Ideal for long-running big data jobs, ETL processes, and machine learning on large datasets.

## **Summary of Strategies**

| **Strategy** | **Use Case** | **Pros** | **Cons** |
| --- | --- | --- | --- |
| EC2 with CRON | Simple, familiar for some | Easy to understand for CRON users | Not HA, not scalable, unreliable |
| EventBridge + Lambda | Short to medium duration, event-driven tasks | Serverless, scalable, highly available | Execution time and resource limits |
| Reactive Workflows (Lambda) | Event-driven processing | Scalable, HA, cost-effective, decoupled | Subject to Lambda limits |
| EventBridge + AWS Batch | Longer running, containerized batch jobs | Handles long durations, container support, scalable | More complex than Lambda |
| EventBridge + AWS Fargate | Running containers | Serverless containers, quick execution | Less job management than Batch |
| AWS EMR | Big data processing, long-running analytics | Scalable for large datasets, cost-effective for big data | Designed for big data workloads, might be overkill for smaller tasks |