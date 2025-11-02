# DocumentDB

# **Amazon DocumentDB (with MongoDB compatibility)**

## **Purpose and Goals**

- AWS's fully managed, highly available, and scalable NoSQL document database service.
- Provides compatibility with MongoDB, a popular NoSQL database for storing and querying JSON data.
- Offers a cloud-native alternative to running self-managed MongoDB on AWS.

## **Core Concepts**

![image.png](image%2036.png)

- **MongoDB Compatibility:** Designed to be compatible with MongoDB APIs, allowing users to migrate MongoDB applications to AWS with minimal code changes.
- **Aurora-like Architecture:** Shares a similar architecture to Amazon Aurora, benefiting from its cloud-native design and features.
- **Fully Managed:** AWS handles infrastructure provisioning, patching, backups, and other operational tasks.
- **High Availability:** Built with replication across three Availability Zones (AZs) to ensure data durability and availability.
- **Automatic Scaling:** The underlying storage layer automatically grows in increments of 10 GB as data volume increases.
- **Scalability:** Designed to handle millions of requests per second, providing high throughput for demanding applications.

## **Pricing Model**

- **Pay-as-you-go:** Users are charged based on their actual usage with no upfront costs.
- **Components of Cost:**
    - **On-Demand Instances:** Charged per second with a minimum of 10 minutes. Includes primary instances (for read and write) and replica instances (for read scaling and high availability).
    - **Database I/O:** Charged per million input/output (I/O) operations performed by the instances against the storage layer.
    - **Database Storage:** Charged per GB per month for the actual storage consumed by the data.
    - **Backups:** Backups are stored in Amazon S3 and are charged per GB per month for the storage consumed by the backups.

## **Important Note**

- **No On-Demand Tier:** Unlike some other AWS database services, Amazon DocumentDB is **provisioned**. You explicitly provision instances and pay for them along with storage and I/O. There is no purely on-demand, compute-less tier for DocumentDB.

## **Key Takeaways for the Exam**

- Understand that DocumentDB is AWS's **MongoDB-compatible NoSQL database service**.
- Recognize its **similarity in architecture and benefits to Amazon Aurora** (fully managed, HA, scalable).
- Know that it's designed for storing and querying **JSON data**.
- Understand the **pricing model**, which includes charges for instances, I/O operations, storage, and backups.
- Remember that DocumentDB is **provisioned**, and there is **no purely on-demand tier**.