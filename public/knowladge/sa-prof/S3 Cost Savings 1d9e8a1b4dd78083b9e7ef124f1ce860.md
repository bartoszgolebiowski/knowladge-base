# S3 Cost Savings

## **S3 Cost Savings**

Here's a breakdown of cost-saving strategies for Amazon S3, based on the lecture:

### **S3 Storage Classes**

Choosing the right storage class is crucial for optimizing costs based on data access patterns.

- **S3 Standard - General Purpose:** Default for frequently accessed data.
- **S3 Standard - Infrequent Access (IA):** Lower storage cost but higher retrieval cost for infrequently accessed data.
- **S3 One Zone - Infrequent Access (One Zone IA):** Lowest storage cost among IA options but data loss possible with an Availability Zone (AZ) failure. Suitable for easily recreatable data (e.g., thumbnails).
- **Intelligent-Tiering:** Automatically moves data between frequent and infrequent access tiers based on usage, optimizing costs. Requires a per-object monitoring fee but reduces management overhead.
- **Amazon S3 Glacier Instant Retrieval:** Low-cost archive storage with fast retrieval times (in minutes).
- **Amazon S3 Glacier Flexible Retrieval (formerly S3 Glacier):** Lower cost than Instant Retrieval with flexible retrieval options (expedited, standard, bulk).
- **Amazon S3 Glacier Deep Archive:** Lowest cost storage for long-term archiving with retrieval times ranging from hours to days.

### **S3 Lifecycle Rules**

Automate cost optimization by managing the lifecycle of your objects:

- **Transitioning between storage classes:** Automatically move objects to cheaper tiers (e.g., from Standard to IA, then to Glacier) after a defined period.
- **Object deletion:** Automatically delete objects after a specified timeframe to reduce storage costs.

### **Object Compression**

Reducing the size of objects before storing them in S3 directly translates to lower storage costs.

### **S3 Requester Pays**

Control who pays for data transfer costs associated with accessing your S3 buckets:

- **Default:** Bucket owner pays for storage and all data transfer (uploads and downloads).
- **Requester Pays:** When enabled, the requester pays for the cost of requests and data downloads from the bucket. The bucket owner still pays for storage.
- **Use Case:** Sharing large datasets with numerous external accounts where you don't want to incur the download costs.
- **Implementation:** Requires an S3 bucket policy that enforces Requester Pays. Requesters must be authenticated (using IAM users or roles belonging to their own AWS accounts).
- **Important Note:** If users access the bucket using an assumed cross-account IAM role that resides in *your* account, *you* will still be responsible for the request costs, as the request originates from within your AWS account. To ensure other accounts pay, they must use their own IAM credentials.