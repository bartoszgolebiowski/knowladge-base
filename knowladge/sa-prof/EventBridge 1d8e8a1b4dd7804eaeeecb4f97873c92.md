# EventBridge

That was an excellent and thorough explanation of Amazon EventBridge! You covered all the key concepts and use cases that are important to understand for the SA Pro exam. Let's recap the main points and add a little extra emphasis:

# **Amazon EventBridge**

## **Overview**

- Formerly known as CloudWatch Events.
- A serverless event bus that enables you to build scalable and event-driven applications.
- Allows you to react to events from AWS services, SaaS applications, and your own applications.

## **Key Capabilities**

- **Scheduling (Cron Jobs in the Cloud):**
    - Schedule events to trigger actions at specific times or intervals (e.g., run a Lambda function every hour).
- **Event-Driven Architecture:**
    - React to event patterns emitted by AWS services.
    - Example: Trigger an SNS notification upon IAM root user sign-in.
- **Destinations:**
    - Supports various target destinations for events, including:
        - Lambda functions
        - SNS topics
        - SQS queues
        - AWS Batch jobs
        - ECS tasks
        - Kinesis Data Streams
        - Step Functions state machines
        - CodePipeline
        - CodeBuild
        - SSM Automation
        - EC2 actions (start, stop, restart)
- **Event Buses:**
    - **Default Event Bus:** Receives events from AWS services.
    - **Partner Event Bus:** Receives events directly from integrated SaaS partners (e.g., Zendesk, Datadog, Auth0). Requires checking the partner list for integrations.
    - **Custom Event Bus:** Allows your own applications to publish events.
- **Event Filtering:**
    - Define rules to filter events based on specific criteria (e.g., events for a specific S3 bucket).
    - EventBridge generates a JSON document representing the event details.
- **Cross-Account Event Bus Access:**
    - Utilize resource-based policies to grant permissions for other AWS accounts to send events to your event bus.
    - Enables centralized event aggregation within an AWS Organization.
- **Event Archiving and Replay:**
    - Archive events (all or a subset based on filters) with indefinite or defined retention periods.
    - Replay archived events for debugging, troubleshooting, and retesting scenarios after fixes.
- **Schema Registry:**
    - Automatically discovers and infers event schemas in your event bus.
    - Provides a schema registry where you can view and download code bindings for various programming languages.
    - Enables developers to understand the structure of events and generate code that can readily process them.
    - Supports schema versioning for iterative application development.
- **Resource-Based Policies:**
    - Control permissions at the event bus level.
    - Allow or deny events from specific AWS accounts or regions.
    - Facilitates the creation of central event buses for event aggregation across accounts.

## **Use Cases**

- Automating operational tasks based on AWS service events.
- Building loosely coupled and scalable microservices.
- Integrating with third-party SaaS applications.
- Implementing security and compliance monitoring (e.g., root user sign-in alerts).
- Creating event-driven workflows and pipelines.
- Centralized logging and auditing of events across multiple accounts.
- Debugging and troubleshooting event-driven applications by replaying archived events.

## **Exam Relevance**

- Understanding the different types of event buses (default, partner, custom).
- Knowing how to create and manage EventBridge rules and event patterns.
- Understanding the various target destinations and their use cases.
- Familiarity with cross-account event bus access and resource-based policies.
- Knowledge of event archiving and replay capabilities for disaster recovery and debugging.
- Understanding the benefits and features of the Schema Registry.

This summary provides a comprehensive overview of Amazon EventBridge based on the provided transcription, highlighting its key features, capabilities, and relevance for the AWS Solution Architect Professional certification.