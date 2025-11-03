# Aurora 2

# **AWS Solution Architect Professional - Amazon Aurora Serverless and Advanced Features Notes**

## **Aurora Serverless**

- **Serverless Database:** Offers automatic scaling and instantiation based on actual usage.
- **Ideal Workloads:** Infrequent, intermittent, or unpredictable workloads. Eliminates the need for capacity planning.
- **Pay-Per-Second Pricing:** Cost-effective for variable usage patterns.
- **Shared Storage:** Leverages the same highly available and scalable shared storage volume as provisioned Aurora.
- **Proxy Fleet:** Clients connect to a proxy fleet managed by Aurora, which handles routing and scaling in the backend.
- **Single Endpoint:** Applications connect to a single endpoint, simplifying connectivity management.
- **Data API:**
    - Enables accessing Aurora Serverless via secure HTTPS endpoints.
    - Allows running SQL statements without establishing traditional JDBC/ODBC connections.
    - Simplifies application development by removing the need for persistent connection management.
    - Authorization is handled by verifying the application's IAM permissions to access the underlying database credentials stored in AWS Secrets Manager.
    - Applications need IAM permissions for Aurora Serverless Data API and access to the relevant Secrets Manager secret.

## **RDS Proxy for Aurora**

- **Connection Pooling:** Similar benefits to RDS Proxy for standard RDS, managing connections to the Aurora Primary Instance.
- **Read-Only Proxy:** Specifically, RDS Proxy can be configured to front the read-only endpoints of Aurora Read Replicas.
- **Architecture:** Allows Lambda functions or other read-heavy applications to connect to a dedicated, scalable read endpoint managed by RDS Proxy, offloading connection management from the application.

## **Aurora Global Database**

- **Cross-Region Replication:** Provides easy setup for disaster recovery.
- **Primary and Secondary Regions:** Defines a primary region for read and write operations and up to five read-only secondary regions.
- **Low Replication Lag:** Guarantees a replication lag of less than one second between the primary and secondary regions.
- **Scalable Reads:** Up to 16 Read Replicas can be created per secondary region.
- **Reduced Latency:** Improves read latency for users in secondary regions.
- **Fast Failover:** If the primary region fails, a secondary region can be promoted to primary with an RTO of less than one minute.
- **RPO Management (PostgreSQL):** Allows managing the Recovery Point Objective (RPO) for Aurora PostgreSQL to minimize data loss in case of failures.
- **Write Forwarding:**
    - Enables applications in secondary regions to send write operations to their local secondary cluster endpoint.
    - The secondary cluster forwards these write requests to the primary database cluster.
    - Writes are always executed on the primary cluster first, and then changes are replicated to the secondaries.
    - **Benefit:** Simplifies application connectivity by allowing applications in all regions to use their local cluster endpoint for both reads and writes, without needing to know the primary region's endpoint.

## **Migrating to Aurora**

- **From RDS Database Instance:** Two main methods:
    - **Snapshot Restore:**
        1. Create a database snapshot of the RDS instance.
        2. Restore the snapshot to a new Aurora Database Instance.
        - **Benefit:** Relatively quick operation.
        - **Consideration:** Requires a downtime window if the original RDS instance needs to be taken offline for a consistent snapshot or if replicating ongoing changes is a concern.
    - **Create Aurora Read Replica:**
        1. Create an Aurora Read Replica from the existing RDS Database Instance.
        2. Wait for the replication lag to be minimal.
        3. Promote the Aurora Read Replica to become a standalone Aurora Database Instance.
        4. Migrate application traffic from the RDS instance to the new Aurora instance.
        - **Benefit:** Allows for a more gradual migration with minimal downtime, as the application can continue using the RDS instance until the Aurora replica is promoted.

**Key takeaway for the exam:** Understand the use cases and benefits of Aurora Serverless, including the Data API. Know how RDS Proxy can be used with Aurora for connection management, especially for read replicas. Deeply understand the architecture and advantages of Aurora Global Database for global applications and disaster recovery, including the concept of Write Forwarding. Finally, be familiar with the different strategies for migrating existing RDS databases to Aurora.