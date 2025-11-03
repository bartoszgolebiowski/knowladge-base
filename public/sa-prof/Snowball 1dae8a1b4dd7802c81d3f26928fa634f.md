# Snowball

Alright, let's break down AWS Snowball and its capabilities for data migration and edge computing. Here's a summary in markdown format:

## **AWS Snowball: Secure Data Migration and Edge Computing**

AWS Snowball is a secure and portable device designed to facilitate data collection, processing at the edge, and large-scale data migration into and out of AWS.

**Key Use Cases:**

- **Data Migration:** Transferring large volumes of data (petabytes) when network connectivity is limited, slow, costly, or unstable.
- **Edge Computing:** Processing data locally at the edge where internet access or compute resources are constrained.

**Snowball Edge Device Types:**

There are two main types of Snowball Edge devices, optimized for different use cases:

- **Snowball Edge Storage Optimized:**
    - Primarily designed for **high-capacity data storage and fast data transfer**.
    - Offers a significant amount of storage (e.g., 210 TB).
    - Suitable for large data migration projects.
- **Snowball Edge Compute Optimized:**
    - Optimized for **compute capabilities** at the edge.
    - Offers a smaller amount of storage (e.g., 28 TB) but includes significant compute resources.
    - Ideal for edge computing workloads, running EC2 instances and Lambda functions locally.

**Data Migration with Snowball:**

- **Challenges of Network Transfers for Large Datasets:**
    - Time-consuming for petabyte-scale data over standard network connections.
    - Limited bandwidth.
    - High network costs.
    - Shared and potentially unstable network connections.
- **Snowball Solution:**
    1. Request a Snowball device through the AWS Management Console.
    2. AWS ships the ruggedized Snowball device to your location.
    3. Connect the Snowball to your local network and transfer your data onto it.
    4. Ship the Snowball back to AWS.
    5. AWS imports the data from the Snowball into your specified AWS service (e.g., Amazon S3).
- **Benefits:** Overcomes network limitations for large-scale migrations, providing a secure and efficient transfer method.

**Edge Computing with Snowball Edge:**

- **Scenarios:** Locations with no or limited internet access and/or insufficient local compute power (e.g., remote industrial sites, mobile environments).
- **Snowball Edge Capabilities:**
    - Provides local compute resources.
    - Allows running **EC2 instances** and **Lambda functions** directly on the device.
    - Enables on-site data processing, machine learning inference, media transcoding, and other compute-intensive tasks.
- **Workflow:**
    1. Order a Snowball Edge (Compute Optimized or Storage Optimized depending on needs).
    2. Deploy the device at the edge location.
    3. Process data locally using the onboard compute resources.
    4. Optionally, transfer the processed data back to AWS by shipping the device.
- **Benefits:** Enables real-time data processing and analysis at the source, reducing latency and reliance on internet connectivity.

**In essence, AWS Snowball provides a physical solution for overcoming network constraints in data migration and bringing AWS compute power to edge locations.** It's a valuable tool when dealing with massive datasets or environments with limited or no internet connectivity.