# SNS

# **AWS Solution Architect Professional - Amazon SNS (Simple Notification Service)**

## **Purpose and Goals**

- **Publish/Subscribe (Pub/Sub) Messaging:** Enables a one-to-many communication pattern where a message publisher sends messages to a topic, and multiple subscribers receive those messages.
- **Decoupling:** Separates message producers from message consumers, allowing them to evolve and scale independently.
- **Fan-Out:** Allows a single message to be distributed to multiple different endpoints and services simultaneously.

## **Key Concepts**

- **Topics:** Logical access points and communication channels. Producers send messages to a specific SNS topic.
- **Subscribers:** Entities that are interested in receiving messages published to a topic. They create subscriptions to the SNS topic.
- **Subscriptions:** The association between a topic and an endpoint. Subscribers specify the endpoint type (e.g., email, SMS, SQS queue, Lambda function) to receive messages.
- **Publishers:** Applications or services that send messages to SNS topics using the SNS API (e.g., `Publish`).
- **Endpoints:** The destination for the messages sent to a topic (e.g., email address, phone number, SQS queue ARN, Lambda function ARN, HTTP/HTTPS URL, Kinesis Data Firehose ARN).

## **Scalability and Limits**

- **Subscribers per Topic:** Up to 12,000,000+ subscriptions per topic (limit can change).
- **Topics per Account:** Up to 100,000 topics per account (limit can be increased).
- **Note:** You are generally not tested on specific service limits in the exam, but understanding the high scalability of SNS is important.

## **Subscriber Types (Endpoints)**

SNS can deliver messages to various types of subscribers:

- **Direct User Notifications:**
    - Email
    - SMS (Text Messages)
    - Mobile Push Notifications (via platform-specific services like APNS, GCM/FCM, ADM)
- **AWS Service Integrations:**
    - **Amazon SQS:** Delivers messages to one or more SQS queues.
    - **AWS Lambda:** Triggers a Lambda function with the message payload.
    - **Amazon Kinesis Data Firehose:** Streams messages to destinations like S3, Amazon ES, or Redshift.
    - **HTTP/HTTPS Endpoints:** Sends messages as HTTP POST requests to specified URLs.

## **Integration with AWS Services (Event Sources)**

Many AWS services can directly publish notifications to SNS topics:

- Amazon CloudWatch Alarms
- Auto Scaling Group Notifications
- AWS CloudFormation State Changes
- AWS Budgets
- Amazon S3 Bucket Events
- AWS DMS (Database Migration Service) Events
- AWS Lambda (can publish upon completion or failure)
- Amazon DynamoDB Streams
- Amazon RDS Events
- And many more...

## **How SNS Works**

- **Publishing Messages:** Producers use the AWS SDK to call the `Publish` API action, specifying the target SNS topic ARN and the message payload.
- **Subscription Creation:** Subscribers create subscriptions to a topic, specifying the protocol (e.g., email, sqs, lambda) and the endpoint.
- **Message Delivery:** When a message is published to a topic, SNS replicates and delivers the message to all subscribed endpoints according to the subscription configuration.

## **Direct Publish for Mobile Apps**

- **Platform Applications:** Represent the mobile platform (e.g., APNS for iOS, FCM for Android).
- **Platform Endpoints:** Represent a specific application instance on a device.
- **Publishing to Endpoints:** Producers can directly publish messages to specific platform endpoints for targeted mobile notifications.

## **Security**

- **In-flight Encryption:** Messages are encrypted during transit by default.
- **At-rest Encryption:** Supports encryption of stored messages using AWS KMS keys.
- **Client-side Encryption:** Clients can encrypt messages before publishing, but SNS does not manage the encryption/decryption in this case.
- **IAM Policies:** Control access to SNS API actions (e.g., `Publish`, `Subscribe`, `DeleteTopic`).
- **SNS Access Policies:** Resource-based policies attached to SNS topics, similar to S3 bucket policies. Useful for:
    - **Cross-Account Access:** Allowing principals in other AWS accounts to publish to or subscribe to the topic.
    - **Service Permissions:** Granting permissions to other AWS services (e.g., S3) to publish events to the topic.

In summary, Amazon SNS is a highly scalable and flexible messaging service for implementing decoupled, event-driven architectures using the publish/subscribe pattern. It offers broad integration with other AWS services and various endpoint types, making it a fundamental component for building modern cloud applications.