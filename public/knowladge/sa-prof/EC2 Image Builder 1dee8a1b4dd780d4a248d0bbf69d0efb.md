# EC2 Image Builder

## **EC2 Image Builder**

- Service to create and automate the creation of virtual machine or container images.
- Automates the creation, maintenance, validation, and testing of EC2 AMIs.
- Can be run on a schedule (e.g., weekly, upon package updates).
- Can be triggered through automation.
- **Cost:** Free service; pay only for underlying resources (EC2 instances).
- **Distribution:** AMIs created can be published to multiple regions and accounts.

### **Workflow**

1. **Setup:** Define build instructions for the Image Builder service.
2. **Builder Instance:** The service launches a builder EC2 instance (minimal configuration).
3. **Build Components:** The Image Builder runs build components to customize the software on the builder instance based on the provided instructions.
4. **AMI Creation:** Once build instructions are complete, an AMI is created.
5. **Testing:** A new EC2 instance is launched from the created AMI. Tests are run to verify functionality and security.
6. **Distribution:** The AMI is distributed to the region it was created in and optionally to other specified regions and accounts.

### **CI/CD Architecture with EC2 Image Builder**

1. **Orchestration:** AWS CodePipeline orchestrates the entire process.
2. **Code Source:** CodeCommit stores the application code.
3. **Build:** CodeBuild compiles the application code and creates an executable.
4. **AMI Building:**
    - CloudFormation automates and launches the EC2 Image Builder service.
    - Image Builder takes the built code from CodeBuild.
    - Image Builder creates an AMI.
5. **AMI Rollout:**
    - CloudFormation performs a rolling update on an Auto Scaling Group.
    - EC2 instances in the Auto Scaling Group are gradually updated from the previous AMI to the new AMI.

This architecture provides a fully automated way to:

- Push code to CodeCommit.
- Build an AMI from the code.
- Roll out the new AMI to production instances.