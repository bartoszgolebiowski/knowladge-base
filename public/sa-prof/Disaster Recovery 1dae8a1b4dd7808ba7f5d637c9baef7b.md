# Disaster Recovery

Alright, let's break down this comprehensive lecture on Disaster Recovery (DR) on AWS. Here's a structured summary in markdown format, hitting the key points for the AWS Solution Architect Professional exam:

## **Disaster Recovery (DR) on AWS**

Disaster Recovery (DR) is crucial for maintaining business continuity and minimizing the impact of disruptive events. As a Solutions Architect, understanding DR strategies on AWS is essential.

**What is a Disaster?**

Any event that negatively impacts a company's business continuity or finances.

**Types of Disaster Recovery:**

- **On-Premise to On-Premise:** Traditional DR between two physical data centers (expensive).
- **On-Premise to AWS (Hybrid Recovery):** Utilizing AWS as a secondary DR site for on-premise infrastructure.
- **AWS Cloud Region A to AWS Cloud Region B (Full Cloud DR):** Implementing DR strategies entirely within the AWS cloud across different regions.

**Key Terminology:**

- **Recovery Point Objective (RPO):** The maximum acceptable amount of data loss measured in time. It determines how far back in time you need to recover.
- **Recovery Time Objective (RTO):** The maximum acceptable downtime for an application or service after a disaster. It defines how quickly you need to restore service.
    - Smaller RPO and RTO typically lead to higher costs.

**Disaster Recovery Strategies (Ranked by RTO - Lowest to Highest Cost):**

1. **Backup and Restore:**
    - **RPO:** High (depends on backup frequency).
    - **RTO:** High (time to restore data and rebuild infrastructure).
    - **Mechanism:** Regularly backing up data (e.g., to S3, Glacier via Storage Gateway or Snowball) and infrastructure configurations (e.g., AMIs, snapshots). Restore from backups in case of disaster.
    - **Cost:** Relatively low (primarily storage costs).
2. **Pilot Light:**
    - **RPO:** Lower (continuous data replication for critical data).
    - **RTO:** Lower than Backup and Restore (critical core systems are running).
    - **Mechanism:** Maintaining a minimal, always-on version of critical systems in the cloud (e.g., a running RDS instance with replicated data). Upon disaster, provision and scale up other non-critical components (e.g., EC2 instances from AMIs). Use Route 53 for failover.
    - **Cost:** Moderate (cost of running minimal critical services).
3. **Warm Standby:**
    - **RPO:** Lower (continuous data replication).
    - **RTO:** Lower than Pilot Light (a scaled-down but fully functional system is running).
    - **Mechanism:** Having a full system running in the cloud at a minimum capacity (e.g., EC2 Auto Scaling group at minimum size, ELB ready). Replicate data (e.g., to an RDS read replica). Upon disaster, failover DNS (Route 53) and scale up the standby environment.
    - **Cost:** Higher (cost of running a standby environment).
4. **Multi-Site/Hot Site:**
    - **RPO:** Very Low (near real-time replication).
    - **RTO:** Very Low (minutes or seconds).
    - **Mechanism:** Running two fully redundant production environments (on-premise and AWS, or multi-region AWS) in an active-active setup. Traffic can be routed to both (e.g., via Route 53). Failover is seamless.
    - **Cost:** Very High (cost of running two full-scale environments).

**All-Cloud DR (Multi-Region):**

- Similar architectures as above, but implemented across different AWS Regions.
- Leverages services like Aurora Global Database for cross-region replication and failover.

**Disaster Recovery Tips and Technologies:**

- **Backups:**
    - EBS Snapshots, RDS Automated Backups/Snapshots.
    - Store backups in S3, S3 IA, Glacier with Lifecycle Policies.
    - Cross-Region Replication (CRR) for backup redundancy.
    - Snowball or Storage Gateway for transferring on-premise data to the cloud for backup.
- **High Availability (HA):**
    - Route 53 for DNS failover between regions.
    - Multi-AZ deployments (RDS, ElastiCache).
    - EFS (regional), S3 (global).
    - Network Resilience: Site-to-Site VPN as a backup for Direct Connect.
- **Replication:**
    - RDS Cross-Region Replication, Aurora Global Database.
    - Database replication software for on-premise to RDS.
    - Storage Gateway for replicating data.
- **Automation:**
    - CloudFormation/Elastic Beanstalk for rapid environment recreation.
    - CloudWatch Alarms to trigger recovery actions (e.g., EC2 reboot).
    - AWS Lambda for custom automation scripts.
- **Chaos Testing:**
    - Simulating failures in production environments (e.g., Netflix's Simian Army) to ensure resilience and validate recovery procedures.

**Exam Focus:**

The exam will likely present scenarios and ask you to recommend an appropriate DR strategy based on RPO, RTO, and cost considerations. Understanding the trade-offs of each strategy is crucial.