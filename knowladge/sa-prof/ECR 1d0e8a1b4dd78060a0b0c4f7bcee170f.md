# ECR

## **1. Purpose and Functionality**

- **Storage and Management:** Used to store and manage Docker images on AWS.
- **Repository Types:**
    - **Private:** For your own account.
    - **Public:** For sharing images publicly (accessible via `gallery.ecr.aws`).

## **2. Integration with ECS**

- **Image Pulling:** ECS clusters (specifically the EC2 instances within them, via their Instance Profile) are granted permissions (through IAM) to pull Docker images from ECR repositories.
- **Seamless Integration:** ECR is tightly integrated with ECS for easy deployment of containerized applications.
- **Access Control:** Access to ECR repositories is managed through AWS IAM policies. Permission errors indicate a policy issue.

## **3. Key Features**

- **Vulnerability Scanning:**
    - **Basic Scanning:** Identifies common vulnerabilities.
        - Triggered by pushing an image to ECR.
        - ECR performs the scan.
        - Vulnerability findings can trigger events in Amazon EventBridge (source: ECR).
    - **Enhanced Scanning:** Leverages Amazon Inspector for deeper analysis.
        - Looks for OS and programming language vulnerabilities in addition to common CVEs.
        - Triggered by pushing an image to ECR.
        - Amazon Inspector performs the scan.
        - Vulnerability findings are available in EventBridge (source: Inspector).
    - **Console Visibility:** Scan results for both basic and enhanced scanning can be viewed directly in the AWS console.
- **Versioning:** Supports versioning of Docker images.
- **Image Tags:** Allows tagging of Docker images for better organization and management.
- **Image Lifecycle:** Enables the definition of lifecycle policies to automate the cleanup of old or untagged images, helping to manage storage costs.
- **Cross-Region Replication:**
    - Supports replicating images across different AWS regions.
    - Supports cross-account replication (sharing images with other AWS accounts).
    - **Benefits:**
        - Avoids the need to rebuild images in multiple regions.
        - Enables faster deployment of applications in different regions, contributing to global application availability.

In summary, Amazon ECR provides a secure, scalable, and integrated solution for storing and managing Docker images within the AWS ecosystem, offering features like security scanning and cross-region replication to enhance container workflows.

As an AWS Solution Architect Professional, let's break down the key differences between EKS Managed Node Groups and Self-Managed Nodes:

**EKS Managed Node Groups:**

- **AWS Responsibility:** AWS takes on the responsibility for provisioning, scaling, upgrading, and patching the underlying EC2 instances (worker nodes) in the node group.
- **Lifecycle Management:** The lifecycle of the worker nodes is largely automated by the EKS service. This includes:
    - **Provisioning:** Creating new instances based on the specified configuration (instance type, desired capacity, etc.).
    - **Scaling:** Integrating with Auto Scaling Groups (ASGs) that are managed by EKS to automatically scale the number of nodes based on demand.
    - **Updates:** Handling Kubernetes version upgrades and operating system patching of the nodes in a controlled and orchestrated manner, often with options for rolling updates and draining of nodes.
    - **Termination:** Graceful handling of node terminations during scaling down or updates.
- **Ease of Use:** Generally simpler to set up and manage, reducing the operational overhead for managing the worker nodes.
- **Integration:** Tightly integrated with the EKS control plane.
- **Customization:** Offers a good level of customization for instance types, scaling configurations, and the use of either the Amazon EKS-optimized AMI or custom AMIs (via Launch Templates). However, the underlying node management is abstracted.
- **AMI Management:** When using the EKS-optimized AMI, AWS manages the base AMI updates. For custom AMIs, you manage the AMI but EKS handles the orchestration of updates.
- **Cost:** You pay for the underlying EC2 instances and any other AWS resources used by the node group. There is no additional charge for using Managed Node Groups.
- **Use Cases:** Ideal for general-purpose workloads, teams wanting EC2 flexibility with less operational overhead, and users new to EKS.

**Self-Managed Nodes:**

- **Customer Responsibility:** You have full control and responsibility for creating, configuring, managing, scaling, upgrading, and patching the EC2 instances that serve as your worker nodes.
- **Lifecycle Management:** You are responsible for implementing and managing all aspects of the worker node lifecycle, including:
    - **Provisioning:** Manually creating EC2 instances or using tools like CloudFormation or Terraform.
    - **Scaling:** Configuring and managing your own Auto Scaling Groups.
    - **Updates:** Planning and executing Kubernetes version upgrades and operating system patching on the nodes. This often involves manually cordoning and draining nodes.
    - **Joining the Cluster:** Manually configuring the `kubelet` and `aws-auth` ConfigMap to allow the nodes to join the EKS control plane.
- **Flexibility and Control:** Provides the highest degree of flexibility and control over the underlying infrastructure, including the choice of operating system, custom AMIs, kernel parameters, and installed software.
- **Customization:** Allows for deep customization of the worker nodes to meet specific workload requirements.
- **AMI Management:** You are entirely responsible for creating, maintaining, and updating the AMIs used for your worker nodes.
- **Cost:** You pay for the underlying EC2 instances and other AWS resources.
- **Complexity:** Higher operational overhead due to the manual management of the worker nodes. Requires more in-depth knowledge of EC2, Kubernetes, and operating system management.
- **Use Cases:** Suitable for complex workloads with very specific requirements, integration with existing or legacy infrastructure, scenarios requiring full control over the node configuration, and teams with strong DevOps expertise.

**Here's a table summarizing the key differences:**

| **Feature** | **EKS Managed Node Groups** | **Self-Managed Nodes** |
| --- | --- | --- |
| **Node Provisioning** | Automated by EKS | Manual or via your own tooling |
| **Scaling** | Integrated and managed by EKS (via ASG) | You configure and manage your own ASG |
| **Updates/Patching** | Automated and orchestrated by EKS | You are fully responsible |
| **Lifecycle Mgmt.** | Largely automated | Fully manual |
| **Ease of Use** | Simpler, lower operational overhead | More complex, higher operational overhead |
| **Control** | Good level of control over instance types | Full control over all aspects of the nodes |
| **AMI Management** | AWS manages EKS-optimized AMIs | You manage all aspects of the AMIs |
| **Integration** | Tightly integrated with EKS control plane | Requires manual configuration to join |
| **Complexity** | Lower | Higher |
| **Best For** | General workloads, easier management | Highly customized, specific requirements |

In most common scenarios, **EKS Managed Node Groups are the recommended approach** due to the reduced operational burden and simplified management. You should only consider Self-Managed Nodes when you have very specific customization needs that cannot be met by Managed Node Groups or Fargate.