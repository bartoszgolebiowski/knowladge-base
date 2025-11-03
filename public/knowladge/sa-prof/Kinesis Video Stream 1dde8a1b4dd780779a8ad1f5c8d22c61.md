# Kinesis Video Stream

Alright, let's break down Kinesis Video Streams and its integration with Rekognition.

## **Kinesis Video Streams - Key Concepts**

- **Producers:** Streaming devices (security cameras, body-worn cameras, smartphones, or custom applications using the Kinesis Video Streams Producer Library) that generate video streams.
- **One Stream per Device:** Each streaming device sends its video data to its own dedicated Kinesis Video Stream. So, if you have many cameras, you'll have a corresponding number of video streams.
- **Underlying Storage:** The video data is stored in Amazon S3, but this storage is managed by Kinesis Video Streams, and you don't directly access the S3 buckets.
- **Direct S3 Output Limitation:** You **cannot** directly output the raw video stream data into S3. You need to consume the stream and build a custom solution to send data to S3 if required. This is a key point for the exam.
- **Consumers:** Services or applications that process the video stream. These can include:
    - **EC2 Instances:** For real-time or batch analysis of the video stream.
    - **Amazon S3 (indirectly):** By building a custom consumer application.
    - **AWS Rekognition:** For video analytics like facial detection.
- **Kinesis Video Stream Parser Library:** Used by consumers to read and process data from Kinesis Video Streams.

## **Integration with AWS Rekognition for Video Analytics**

This is a crucial architecture to understand for the exam:

1. **Video Producers** send video data to a **Kinesis Video Stream**.
2. The **Kinesis Video Stream** is configured as an input source for **AWS Rekognition**.
3. **Rekognition** processes the video stream, performing analysis such as facial detection. It compares detected faces against its internal **Rekognition Face Collection** (a database of known faces).
4. **Rekognition** outputs the analysis results (metadata about the video stream, like detected faces and timestamps) as a new **Kinesis Data Stream**.
5. This **Kinesis Data Stream** can then be consumed by various AWS services for further processing and analysis:
    - **EC2 with Kinesis Client Library (KCL)**
    - **Kinesis Data Firehose**
    - **Kinesis Data Analytics**

## **Exam Relevance**

Remember that you can effectively combine **Kinesis Video Streams** and **Rekognition** to perform real-time video analytics. Rekognition can analyze the video stream and output metadata about the analysis into a **Kinesis Data Stream**, which can then be processed by other Kinesis services or EC2 instances. The key is that Rekognition uses its *internal* Face Collection for comparison during this process.