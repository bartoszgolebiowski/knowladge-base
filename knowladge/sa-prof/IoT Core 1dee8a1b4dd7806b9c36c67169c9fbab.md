# IoT Core

## **AWS IoT Core**

- Enables easy connection of IoT (Internet of Things) devices to the cloud.
- Provides a serverless, secure, and scalable solution for connecting billions of devices and trillions of messages.
- Facilitates the publishing and subscribing of messages between devices and applications.
- Offers integrations with various AWS services like Lambda, S3, and SageMaker for building IoT applications.

### **Key Concepts**

- **IoT Topics:** Similar to SNS Topics, they ingest data from IoT devices. Common protocols like MQTT are used for message reception.
- **IoT Rules:** Define actions to be taken based on the messages received on IoT Topics.
- **Actions:** IoT Rules can trigger actions involving other AWS services, including:
    - Kinesis
    - DynamoDB
    - SQS
    - MSK
    - SNS
    - S3
    - Lambda

### **Integration with Kinesis Data Firehose**

- IoT Core can send MQTT messages in near real-time to Amazon Kinesis Data Firehose.
- Kinesis Data Firehose allows for optional transformation of these messages using Lambda functions.
- Processed messages can then be persisted in destinations like:
    - Amazon S3
    - Redshift
    - Amazon OpenSearch