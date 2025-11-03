# Route 53 Hosted Zones

## Hosted Zones

- **Definition:** A container for records that define how to route traffic to a domain and its subdomains.
- **Types:**
    - **Public Hosted Zones:**
        - Allow the internet to resolve records for public domains.
        - Targets can be:
            - Public IP of an EC2 Instance
            - Public IP of an Application Load Balancer (ALB)
            - CloudFront distribution
            - S3 Bucket website
    - **Private Hosted Zones:**
        - Can only be resolved from within your Virtual Private Cloud (VPC).
        - Allows defining private URLs.
        - Very helpful for linking to:
            - Private IP of EC2 Instances
            - Private IP of Database Instances
- **Private Hosted Zones with Private DNS:**
    - Require enabling two VPC settings:
        - `enableDnsHostnames`
        - `enableDnsSupport`

## DNS Security Extensions (DNSSEC)

- **Purpose:** A protocol for securing DNS traffic by verifying DNS data integrity and origin.
- **Protection:** Helps protect against Man in the Middle (MITM) attacks on DNS.
- **Route 53 Support:**
    - DNSSEC for Domain Registration
    - DNSSEC Signing
- **Limitation:** Only works with Public Hosted Zones.

## Using Route 53 with a 3rd Party Registrar

- You can buy your domain outside of AWS and still use Route 53 as your DNS provider.
- **Configuration:** Update the NS records at your registrar to point to the AWS name servers provided by Route 53.

## Health Checks

- **Public Health Checks:** Used to monitor the health of public endpoints (e.g., ALBs in different regions).
- **Integration with DNS Records:** Health Checks can be linked to specific DNS records to enable automatic DNS Failover.
- **Types of Health Checks:**
    - **Endpoint Health Checks:** Monitor the health of an application, server, or other AWS resource.
        - Health Checkers worldwide make HTTP(S) requests to a specified health route.
        - Requires a Public Endpoint.
        - Health Check passes if the endpoint responds with 200 or 300 status codes.
        - Can be configured to pass/fail based on specific text (first 5120 bytes) in the response.
    - **Calculated Health Checks:** Monitor the status of other Health Checks.
        - Combine up to 256 Child Health Checks into a Parent Health Check.
        - Supports OR, AND, and NOT conditions.
        - You can specify the number of child health checks that need to pass for the parent to pass.
        - **Use Case:** Performing maintenance on a website without causing all health checks to fail.
    - **CloudWatch Alarm Health Checks:** Monitor the state of a CloudWatch Alarm.
        - Provides full control over the monitoring criteria (e.g., DynamoDB throttles, RDS alarms, custom metrics).
        - Particularly helpful for monitoring private resources.
- **CloudWatch Metrics:** All Health Checks publish CloudWatch metrics.

## Monitoring Private Hosted Zones

- Health Checkers are outside the VPC and cannot directly access private endpoints (EC2 instances, on-premises resources).
- **Solution:**
    1. Create a CloudWatch Metric related to the health of the private resource.
    2. Associate a CloudWatch Alarm with the metric.
    3. Create a Route 53 Health Check that monitors the CloudWatch Alarm.

## Multi-Region Failover with RDS Example

![image.png](image%2032.png)

- **Scenario:** Main RDS database in one region (e.g., us-east-1) with asynchronous replication to another region (e.g., us-west-2).
- **Two Options for Health Monitoring:**
    1. **EC2 Instance with Health Endpoint:**
        - Set up an EC2 Instance to monitor the database health.
        - The EC2 instance exposes an HTTP `/health-db` endpoint.
        - Create a Route 53 Endpoint Health Check targeting this EC2 instance.
    2. **CloudWatch Alarm Health Check (Preferred):**
        - Define a CloudWatch Alarm to monitor a relevant database metric.
        - Link the CloudWatch Alarm to a Route 53 Health Check.
- **Automated Failover Process (using CloudWatch Alarm Health Check):**
    1. The Route 53 Health Check monitors the CloudWatch Alarm.
    2. If the Health Check fails (indicating an issue with the primary database), it can trigger a CloudWatch Alarm (different alarm based on the health check status).
    3. This CloudWatch Alarm triggers an SNS Topic or CloudWatch Event.
    4. The SNS Topic or CloudWatch Event invokes a Lambda function.
    5. The Lambda function updates the DNS records in Route 53 to point the application to the secondary region (us-west-2).
    6. The Lambda function promotes the Read Replica in the secondary region to become the new primary.