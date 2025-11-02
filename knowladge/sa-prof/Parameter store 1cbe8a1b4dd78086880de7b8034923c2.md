# Parameter store

## **Purpose and Goals**

- Secure, serverless, scalable, and durable storage for configuration and secrets.
- Optional encryption using AWS KMS for secrets management.
- Simplified management of application configurations.

## **Key Concepts**

- **Secure Storage:** Stores configuration data (plain text) and secrets (encrypted).
- **Encryption:** Integrates with AWS KMS for encrypting parameter values, turning configurations into secrets. Requires appropriate IAM permissions for applications to access KMS keys.
- **Serverless, Scalable, and Durable:** Managed service requiring no infrastructure management.
- **Easy to Use SDK:** Simple integration with applications.
- **Version Tracking:** Maintains a history of parameter updates.
- **Security via IAM:** Controls access to parameters through IAM policies.
- **Notifications with Amazon EventBridge:** Sends notifications for parameter changes and policy events.
- **CloudFormation Integration:** Allows CloudFormation templates to use parameters stored in Parameter Store as input.

## **Use Cases**

- Storing database connection strings.
- Managing API keys and other sensitive information.
- Centralizing application configuration.
- Dynamically configuring applications during deployment.

## **Parameter Organization**

- **Hierarchical Structure:** Parameters can be organized in a path-like structure (e.g., `/my-department/my-app/dev/db-url`).
- **Simplified IAM Policies:** Enables granting granular access to parameters based on the hierarchy (e.g., access to all parameters under `/my-department/my-app/dev/`).

## **Accessing Secrets Manager Secrets**

- Parameter Store can reference secrets stored in AWS Secrets Manager using a specific syntax (not explicitly detailed in the transcription but mentioned as a "little trick").

## **Public Parameters**

- AWS provides public parameters that can be accessed (e.g., the latest AMI ID for a specific region and operating system).

## **Parameter Tiers**

- **Standard Tier (Free):**
    - Maximum parameter value size: 4KB.
    - No parameter policies.
- **Advanced Tier (Charged):**
    - Maximum parameter value size: 8KB.
    - Supports parameter policies ($0.05 per month per advanced parameter).

## **Parameter Policies (Advanced Tier Only)**

- **Time to Live (TTL):** Allows setting an expiration date for a parameter, forcing updates or deletion of sensitive data.
- **Expiration Policy:** Automatically deletes a parameter at a specified timestamp. Notifications are sent to EventBridge before expiration (e.g., 15 days prior).
- **No Change Notification:** Sends notifications to EventBridge if a parameter has not been updated within a specified duration (e.g., 20 days).

## **Example Application Access**

- **Dev Lambda Function:** IAM role grants access to specific parameters under `/my-app/dev/` (e.g., `DB-URL`, `DB-password`).
- **Prod Lambda Function:** Different IAM policy and potentially environment variables allow access to parameters under a different path (e.g., `/another-app/prod/`).

## **Summary**

AWS SSM Parameter Store provides a robust and secure solution for managing application configurations and secrets. Its features like encryption, hierarchical organization, IAM integration, and advanced policies offer flexibility and control. Understanding the different parameter tiers and their associated costs and capabilities is crucial for effective utilization.