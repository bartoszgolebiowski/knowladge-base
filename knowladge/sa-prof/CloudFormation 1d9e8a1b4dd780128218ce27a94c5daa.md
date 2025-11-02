# CloudFormation

# AWS CloudFormation - Solution Architect Professional Notes

## Core Concepts

- **Infrastructure as Code (IaC):** CloudFormation enables defining and managing AWS infrastructure using code (templates).
- **Portability and Reusability:** Templates can be used across multiple AWS accounts and regions for consistent deployments.
- **Foundation for Other Services:** Underpins services like Elastic Beanstalk, Service Catalog, and SAM.
- **Low-Level Tool:** Other AWS services might leverage CloudFormation for their operations.

## Retaining Data on Stack Deletion

- **Deletion Policy:** Controls what happens to resources when a CloudFormation stack is deleted.
    - `DeletionPolicy: Retain`: Preserves the resource and its data when the stack is deleted. Works on any resource or nested stack.
    - `DeletionPolicy: Snapshot`: Creates a snapshot of the resource (if supported) before deleting it. Applicable to:
        - EBS Volumes
        - ElastiCache Clusters (Redis) and Replication Groups
        - RDS DB Instances and DB Clusters
        - Redshift Clusters
    - `DeletionPolicy: Delete` (Default): The resource is deleted when the stack is deleted.
    - **Exceptions:**
        - `AWS::RDS::DBCluster`: Default Deletion Policy is `Snapshot`.
        - `AWS::S3::Bucket`: Bucket must be empty before the stack can be deleted.

## Custom Resources with Lambda

- **Extending CloudFormation:** Allows managing resources or performing actions not natively supported by CloudFormation.
- **Lambda Backed:** Implemented using AWS Lambda functions.
- **Use Cases:**
    - Managing new AWS services not yet in CloudFormation.
    - Managing on-premise resources.
    - Emptying S3 buckets before deletion.
    - Retrieving AMI IDs dynamically.
    - Any custom logic required during stack creation, update, or deletion.
- **Lifecycle Events:** The Lambda function is invoked on stack creation, update, and deletion events.
- **API Interactions:** The Lambda function needs to be programmed to make API calls to manage the desired resources.

## StackSets

- **Multi-Account and Multi-Region Management:** Enables creating, updating, and deleting stacks across multiple AWS accounts and regions in a single operation.
- **Administrator Account:** Creates and manages the StackSet.
- **Trusted Accounts:** Can create, update, and delete stack instances based on the StackSet.
- **Centralized Management:** Provides a single point of control for deploying consistent infrastructure across an organization.
- **Automatic Deployments:** With AWS Organizations, StackSets can automatically deploy to new accounts as they are created, ensuring baseline configurations.

## Drift

- **Detecting Configuration Changes:** Identifies if the actual configuration of CloudFormation-managed resources has deviated from the configuration defined in the CloudFormation template (manual changes).
- **Resource and Stack Level:** Drift can be detected for an entire stack or individual resources within a stack.
- **Comparison:** CloudFormation compares the expected configuration (from the template) with the current configuration of the resources.

## Secrets Manager Integration

- **Secure Secret Injection:** Demonstrates how to use AWS Secrets Manager to manage and inject secrets into CloudFormation resources (e.g., RDS database passwords).
- **Template Components:**
    1. Generate a secret in Secrets Manager.
    2. Use the `Sub` function to reference and retrieve the secret value within the CloudFormation template.
    3. Pass the retrieved secret to the resource (e.g., `DBInstance`).
    4. Create a secret target attachment to link the secret to the RDS database instance for automatic rotation.

## Resource Imports

- **Onboarding Existing Resources:** Allows bringing existing AWS resources (created outside of CloudFormation) under CloudFormation management without deleting and recreating them.
- **Process:**
    1. Create a CloudFormation template that describes the stack you want to create and the resources you want to import.
    2. Ensure each target resource for import has a unique identifier (e.g., S3 bucket name).
    3. Use the `aws cloudformation import-resources` command to import the resources into a new or existing stack.
- **Requirements:**
    - The template must accurately describe the resources being imported.
    - Each imported resource requires a `DeletionPolicy` defined (any value is acceptable during import).
    - Each imported resource needs a unique identifier.
    - The same resource cannot be imported into multiple stacks.
- **No Recreation:** CloudFormation takes control of the existing resource without deleting or recreating it.