# CodeDeploy

# AWS CodeDeploy - Solution Architect Professional Notes

## Purpose for Solutions Architect Professional Exam

- Understand how CodeDeploy works for deploying applications to various AWS compute services.
- Focus on deployments to EC2, Auto Scaling Groups (ASG), ECS, and Lambda.
- Recognize its role in automating application deployments and updates.

## Core Concepts

- **Managed Deployment Service:** Automates application deployments to various AWS environments.
- **Agent-Based (EC2/On-Premise):** Requires a CodeDeploy agent to be running on target EC2 instances.
- **Integration with AWS Services:** Seamlessly integrates with EC2, ASG, ECS, and Lambda.
- **Deployment Strategies:** Offers different strategies for controlling the speed and impact of deployments (e.g., AllAtOnce, HalfAtATime, Blue/Green, Canary).
- **AppSpec File (`appspec.yml`):** Defines the deployment actions, lifecycle events (hooks), and files to be deployed.
- **Deployment Group:** A set of target instances (EC2, ECS, Lambda functions) for a deployment.

## CodeDeploy with EC2

- **In-Place Updates:** Updates the application directly on the existing EC2 instances.
- **Process:**
    1. CodeDeploy takes a batch of instances offline.
    2. The application on those instances is updated to the new version.
    3. Optional lifecycle event hooks are executed (e.g., for testing).
    4. The updated instances are brought back online.
    5. This process repeats for the remaining instances based on the deployment strategy.
- **Example (HalfAtATime):** With four EC2 instances (V1), two are taken offline, updated to V2, and brought back online. Then the other two are updated.
- **Lifecycle Event Hooks:** Allow running scripts at various stages of the deployment to validate the new version.

## CodeDeploy with Auto Scaling Groups (ASG)

- **In-Place Updates (Similar to EC2):** Updates the existing instances within the ASG. New instances launched by the ASG during deployment will also receive the new application version.
- **Blue/Green Deployment:**
    1. A new ASG with the new application version is created.
    2. Traffic is gradually shifted from the old ASG to the new ASG using an Elastic Load Balancer (ELB/ALB).
    3. Allows for testing the new version with a subset of traffic.
    4. The old ASG can be kept for a rollback period and then terminated.
    5. Requires an ELB/ALB.
    6. New EC2 instances are created in the new ASG, ensuring a clean environment for the new version.

## CodeDeploy with AWS Lambda

- **Traffic Shifting:** Leverages the traffic shifting capabilities of Lambda aliases.
- **Process:**
    1. CodeDeploy creates a new version of the Lambda function (V2).
    2. Initially, the alias points 100% to the old version (V1).
    3. **Pre-Traffic Hook (Optional):** A separate Lambda function can be executed to run tests against the V2 function before traffic is shifted.
    4. Traffic is gradually shifted from V1 to V2 on the Lambda alias.
    5. **CloudWatch Alarms:** Can be configured to automatically trigger a rollback to V1 if alarms are triggered during traffic shifting.
    6. **Post-Traffic Hook (Optional):** Another Lambda function can be executed to run tests after all traffic has been shifted to V2.
    7. Once complete, the alias points 100% to the V2 function.
- **Serverless Application Model (SAM):** Deploying new Lambda versions through SAM natively uses CodeDeploy for deployments.

## CodeDeploy with Amazon ECS and AWS Fargate

- **Blue/Green Deployments:** Supported for ECS services. Configuration is done within the ECS service definition (not directly in the CodeDeploy console).
- **Process:**
    1. A new task set with the new task definition is created.
    2. Traffic is rerouted from the old task set to the new task set via the Application Load Balancer (ALB).
    3. **Traffic Shifting:** CodeDeploy manages the gradual shifting of traffic to the new task set.
    4. **Stability Check:** CodeDeploy monitors the new task set for stability for a defined period.
    5. **Termination of Old Task Set:** If the new deployment is stable, the old task set is terminated.
- **Canary Deployments:** Another strategy where a small percentage of traffic (e.g., 10%) is shifted to the new task set for a short period (e.g., 5 minutes) before a full deployment.
- **Key Idea:** Leverages ECS service features for managing task sets and traffic.

## Key Takeaways for the Exam

- CodeDeploy automates application deployments to various AWS compute services.
- Understand the different deployment strategies available for each service.
- Recognize the integration points with EC2 agents, ASG lifecycle, Lambda aliases, and ECS service definitions.
- Be familiar with the concepts of in-place updates and blue/green deployments for different services.
- Understand the role of `appspec.yml` and lifecycle event hooks (especially for EC2 and Lambda).
- Know that Lambda deployments use traffic shifting on aliases and support pre/post-traffic hook functions.
- Understand that ECS deployments involve creating new task sets and shifting traffic via the ALB.