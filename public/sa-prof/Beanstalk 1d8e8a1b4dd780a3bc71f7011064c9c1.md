# Beanstalk

# **AWS Elastic Beanstalk - Solution Architect Professional Notes**

## **Purpose for Solutions Architect Professional Exam**

- Understand Beanstalk as a platform for re-platforming on-premise applications to AWS.
- Recognize its developer-centric approach to deploying applications.
- Comprehend that it's a managed service wrapping underlying AWS components.

## **Core Concepts**

- **Developer-Centric:** Provides an easy-to-use interface for deploying and managing applications on AWS.
- **Wrapper Service:** Abstracts underlying AWS services like EC2, ASG, ELB, EIP, RDS, etc., into a single view.
- **Full Control:** Users retain control over the configuration of individual underlying components.
- **Deployment Flexibility:** Offers various deployment strategies managed by Beanstalk.
- **Cost:** Beanstalk service itself is free; users pay for the underlying AWS resources consumed.

## **Supported Platforms**

- Go
- Java
- Java with Tomcat (Important for Tomcat application migrations)
- .NET on Windows Server
- Node.js
- PHP
- Python
- Ruby
- Packer

## **Docker Support**

- Single Docker container
- Multicontainer Docker
- Preconfigured Docker
- Enables migration of applications that can be dockerized.

## **Re-platforming Use Case**

- Ideal for migrating existing on-premise applications to AWS.
- Allows running applications as native AWS applications with minimal code changes.
- Focuses on moving the runtime environment to Beanstalk.

## **Managed Service Aspects**

- **Instance Configuration:** Handled by Beanstalk.
- **OS Configuration:** Managed by Beanstalk.
- **Deployment Strategy:** Configurable and executed by Beanstalk.
- **User Responsibility:** Primarily focused on the application code.

## **Architecture Models**

1. **Single-Instance Deployment:**
    - Suitable for development environments.
    - Runs in a single Availability Zone (AZ).
    - EC2 instance with an Elastic IP (for seamless updates).
    - Optional single-AZ Amazon RDS database.
    - Cost-effective for development.
2. **Load Balancer + Auto Scaling Group (ASG):**
    - Recommended for production and pre-production web applications.
    - Multi-AZ deployment for high availability (e.g., ALB).
    - Auto Scaling Group of EC2 instances to handle varying traffic.
    - Multi-AZ RDS deployment (Master/Standby) for database resilience.
3. **Auto Scaling Group Only (Worker Environment):**
    - Suitable for non-web applications in production.
    - Often referred to as a "worker environment".
    - Typically involves an SQS queue and an ASG of EC2 instances processing messages from the queue.
    - Scales based on the SQS queue load.

## **Web Server Environment vs. Worker Environment**

- **Web Server:** Handles incoming HTTP/HTTPS traffic and serves the application to users.
- **Worker Environment:** Designed for processing long-running or resource-intensive background tasks.
- **Decoupling:** Offloading tasks to a worker environment improves the responsiveness and scalability of the web tier.
- **SQS Integration:** Worker environments commonly integrate with SQS for receiving and processing tasks (decoupling).

## **Worker Environment Use Cases**

- Processing videos
- Generating zip files
- Applying complex image filters
- Any task that consumes significant CPU or threads on web servers.

## **Periodic Tasks in Worker Environment**

- Utilize a `cron.yaml` file to define and schedule cron jobs within the worker environment.

## **Typical Beanstalk Architecture**

- **Web Tier:** ALB + Auto Scaling Group (production-like).
- **Worker Tier:** SQS Queue + Auto Scaling Group of EC2 instances.
- Web tier puts long-running tasks into the SQS queue.
- Worker tier instances process tasks from the queue.
- Both tiers are managed by Beanstalk.

## **Blue/Green Deployment**

- **Not a direct Beanstalk feature** but can be implemented with Beanstalk.
- Provides zero downtime and facilitates easier releases.
- Involves creating a new (green) environment with the new application version (v2).
- Validate the green environment.
- Rollback by deleting the green environment if issues arise.
- **Traffic Shifting:**
    - **Weighted Routing (Route 53):** Gradually shift traffic from the old (blue) to the new (green) environment by adjusting weights.
    - **Swap URL (DNS Swap):** Instantly switch all traffic from the blue to the green environment by swapping DNS records.

## **Key Takeaways for the Exam**

- Beanstalk is excellent for migrating and re-platforming on-premise applications.
- It's a strong choice for managing both web server applications and worker tiers for background processing.
- Understand the different architecture models (single instance, web tier, worker tier).
- Be aware of how blue/green deployments can be implemented with Beanstalk for zero-downtime releases.