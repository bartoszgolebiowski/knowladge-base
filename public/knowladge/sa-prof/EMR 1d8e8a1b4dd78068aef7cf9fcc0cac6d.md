# EMR

# **AWS Elastic MapReduce (EMR) - Key Concepts**

## **Purpose and Goals**

- Create Hadoop clusters in the AWS Cloud for big data processing.
- Facilitate migration of on-premise Hadoop workloads to AWS.
- Leverage cloud elasticity for scalable and cost-effective data processing.

## **Core Concepts**

- **Hadoop Clusters:** EMR provisions and manages Hadoop clusters composed of EC2 instances.
- **Elasticity:** Scale clusters up to hundreds of EC2 instances for processing and down when done to save costs.
- **Ecosystem Integration:** Supports various big data frameworks like Apache Spark, HBase, Presto, Flink, and Hive.
- **Simplified Provisioning:** Automates the creation and configuration of EC2 instances for Hadoop clusters.
- **Auto Scaling:** Integrates with CloudWatch for automatic scaling of the cluster based on demand.

## **Use Cases**

- Data processing
- Machine learning
- Web indexing
- Big data analytics
- Any large-scale data processing needs

## **Integrations**

- **VPC:** EMR clusters are launched within a Virtual Private Cloud (VPC).
- **Availability Zone (AZ):** Clusters reside within a single Availability Zone.
- **EBS Volumes:** EC2 instances within the cluster use EBS volumes for storage.
- **HDFS (Hadoop Distributed File System):** Provides temporary, local storage on the EBS volumes of the EC2 instances.
- **EMRFS:** A native integration with Amazon S3 for durable, multi-AZ storage of data.
    - S3 offers permanent storage and supports server-side encryption.
    - Recommended for long-term data retention.
- **DynamoDB:** Apache Hive on EMR can directly read data from DynamoDB tables for analysis.

## **Cost Optimization**

- EMR clusters are composed of EC2 instances with different node types:
    - **Master Node:** Manages the cluster, coordinates other nodes, monitors health. Must be long-running.
    - **Core Node:** Runs tasks and stores data. Must be long-running.
    - **Task Node:** Executes tasks only. Can be used with Spot Instances and is optional.
- **Purchasing Options:**
    - **On-Demand Instances:** Reliable, predictable, never terminated. Suitable for master and core nodes.
    - **Reserved Instances:** Significant cost savings for long-term usage (minimum 1 year). EMR automatically utilizes them. Ideal for master and core nodes.
    - **Spot Instances:** Less reliable (can be terminated), but cost-effective for non-critical workloads like task nodes.
- **Deployment Models:**
    - **Long-Running Clusters:** Suitable for continuous workloads, benefits from Reserved Instances.
    - **Transient (Temporary) Clusters:** Launched for specific analysis tasks and terminated afterward for cost savings.

## **Instance Configuration**

- **Uniform Instance Groups:**
    - Selects a single instance type and purchasing option for each node type (master, core, task).
    - Supports auto scaling.
    - Example: Master (on-demand/spot), Core (2 instances, on-demand/spot), Task (various instance types, on-demand/spot).
- **Instance Fleet:**
    - Selects a target capacity and mixes instance types and purchasing options.
    - Offers more flexibility in choosing cost-effective instances.
    - Supports node auto scaling (as of the transcription).
    - Allows specifying a mix of on-demand and spot instances with different instance types for each node type.
    - Similar to a "spot fleet" for EMR.

## **Key Takeaways for the Exam**

- Understand the purpose and benefits of using EMR for big data processing and Hadoop migration.
- Know the different components of an EMR cluster (master, core, task nodes).
- Be familiar with storage options: temporary (HDFS on EBS) vs. durable (EMRFS on S3).
- Understand cost optimization strategies using different EC2 purchasing options (On-Demand, Reserved, Spot) and their suitability for different node types.
- Differentiate between uniform instance groups and instance fleets for configuring EMR clusters.
- Remember the integration with VPC, single AZ deployment, and potential data loss in case of AZ failure.
- Be aware of the integration with other AWS services like S3 and DynamoDB.