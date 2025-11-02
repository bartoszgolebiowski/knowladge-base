# API Gateway

## **Core Functionality**

- Exposes REST APIs to clients.
- Proxies requests to various backends:
    - Lambda functions (most common).
    - HTTP endpoints.
    - AWS services.
- Serves as the initial point of contact for clients.

## **Advantages of Using API Gateway**

- **API Versioning:** Publish and manage multiple API versions for seamless client migration.
- **Authorization:** Integrates with various security mechanisms (IAM, Lambda Authorizers, Cognito).
- **Traffic Management:** Define API keys, usage plans, and throttling to control access and usage.
- **Scalability:** Serverless architecture ensures automatic scaling without server management.
- **Request and Response Transformations:** Modify request/response formats for compatibility.
- **OpenAPI Specification:** Publish or import API definitions in OpenAPI (Swagger) format, enabling automatic client library generation.
- **CORS Support:** Handles Cross-Origin Resource Sharing for browser-based security.

## **Important Limits**

- **Timeout:** Maximum request timeout of **29 seconds**. This applies even if the backend Lambda function has a longer timeout.
- **Payload Size:** Maximum request and response payload size of **10 megabytes**. This limitation needs careful consideration for file uploads or large data transfers.

## **Deployment Stages**

- Deploy API changes to multiple named stages (e.g., dev, test, prod).
- Stages can be rolled back to previous deployments, maintaining a history of changes.
- Stages can be configured to point to specific Lambda function aliases (e.g., prod alias pointing to V2).

## **Integrations**

- **HTTP:** Proxy requests to existing HTTP endpoints (on-premises or behind an Application Load Balancer). Useful for adding API Gateway features like rate limiting and authentication.
- **Lambda Functions:** Directly invoke Lambda functions, creating serverless REST APIs.
- **AWS Services:** Expose AWS service APIs (e.g., Step Functions, SQS) through the API Gateway, adding security and management layers.

## **Solution Architecture Considerations: API Gateway and S3 Uploads**

**Inefficient Architecture (Direct S3 Proxy):**

- API Gateway directly proxies requests to the S3 `PutObject` API.
- **Limitation:** Subject to the 10 MB payload size limit, making it unsuitable for large file uploads.

**Efficient Architecture (Pre-Signed URL):**

1. Client application requests an upload.
2. API Gateway invokes a Lambda function.
3. Lambda function generates a **pre-signed URL** for the private S3 bucket.
4. API Gateway returns the pre-signed URL to the client.
5. Client application **directly uploads the file to S3** using the pre-signed URL, bypassing the API Gateway's payload limit.
- **Advantages:** Allows uploading files of any size, leverages API Gateway features while respecting component limitations.

## **Endpoint Types**

- **Edge-Optimized (Default):** Requests are routed through CloudFront Edge locations, improving latency for global clients. The API Gateway itself resides in a single AWS region.
- **Regional:** API Gateway is deployed in a specific AWS region. Suitable for clients primarily within that region. Can be combined with CloudFront for more control over caching and distribution.
- **Private:** Accessible only within a Virtual Private Cloud (VPC) via Elastic Network Interfaces (ENIs). Requires resource policies to control access.

## **Caching**

- Cache API responses at the API Gateway level to reduce backend load and improve latency.
- Gateway cache checks for available responses before forwarding requests to the backend.
- **Time to Live (TTL):** Configurable per stage (default 300 seconds). Can be set to 0 (no cache) or up to one hour.
- **Method-Level Overrides:** Cache settings can be customized for individual API methods.
- **Client-Side Invalidation:** Clients can bypass the cache using the `Cache-Control: max-age=0` header (requires proper IAM authorization).
- **Cache Flushing:** Entire cache can be invalidated programmatically.
- **Encryption:** Cache data can be encrypted.
- **Capacity:** Configurable cache capacity ranging from 0.5 GB to 237 GB.

## **Error Handling**

- **4xx Errors (Client Errors):**
    - `400 Bad Request`: Invalid request format.
    - `403 Access Denied`: Insufficient permissions or WAF blocking.
    - `429 Too Many Requests`: Quota exceeded or throttling applied by API Gateway.
- **5xx Errors (Server-Side Errors):**
    - `502 Bad Gateway Exception`: Backend Lambda function returned an invalid output or out-of-order invocations under heavy load.
    - `503 Service Unavailable Exception`: Backend service is unable to respond.
    - `504 Integration Failure`: Backend endpoint request timed out (likely due to the API Gateway's 29-second timeout).

## **Security**

- **SSL Certificates:** Load SSL certificates onto the API Gateway and use Route 53 CNAME for custom domains.
- **Resource Policies:** Control access to the API based on AWS accounts, IPs, CIDR blocks, VPCs, or VPC endpoints.
- **IAM Execution Roles:** Define permissions for the API Gateway to interact with backend services (e.g., invoking Lambda functions).
- **CORS (Cross-Origin Resource Sharing):** Configure to allow specific domains to make requests to the API from web browsers.
- **Authentication:**
    - **IAM-based Access (SigV4):** Secure access for users and services within your AWS infrastructure using IAM credentials in the request header.
    - **Lambda-based Authorizers (Custom Authorizers):** Use a Lambda function to verify custom authentication tokens (e.g., OAuth, SAML). Requires implementing the verification logic in the Lambda function.
    - **Cognito User Pool Integration:** Leverage Cognito User Pools for user authentication. Clients authenticate with Cognito, obtain a token, and pass it to the API Gateway, which automatically verifies it. The user's identity can be passed to the backend Lambda function.

## **Logging, Monitoring, and Tracing**

- **CloudWatch Logs:**
    - Stage-level logging for errors and informational messages.
    - Option to log full request and response data for troubleshooting.
- **Access Logs:** Customizable logs of API requests, which can be sent to CloudWatch Logs or Kinesis Data Firehose.
- **CloudWatch Metrics:** Stage-level metrics, including:
    - Integration latency.
    - Overall latency.
    - Cache hit count.
    - Cache miss count.
    - Enable detailed metrics for more granular insights.
- **AWS X-Ray:** Provides tracing capabilities to analyze request flow through the API Gateway, including latency and errors. Integrating X-Ray with backend services like Lambda functions offers end-to-end visibility.