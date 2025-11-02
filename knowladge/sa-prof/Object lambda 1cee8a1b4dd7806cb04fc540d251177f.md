# Object lambda

## **Introduction to S3 Object Lambda**

- **Concept:** Allows you to modify the data retrieved from an S3 object on-the-fly, just before it's returned to the requesting application.
- **Goal:** Transform or redact object data without needing to create and manage separate copies of the data in different S3 buckets.
- **Dependency:** Requires the use of standard S3 Access Points as a foundation.

## **How S3 Object Lambda Works**

1. **Standard S3 Bucket:** You have your original data stored in a regular S3 bucket.
2. **Standard S3 Access Point:** You create a standard S3 Access Point that provides a named network endpoint to your bucket.
3. **Lambda Function:** You write a Lambda function containing the code to perform the desired data transformation or redaction.
4. **S3 Object Lambda Access Point:** You create an S3 Object Lambda Access Point. This access point is configured to:
    - Be associated with your standard S3 Access Point (pointing to the underlying bucket).
    - Invoke your specified Lambda function whenever an object is accessed through the Object Lambda Access Point.
5. **Application Access:** Client applications access data through the **S3 Object Lambda Access Point** instead of directly through the standard S3 Access Point or the bucket itself.
6. **Data Flow:**
    - When an application requests an object via the S3 Object Lambda Access Point:
        - The request is intercepted by the Object Lambda Access Point.
        - The configured Lambda function is invoked.
        - The Lambda function retrieves the original object from the S3 bucket (via the underlying standard S3 Access Point).
        - The Lambda function executes its code to transform or redact the data.
        - The **modified data** is returned by the Lambda function to the S3 Object Lambda Access Point.
        - The Object Lambda Access Point then returns the modified data to the requesting application.

## **Use Case Examples**

- **Data Redaction (PII):**
    - An analytics application needs access to customer data but without Personally Identifiable Information (PII).
    - An S3 Object Lambda is created with a Lambda function that removes or masks PII fields from the object before it's delivered to the analytics application.
    - The analytics application accesses the data through the Object Lambda Access Point and receives the redacted version, while the original data in the S3 bucket remains intact for the E-commerce application.
- **Data Enrichment:**
    - A marketing application wants to enrich product data with customer loyalty information before accessing it.
    - An S3 Object Lambda is created with a Lambda function that retrieves product data, queries a customer loyalty database, and merges the relevant information into the object.
    - The marketing application accesses the enriched data through its dedicated Object Lambda Access Point.
- **Data Transformation:**
    - Converting data formats on-the-fly (e.g., XML to JSON).
    - Resizing and watermarking images dynamically based on the requester or application.

## **Benefits of S3 Object Lambda**

- **Avoid Data Duplication:** Eliminates the need to create and manage multiple copies of the same data with different transformations or redactions. This saves storage costs and simplifies data management.
- **Centralized Data Management:** The original, canonical data remains in a single S3 bucket.
- **On-Demand Transformation:** Data is modified only when it's accessed, ensuring that the transformations are always up-to-date based on the Lambda function's logic.
- **Simplified Application Logic:** Client applications only need to interact with the Object Lambda Access Point and receive the desired data format or content directly. They don't need to perform the transformations themselves.
- **Granular Access Control:** You can create different Object Lambda Access Points with different associated Lambda functions, providing tailored views of the data for various applications or user groups.

## **Key Takeaways for S3 Object Lambda**

- Extends the functionality of standard S3 Access Points.
- Leverages AWS Lambda for serverless data transformation and redaction during retrieval.
- Enables multiple applications to access modified versions of the same underlying S3 object without data duplication.
- Provides a powerful mechanism for data virtualization and on-demand processing within S3.
- Key use cases include PII redaction, data enrichment, and format conversion.