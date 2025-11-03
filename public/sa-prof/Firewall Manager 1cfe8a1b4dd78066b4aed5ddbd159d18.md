# Firewall Manager

## **Purpose and Goals**

- Centrally manage firewall rules across multiple AWS accounts within an AWS Organization.
- Enforce consistent security policies across the entire organization.
- Automate the application of security rules to existing and newly created resources.

## **Key Concepts**

- **Security Policy:** A common set of security rules that can be applied across multiple accounts and resources.
- **AWS Organization:** A service to centrally manage and govern your AWS accounts.
- **Region Level Policies:** Firewall Manager policies are created within a specific AWS region and can then be applied to accounts in that region across the organization.
- **Automatic Resource Protection:** Firewall Manager can automatically apply defined security policies to new resources as they are created within the specified scope.

## **Supported Security Policies**

Firewall Manager can manage the following types of security rules:

- **AWS WAF Rules:** Manage Web ACLs and rules for Application Load Balancers (ALB), API Gateways, and CloudFront distributions.
- **AWS Shield Advanced Rules:** Configure and manage Shield Advanced protections for ALBs, Classic Load Balancers (CLB), Network Load Balancers (NLB), Elastic IPs, and CloudFront distributions.
- **Security Groups:** Standardize and enforce security group configurations for EC2 instances, Application Load Balancers, and Elastic Network Interfaces (ENIs) within VPCs.
- **AWS Network Firewall Rules:** Centrally manage rules for AWS Network Firewall deployed at the VPC level.
- **Amazon Route 53 Resolver DNS Firewall Rules:** Manage DNS Firewall rules to protect against DNS-based attacks.

## **Relationship with WAF and Shield**

- **AWS WAF:** Used to define individual Web ACL rules for protecting web applications at Layer 7. For one-off protection, WAF is the direct tool.
- **AWS Firewall Manager:** Extends the capabilities of WAF and Shield by allowing you to manage these protections across multiple accounts and automate their application to new resources. Firewall Manager acts as a central administration point for WAF and Shield policies within an organization.
- **AWS Shield Advanced:** Provides enhanced DDoS protection beyond the standard Shield offering, including dedicated support from the Shield Response Team (SRT), advanced reporting, and automatic WAF rule creation in response to DDoS events. Firewall Manager can be used to deploy Shield Advanced protections across all accounts in an organization.

## **Use Cases for Firewall Manager**

- **Centralized Security Administration:** Security teams can define and enforce consistent security policies across all organizational units (OUs) and accounts from a single management console.
- **Simplified Rule Deployment:** Avoids the need to manually configure firewall rules in each individual account.
- **Automated Protection:** Ensures that new resources automatically inherit the defined security policies, reducing the risk of unprotected deployments.
- **Compliance and Governance:** Helps organizations meet compliance requirements by enforcing consistent security controls across their AWS environment.
- **Incident Response:** Provides a central view of firewall configurations and allows for rapid updates or changes in response to security incidents.

## **Key Benefits**

- **Consistency:** Enforce uniform security standards across the entire AWS Organization.
- **Efficiency:** Streamline the management of firewall rules, saving time and effort.
- **Scalability:** Easily manage security policies as your AWS environment grows.
- **Automation:** Reduce manual configuration and ensure consistent protection for new resources.
- **Visibility:** Provides a centralized view of firewall policies and their application status across accounts.

**In summary, AWS Firewall Manager is a powerful service for organizations that need to manage firewall rules across multiple AWS accounts. It simplifies the administration of WAF, Shield Advanced, Security Groups, Network Firewall, and Route 53 Resolver DNS Firewall, ensuring consistent security and automating protection for new resources.**