# Organizations

# AWS Organizations

## Overview

- AWS Organizations allows you to manage multiple AWS accounts centrally.
- It provides features for consolidated billing, access control, and policy management across accounts.

## Key Components

- **Root:**
    - The top-level container for all OUs and accounts.
    - Contains the management account.
- **Management Account:**
    - The account used for administrative purposes.
    - Manages all other accounts within the organization.
- **Organizational Units (OUs):**
    - Containers for grouping accounts.
    - OUs can be nested to create a hierarchical structure.
    - Examples: Dev, Prod, HR, Finance.
- **Member Accounts:**
    - Individual AWS accounts that belong to the organization.
    - Managed by the management account.
- **Organization Account Access Role:**
    - An IAM role automatically created in member accounts when created via the Organizations API.
    - Grants full administrative permissions to the management account.
    - Must be manually created for existing accounts invited into the organization.
    - Allows the management account to perform administrative tasks in member accounts.

![image.png](image%202.png)

## Multi-Account Strategies

- Accounts can be created based on:
    - Departments.
    - Cost centers.
    - Development, test, and production environments.
    - Regulatory restrictions.
    - Resource isolation.
    - Service limits.
    - Logging and security.
- Tagging standards are essential for billing and resource management.
- Centralized logging and security accounts are common patterns.
- OU structures can be based on:
    - Business units.
    - Environment types (Dev, Test, Prod).
    - Projects.

## Feature Modes

- **Consolidated Billing:**
    - Aggregates billing across all accounts.
    - Provides a single payment method.
    - Offers volume discounts and pricing benefits.
- **All Features:**
    - Includes consolidated billing.
    - Adds Service Control Policies (SCPs) for access control.
    - Requires account approval for invited accounts.
    - Once enabled, cannot revert back to Consolidated Billing only.
    - Allows SCPs to prevent member accounts from leaving the organization.

## Shared Resources and Savings

- **Reserved Instances (RIs) and Savings Plans:**
    - Consolidated billing treats all accounts as one for RI and savings plan benefits.
    - Maximum savings are achieved through aggregated usage.
    - The management account can disable RI/savings plan sharing for specific accounts.
    - Both accounts must have sharing enabled for RI/savings plan sharing to occur.

## Moving Accounts Between Organizations

- Process:
    1. Remove the member account from the current organization.
    2. Send an invitation to the member account from the new organization.
    3. Accept the invitation from the member account.
    
    ![image.png](image%203.png)