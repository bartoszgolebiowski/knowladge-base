# ElasticCache

# AWS Solution Architect Professional - Amazon ElastiCache

## Overview of Amazon ElastiCache

- Managed in-memory data store service compatible with Redis and Memcached.
- Provides high-performance, low-latency caching to reduce database load for read-intensive workloads.
- Caches frequently queried or computationally expensive data.
- Can be used as a session store to make applications stateless.
- **Managed Service Benefits:**
    - OS maintenance
    - Patching
    - Optimization
    - Setup and configuration
    - Monitoring
    - Failure recovery
    - Backups (for Redis and Memcached Serverless)
- **Important Note:** Using ElastiCache requires significant application code changes to interact with the cache.

## Use Cases for ElastiCache

1. **Database (DB) Cache:**
    - Application queries ElastiCache first.
    - **Cache Hit:** Data is retrieved from ElastiCache (low latency).
    - **Cache Miss:**
        - Data is read from the primary database (e.g., Amazon RDS).
        - Data is then written to ElastiCache for future requests (**Lazy Loading** strategy).
    - **Benefits:** Reduces load on the database, especially for hot keys or frequently accessed data.
    - **Challenge:** Requires a **cache invalidation strategy** to maintain data consistency between the cache and the database. This is a complex problem.
2. **User Session Store:**
    - In applications running on multiple instances behind a load balancer (without session stickiness).
    - Application writes session data (login status, user preferences, etc.) to ElastiCache.
    - If a user's subsequent request hits a different application instance, the session data can be retrieved from ElastiCache.
    - **Benefits:** Achieves **statelessness** in the application architecture.

## Redis vs. Memcached

This is a critical comparison for the exam.

### Redis

- **High Availability:**
    - Multi-AZ with **auto failover**.
    - Standby nodes for automatic recovery in case of AZ failure.
    - Ability to create **read replicas** for read scaling and increased availability.
- **Persistence:**
    - **Persistent data** through options like Append-Only File (AOF).
    - **Backup and Restore** features.
    - More like a traditional database in terms of data durability.
- **Architecture:** Replication-focused. Data is typically replicated between Redis instances.
- **Key Features to Remember:** **Replication, High Availability, Persistence, Backup/Restore.**

### Memcached

- **Scalability through Sharding:**
    - Multiple nodes are used for **partitioning and data sharding**, not primarily for replication.
    - Data is distributed across multiple Memcached nodes.
- **Non-Persistent Cache:**
    - Data is **transient**. If a Memcached node fails, the data on that node is lost.
- **Backup and Restore:** Available for the **serverless version** of Memcached, but not the self-managed version.
- **Architecture:** Sharding-focused. Data is spread across nodes.
- **Key Features to Remember:** **Sharding, Non-Persistent (generally), Multi-threaded Architecture.**

### Key Differences Summarized

| Feature | Redis | Memcached |
| --- | --- | --- |
| **High Availability** | Multi-AZ with Auto Failover, Read Replicas | Not inherently Multi-AZ in the same way |
| **Data Persistence** | Persistent (AOF, RDB) | Generally Non-Persistent (transient data) |
| **Data Replication** | Primary mechanism for HA | Not the primary mechanism; used for sharding |
| **Data Partitioning** | Supported, but HA is primary focus | Primary mechanism for scaling |
| **Backup/Restore** | Yes | Yes (Serverless only) |
| **Architecture** | Replication-focused | Sharding-focused, Multi-threaded |
| **Use Cases** | Session stores, caching where HA/persistence are important | Simple caching for high-traffic websites |

Understanding these differences is crucial for choosing the appropriate ElastiCache engine based on the specific requirements of a solution architecture.