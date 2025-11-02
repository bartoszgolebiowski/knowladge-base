# Amazon Inspector

## **Purpose and Goals**

- Automate security assessments of EC2 instances, container images in Amazon ECR, and Lambda functions.
- Identify potential security vulnerabilities and unintended network accessibility.
- Provide continuous scanning and reporting of security findings.
- Integrate with AWS Security Hub and Amazon EventBridge for centralized visibility and automated response.

## **Key Assessment Areas**

Amazon Inspector evaluates security for the following resources:

- **EC2 Instances:**
    - Leverages the AWS Systems Manager (SSM) Agent installed on the instances.
    - Analyzes for:
        - **Unintended Network Accessibility:** Identifies potential open ports and network configurations that could expose the instance to security risks.
        - **Operating System Vulnerabilities:** Scans the running operating system for known Common Vulnerabilities and Exposures (CVEs).
    - Assessment is performed continuously.
- **Container Images (pushed to Amazon ECR):**
    - Analyzes Docker images as they are pushed to Amazon Elastic Container Registry (ECR).
    - Scans for known software vulnerabilities (CVEs) within the container image layers and base operating system.
- **Lambda Functions:**
    - Analyzes Lambda functions when they are deployed.
    - Scans for software vulnerabilities (CVEs) in the function code and package dependencies.

## **Reporting and Integration**

- **AWS Security Hub:** Findings from Amazon Inspector are reported and aggregated within AWS Security Hub, providing a centralized view of security posture across your AWS environment.
- **Amazon EventBridge:** Inspector findings and events can be sent to Amazon EventBridge, enabling you to create automated workflows and responses to identified vulnerabilities.

## **Evaluation Scope**

Amazon Inspector focuses on:

- **Running EC2 Instances:** Assesses the security state of active EC2 instances.
- **Container Images in Amazon ECR:** Analyzes images stored in your private ECR repositories.
- **Deployed Lambda Functions:** Scans the code and dependencies of your deployed Lambda functions.

## **Continuous Scanning and Vulnerability Database**

- **Continuous Scanning (when needed):** Inspector performs ongoing assessments of your infrastructure.
- **CVE Database:** Inspector analyzes resources against a comprehensive database of known vulnerabilities (Common Vulnerabilities and Exposures).
- **Automatic Re-scanning on CVE Updates:** When the CVE database is updated, Amazon Inspector automatically re-runs assessments to ensure your infrastructure is checked against the latest known vulnerabilities.

## **Risk Scoring and Prioritization**

- Each identified vulnerability is assigned a **risk score** to help prioritize remediation efforts.
- This scoring system allows you to focus on the most critical security issues first.

**In summary, Amazon Inspector is a valuable service for automating security assessments of your EC2 instances, container images in ECR, and Lambda functions. Its continuous scanning, integration with Security Hub and EventBridge, and risk scoring capabilities help you proactively identify and address security vulnerabilities in your AWS environment.**