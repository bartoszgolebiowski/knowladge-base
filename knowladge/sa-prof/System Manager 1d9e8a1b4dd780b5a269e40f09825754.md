# System Manager

# AWS Systems Manager - Solution Architect Professional Notes

## Core Purpose

- Manage EC2 instances and on-premises servers at scale.
- Provide operational insights into infrastructure state.
- Facilitate easy problem detection and remediation.
- Enable patch automation for enhanced compliance.
- Works with both Linux and Windows.
- Integrates with AWS services like CloudWatch and Config.
- Free service (you pay for underlying resource usage).

## How it Works

- **SSM Agent:** Must be installed on managed instances (pre-installed on Amazon Linux and some Ubuntu AMIs).
- **Agent Communication:** Agents communicate with the SSM service.
- **Troubleshooting Registration:** If instances don't appear in SSM:
    - Agent might be misconfigured.
    - Agent might lack necessary IAM permissions (instance profile for EC2, access keys for on-premises).

## Key Features

1. **Run Command:**
    - Remotely execute scripts, documents, or commands across multiple instances without SSH.
    - **Resource Groups:** Define groups of target instances.
    - **Rate Control:** Manage the concurrency of command execution.
    - **Error Control:** Define behavior on command failure (stop all or continue).
    - **Integration:** Fully integrated with IAM and CloudTrail for security and auditability.
    - **Architecture Example (EC2):** SSM Agent on the EC2 instance polls the SSM service for commands and executes them locally.
    - **Architecture Example (ASG Lifecycle Hook):**
        1. ASG initiates instance termination.
        2. Lifecycle hook puts the instance in a "terminating:wait" state.
        3. EventBridge rule triggers on the "terminating:wait" event for the ASG.
        4. SSM Automation document is executed.
        5. SSM Automation uses "send command" to run scripts on the terminating instance (e.g., log collection).
        6. Lifecycle hook is completed, allowing instance termination.
2. **Patch Manager:**
    - Automate patching of instances at scale for OS and applications.
    - **Patch Baselines:** Define approved patches and patching rules.
    - **Patch Groups:** Organize instances by environment (Dev, Test, Prod).
    - **Maintenance Windows:** Schedule patching activities.
    - **RunPatchBaseline Command:** Initiate patching during maintenance windows.
    - **Cross-Platform:** Works on Windows and Linux.
    - **Rate Control and Error Thresholds:** Similar to Run Command.
    - **Patch Compliance:** Monitor patch status using SSM Inventory.
    - **Architecture:** RunPatchBaseline task targets patch groups within defined maintenance windows, applying patches according to the baseline.
3. **Session Manager:**
    - Provides secure shell access to EC2 and on-premises servers via the AWS console, CLI, or SDK **without needing SSH, port 22, Bastion Hosts, or SSH keys.**
    - **Agent Dependency:** Requires the SSM Agent and proper IAM permissions.
    - **Supported OS:** Linux, macOS, Windows.
    - **Benefits over SSH:**
        - **Centralized Logging:** All session commands can be logged to CloudWatch Logs or S3 for full traceability.
        - **Enhanced Security:** Eliminates the need to open SSH ports.
        - **Auditing:** CloudTrail can track Session Manager start events.
    - **Architecture:** Console/CLI/SDK connects to the Session Manager service, which establishes a connection with the SSM Agent on the target instance.
4. **OpsCenter:**
    - Centralized view for managing operational issues (OpsItems) related to AWS resources.
    - **OpsItems:** Represent issues, events, and alerts.
    - **Aggregation of Information:** Provides a consolidated view of relevant data from various AWS services (Config changes, CloudTrail logs, CloudWatch alarms, CloudFormation info, metrics, etc.).
    - **Automation Runbooks:** Integrate with SSM Automation to provide pre-defined steps for resolving issues.
    - **OpsItem Creation:** Can be triggered by:
        - SSM Automation workflows.
        - CloudWatch alarms.
        - EventBridge rules.
    - **Architecture:** OpsCenter aggregates information related to OpsItems from various AWS services, enabling centralized troubleshooting and remediation via Automation Runbooks.

## Key Takeaways for the Exam

- Systems Manager is a powerful tool for managing hybrid AWS environments at scale.
- Understand the function and benefits of Run Command, Patch Manager, Session Manager, and OpsCenter.
- Recognize the importance of the SSM Agent and proper IAM permissions.
- Know that Session Manager provides secure shell access without traditional SSH requirements and offers enhanced logging and auditing.
- Understand how OpsCenter centralizes operational issue management and integrates with Automation.
- Be aware of how Systems Manager can be integrated with other AWS services like EventBridge and CloudWatch for automated responses.