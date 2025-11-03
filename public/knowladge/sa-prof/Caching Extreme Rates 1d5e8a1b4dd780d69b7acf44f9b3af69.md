# Caching Extreme Rates

# AWS Solution Architect Professional - Handling Extremely High Request Rates on AWS

This lecture focuses on the scalability limits of various AWS services within a typical solution architecture and highlights the importance of caching at different layers.

## Architectural Layers and Scalability Limits

![image.png](image%2033.png)

Let's examine the potential bottlenecks when dealing with extremely high request rates, moving from the client towards the data layer.

**1. Client:**

- **Client Caching:** Implement caching on the client side to reduce the number of requests hitting your infrastructure.

**2. DNS (Amazon Route 53):**

- **Scalability:** Global DNS service designed to handle extremely high request rates. Generally not a bottleneck.

**3. Content Delivery Network (Amazon CloudFront):**

- **Scalability:** Can easily handle **100,000+ requests per second**.
- **Origin Shield:** Helps reduce load on the origin by centralizing caching.
- **Caching Capability:** Crucial for offloading requests from the origin.

**4. Origin (e.g., Application Load Balancer - ALB, API Gateway):**

- **Application Load Balancer (ALB):** Scales tremendously and seamlessly (no more significant warm-up issues).
- **API Gateway:**
    - **Soft Limit:** **10,000 requests per second** (can be increased).
    - **Caching Capability:** Implement caching at the API Gateway level to reduce backend load.

**5. Compute Layer:**

- **EC2 with Auto Scaling Group (ASG) / ECS on EC2:**
    - **Scaling:** Scales well but can be slower due to instance bootstrapping after VM creation.
- **AWS Fargate:**
    - **Scaling:** Faster scaling compared to EC2 as it launches Docker containers directly.
    - Leverages AWS Global Infrastructure for potentially faster scaling.
- **AWS Lambda:**
    - **Concurrent Executions:** Soft limit of **1,000 concurrent executions per region** (can be increased).
    - **Caching:** No inherent caching capability within the Lambda compute itself.

**6. Database Layer:**

- **Relational Databases (Amazon RDS, Amazon Aurora, Amazon Elasticsearch Service):**
    - **Scalability:** Provisioned databases, scaling can be more challenging (except potentially Aurora with its auto-scaling features, though still provisioned capacity).
- **NoSQL Database (Amazon DynamoDB):**
    - **Scalability:** Excellent scalability with **autoscaling and on-demand scaling** for reads and writes. Can handle very high throughput.
- **In-Memory Caching:**
    - **Amazon ElastiCache (Redis):** Scales up to **200 nodes**.
    - **Amazon ElastiCache (Memcached):** Scales up to **20 nodes** with sharding.
    - **Amazon DynamoDB Accelerator (DAX):** Scales up to **10 nodes** (primary and replica) for caching DynamoDB reads.

**7. Storage Layer:**

- **Amazon Elastic Block Store (EBS):**
    - **IOPS Limits:** `gp2` up to **16,000 IOPS**, `io1` up to **64,000 IOPS**.
    - **Caching:** Can be used as a local cache on EC2 instances.
- **EC2 Instance Store:**
    - **IOPS Limits:** Can achieve **millions of IOPS** (local to the instance, ephemeral).
    - **Caching:** Commonly used as a high-performance local cache.
- **Amazon Elastic File System (EFS):**
    - **Scalability:** Performance scales with the number of files in the General Purpose mode.
    - **Max I/O / Provisioned Throughput:** Option to provision higher IOPS regardless of file count.

**8. Decoupling Services:**

- **Amazon Simple Notification Service (SNS) & Amazon Simple Queue Service (SQS):**
    - **Scalability:** Virtually unlimited scale.
- **SQS FIFO (First-In, First-Out) Queues:**
    - **Throughput:** Approximately **3,000 requests per second with batching**, **300 requests per second without batching**.
- **Amazon Kinesis:**
    - **Scalability:** Provisioned capacity based on shards.
    - **Throughput per Shard:** Roughly **1 MB/s in, 2 MB/s out**.

**9. Static Content:**

- **Amazon S3 via Amazon CloudFront:**
    - **S3 Performance:** Around **3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per prefix per second**.
- **AWS Key Management Service (KMS):**
    - **Limits:** Can be a bottleneck if using SSE-KMS encryption heavily on S3. Soft limit of around **10,000 API calls per region** (varies by region).

## Key Takeaways for High Request Rates

- **Caching is Paramount:** The earlier you can cache requests in the architecture (client, CDN, API Gateway, in-memory data stores), the less load on your backend and the lower the latency.
- **Understand Service Limits:** Be aware of the soft and hard limits of each AWS service to identify potential bottlenecks under extreme load.
- **Choose Scalable Services:** Opt for services designed for high scalability (e.g., Route 53, CloudFront, ALB, DynamoDB, SNS, SQS).
- **Statelessness:** Design your application to be stateless, leveraging services like ElastiCache for session management to allow for horizontal scaling.
- **Asynchronous Processing:** Use decoupling services like SNS and SQS to handle workloads asynchronously and prevent backpressure on your application.
- **Cost Implications:** Services closer to the data layer (on the right side of the architecture) often incur higher costs due to computation and data access. Efficient caching minimizes these costs.
- **Latency Considerations:** Propagating requests deep into the architecture increases latency. Caching closer to the client improves response times.

This overview emphasizes the importance of a well-architected solution that strategically employs caching and leverages the inherent scalability of various AWS services to handle extremely high request rates efficiently and cost-effectively.