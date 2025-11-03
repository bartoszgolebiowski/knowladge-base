# Secret Manager

## **Purpose of AWS Secrets Manager**

- Designed for storing secrets such as passwords and API keys.
- Key feature: Automated rotation of secrets.

## **Key Features and Concepts**

- **Automated Secret Rotation:**
    - Secrets can be rotated automatically at defined intervals (e.g., every X days).
    - Rotation can be on-demand or automatic.
    - New secrets can be generated automatically, often using Lambda functions.
- **Native Integrations:**
    - Strong native integration with RDS (all DB engines), Redshift, and DocumentDB for automatic password rotation.
    - For other services, custom Lambda functions are required to generate and rotate secrets.
- **Access Control:**
    - Resource-based policies can be used to control access to secrets.
- **Integration with AWS Services:**
    - Deep integration with various AWS services for seamless secret retrieval:
        - CloudFormation (reference secrets in templates)
        - CodeBuild
        - ECS (inject as environment variables at boot time)
        - EMR
        - Fargate
        - EKS
        - Parameter Store (can pull Secrets Manager secrets)
        - And more.

## **Example: ECS Integration**

- ECS tasks can automatically pull secrets from Secrets Manager at boot time.
- Secrets are injected as environment variables within the ECS task.
- This allows applications running in ECS to securely access resources like RDS databases.

## **CloudFormation Integration Example**

- Secrets can be created and managed within CloudFormation templates.
- The process involves:
    1. Generating the secret.
    2. Referencing the secret in the resource that needs it (e.g., RDS DB instance).
    3. Creating a "secret attachment" to link the secret to the resource, enabling Secrets Manager to update the resource during rotation.

## **Sharing Secrets Across AWS Accounts**

- Scenario: Sharing a secret from a security account to a developer account.
- **Limitations:** AWS Resource Access Manager (RAM) cannot be used to share Secrets Manager secrets.
- **Solution:** Using a combination of KMS key policy and Secrets Manager resource-based policy.
    1. **KMS Key Policy:** Allow the user/role in the developer account to perform `kms:Decrypt` on the KMS key protecting the secret.
        - Include a condition `kms:ViaService` to restrict decryption only when invoked through the Secrets Manager service.
    2. **Secrets Manager Resource-Based Policy:** Attach a policy to the secret in the security account granting the user/role in the developer account permission to perform `secretsmanager:GetSecretValue`.
- With both permissions in place, authorized entities in the developer account can access and decrypt the shared secret.

## **Secrets Manager vs. SSM Parameter Store**

| **Feature** | **AWS Secrets Manager** | **SSM Parameter Store** |
| --- | --- | --- |
| **Cost** | More expensive | Less expensive |
| **Secret Rotation** | Automated via Lambda (built-in for some services) | Requires manual setup with EventBridge and Lambda |
| **Encryption** | Mandatory KMS encryption | KMS encryption is optional |
| **Integration** | Deep integration with CloudFormation | Deep integration with CloudFormation |
| **API** | More specialized API for secrets | Simpler API, can store various types of parameters |
| **Secret Storage** | Specifically designed for secrets | Can store secrets and non-secret configuration values |
| **Pulling Secrets via Parameter Store** | N/A | Can pull Secrets Manager secrets using Parameter Store API |

## **Secret Rotation Mechanisms**

- **Secrets Manager:**
    - For integrated services (RDS, Redshift, DocumentDB), a backend Lambda function is automatically invoked (e.g., every 30 days).
    - This Lambda function updates the password in both the target service and Secrets Manager.
- **SSM Parameter Store (for secrets):**
    - Requires manual creation of an Amazon EventBridge rule to trigger a Lambda function at a defined interval.
    - The Lambda function is responsible for changing the password in the target service and updating the value in Parameter Store.
    - Maintaining this integration is the user's responsibility.