# Service Catalog

# AWS Service Catalog - Solution Architect Professional Notes

## Purpose

- Provides a self-service portal for users to launch approved and compliant AWS resources.
- Limits user options to predefined products, ensuring adherence to organizational standards and governance.
- Abstracts the complexity of AWS for users with less experience.

## How it Works

- **Relies on CloudFormation:** The backbone of Service Catalog is CloudFormation templates.
- **Two Key Roles:**
    - **Administrators:** Define and manage products and portfolios.
    - **Users:** Discover and launch approved products.

## Components

1. **Products:**
    - Are CloudFormation templates created by administrators.
    - Define the AWS resources to be provisioned (e.g., EC2 instances, RDS databases, EFS volumes).
    - Administrators ensure these templates are well-architected, secure, and compliant.
2. **Portfolios:**
    - Collections of related products.
    - Access to portfolios is controlled through IAM roles, determining which users can see and launch the products within them.
3. **Users:**
    - Access the Service Catalog portal.
    - See a list of products they are authorized to use based on their IAM permissions.
    - Launch products they need (e.g., an EC2 instance stack).
4. **Provisioned Products:**
    - The actual AWS resources that are created when a user launches a product.
    - These resources are provisioned according to the underlying CloudFormation template.
    - They are properly configured and tagged as defined in the template.

## Benefits

- **Controlled Environment:** Users can only deploy resources approved by administrators.
- **Governance and Compliance:** Ensures resources are provisioned according to organizational policies and standards.
- **Consistency and Standardization:** Enforces consistent configurations, tagging, and other resource properties.
- **Self-Service:** Empowers users to provision resources independently within the defined boundaries.
- **Simplified User Experience:** Abstracts the complexity of AWS for users who don't need granular control.

## Use Case for the Exam

- When the scenario involves users with limited AWS knowledge who need to provision resources.
- When consistency, standardization, and governance are key requirements.
- When administrators need to maintain control over what resources users can deploy.

## Integration

- **Self-Service Portals:** Integrates with existing IT service management (ITSM) portals like ServiceNow, allowing users to request AWS resources through familiar interfaces.

## Key Takeaway

Service Catalog acts as a curated catalog of CloudFormation templates, empowering users to self-provision approved AWS resources while maintaining control and compliance through administrator-defined products and IAM permissions. It's about giving *less* direct control to users and more control to administrators for consistency and governance.