# Storage Classes

## Amazon S3 Storage Classes

This lecture covered the various storage classes available in Amazon S3, emphasizing their differences in cost, availability, and use cases, which are crucial for the AWS Solution Architect Professional exam.

### Key Concepts: Durability and Availability

- **Durability:** Represents the probability of data loss. Amazon S3 offers **11 nines (99.999999999%) durability** across all storage classes. This means a very low chance of losing an object over a given period.
- **Availability:** Represents the accessibility of the service. This varies depending on the storage class. Higher availability typically comes with a higher cost.

### Amazon S3 Storage Classes

Here's a breakdown of the different S3 storage classes discussed:

- **Amazon S3 Standard - General Purpose:**
    - **Availability:** 99.99%
    - **Use Cases:** Frequently accessed data, big data analytics, mobile and gaming applications, content distribution.
    - **Characteristics:** High availability, low latency, high throughput, sustains two concurrent facility failures.
    - **Cost:** Generally the highest cost.
- **Amazon S3 Standard-Infrequent Access (S3 Standard-IA):**
    - **Availability:** 99.9%
    - **Use Cases:** Less frequently accessed data requiring rapid access when needed, disaster recovery, backups.
    - **Characteristics:** Lower cost than S3 Standard, retrieval charges apply.
- **Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA):**
    - **Availability:** 99.5% (data lost if the Availability Zone (AZ) is destroyed)
    - **Use Cases:** Secondary copies of backups (e.g., on-premises data), data that can be easily recreated.
    - **Characteristics:** High durability within a single AZ, lowest cost among the IA options, retrieval charges apply.
- **Glacier Storage Classes (for archiving and backup with retrieval costs):**
    - **Amazon S3 Glacier Instant Retrieval:**
        - **Retrieval Time:** Milliseconds
        - **Use Cases:** Data accessed infrequently (e.g., once a quarter) requiring immediate access.
        - **Minimum Storage Duration:** 90 days.
    - **Glacier Flexible Retrieval (formerly S3 Glacier):**
        - **Retrieval Options:**
            - Expedited: 1-5 minutes
            - Standard: 3-5 hours
            - Bulk (free): 5-12 hours
        - **Use Cases:** Archiving where retrieval time flexibility is acceptable.
        - **Minimum Storage Duration:** 90 days.
    - **Glacier Deep Archive:**
        - **Retrieval Options:**
            - Standard: 12 hours
            - Bulk: 48 hours
        - **Use Cases:** Long-term data retention with the lowest storage cost and longer retrieval times.
        - **Minimum Storage Duration:** 180 days.
- **Amazon S3 Intelligent-Tiering:**
    - **Availability:** Inherits from the underlying tiers (Frequent and Infrequent Access).
    - **Use Cases:** Data with unknown or changing access patterns.
    - **Characteristics:** Automatically moves objects between access tiers (Frequent Access, Infrequent Access, Archive Instant Access, Archive Access - optional, Deep Archive Access - optional) based on usage. Incurs a small monthly monitoring and auto-tiering fee, no retrieval charges.
    - **Tiers:**
        - Frequent Access (default)
        - Infrequent Access (not accessed for ~30 days)
        - Archive Instant Access (not accessed for ~90 days)
        - Archive Access (configurable, 90+ days)
        - Deep Archive Access (configurable, 180+ days)

### Key Takeaways for the Exam:

- Understand the core difference between **durability** (same across all classes) and **availability** (varies by class).
- Know the **primary use cases** for each storage class.
- Be aware of the **cost implications** (storage cost vs. retrieval cost) for each class.
- Understand the **retrieval time options** for the Glacier storage classes.
- Grasp the concept and benefits of **S3 Intelligent-Tiering** for optimizing storage costs based on access patterns.
- Recognize that storage classes can be set upon object creation and modified manually or automatically using **S3 Lifecycle configurations**.

While specific pricing details are not required to be memorized, understanding the relative cost differences between the tiers is beneficial. The provided diagram illustrating the characteristics of each storage class should be reviewed for a better understanding.