# Control Tower

## Purpose and Goals

- Simplifies the setup and governance of secure, compliant multi-account AWS environments based on best practices.
- Automates environment provisioning, policy management, and compliance monitoring.

## Key Features

- **Automated Environment Setup:**
    - Rapid deployment of multi-account environments with a few clicks.
- **Ongoing Policy Management:**
    - Implementation of guardrails for continuous governance.
    - Automated detection and remediation of policy violations.
- **Compliance Monitoring:**
    - Interactive dashboard for real-time compliance visibility.
- **Integration with AWS Organizations:**
    - Builds upon AWS Organizations to manage and organize accounts.
    - Automates the implementation of Service Control Policies (SCPs).
- **Account Factory:**
    - Automates account provisioning and deployment.
    - Creates pre-approved baseline configurations for accounts.
    - Uses AWS Service Catalog for account provisioning.
    - Helps with hybrid cloud setups, by integrating with on premise active directory via AWS Managed Microsoft AD, and IAM Identity Center.
- **Guardrails:**
    - Detects and remediates policy violations for ongoing governance.
    - Types of Guardrails:
        - **Preventive (SCPs):**
            - Disallows actions (e.g., disabling root user access key creation).
        - **Detective (AWS Config):**
            - Monitors compliance (e.g., MFA status for root users).
            - Leverages AWS Config to assess resource compliance.
            - Can trigger automated remediation using services like Lambda.
- **Guardrail Levels:**
    - **Mandatory:**
        - Automatically enabled and enforced (e.g., disallowing public read access to log archive accounts).
    - **Strongly Recommended:**
        - Based on AWS best practices (e.g., enabling encryption for EBS volumes).
    - **Elective:**
        - Optional guardrails for enterprise-specific needs (e.g., disallowing delete actions without MFA in S3 buckets).

## Account Factory and Active Directory Integration

- Control Tower facilitates integration with on-premises Active Directory.
- Uses AWS Managed Microsoft AD as the authentication source for IAM Identity Center.
- Establishes a two-way trust between on-premises and AWS Active Directory.
- Ensures accounts created through the landing zone and Account Factory are properly configured for authentication.

## Detective Guardrails and Remediation

- Uses AWS Config for detective guardrails.
- Monitors resources for compliance (e.g., untagged resources).
- Triggers notifications (SNS) and automated remediation (Lambda) for non-compliant resources.