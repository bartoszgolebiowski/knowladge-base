# CloudWatch

Okay, that's a good overview of CloudWatch Metrics, Alarms, and Synthetics Canaries. Here's a breakdown of the key points and some additional context that might be helpful:

**CloudWatch Metrics**

- **EC2 Metrics:**
    - Standard monitoring provides metrics every 5 minutes.
    - Detailed monitoring provides metrics every 1 minute.
    - Default metrics include CPU, network, and disk (for instance store).
    - RAM usage requires custom metrics using the CloudWatch agent.
- **Custom Metrics:**
    - Standard resolution is 1 minute.
    - High-resolution metrics can go down to 1 second.
    - This is useful for very time-sensitive applications.

**CloudWatch Alarms**

- **Actions:**
    - EC2 actions: reboot, stop, terminate, recover.
    - Auto Scaling actions: scale instances in or out.
    - SNS notifications: send alerts via email, SMS, etc.
- **EventBridge Integration:**
    - Alarms can trigger events on EventBridge, enabling integration with other AWS services.
    - This is very powerful for building complex automated workflows.
    - Examples include triggering Lambda functions, Step Functions, or sending data to Kinesis.
- **Recover Action:**
    - The "recover" action is important. It attempts to migrate the EC2 instance to a new host if there's an underlying hardware issue. This preserves the instance's private IP address.

**CloudWatch Synthetics Canaries**

- **Purpose:**
    - Proactively monitor APIs, URLs, and websites.
    - Simulate user behavior to detect issues before they impact customers.
- **Functionality:**
    - Scripts run on a schedule to perform health checks.
    - Can monitor availability, latency, and functionality.
    - Can store load time data and screenshots.
- **Use Cases:**
    - API monitoring: test API endpoints for correctness and performance.
    - Website monitoring: check for broken links, page load errors, etc.
    - Workflow testing: simulate user logins, form submissions, etc.
- **Technology:**
    - Scripts are written in Node.js or Python.
    - Uses headless Chrome to interact with web pages and APIs.
- **Canary Blueprints:**
    - Provide pre-built scripts for common monitoring tasks.
    - Examples: heartbeat monitoring, API testing, broken link checking, visual monitoring.
    - Canary Recorder and GUI Workflow Builder simplify the creation of complex test scripts.
- **Integration with Alarms:**
    - Canaries can trigger CloudWatch alarms if issues are detected.
    - This allows for automated responses, such as scaling, notifications, or remediation actions.

**Key Takeaways**

- CloudWatch is a comprehensive monitoring and observability service.
- Metrics provide data about the performance and health of your AWS resources.
- Alarms allow you to react automatically to metric changes.
- Synthetics Canaries enable proactive monitoring of applications and APIs.
- EventBridge integration greatly expands the capabilities of CloudWatch alarms.

This information should give you a solid understanding of CloudWatch's core components. Let me know if you have any other questions.