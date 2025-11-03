# Service Quotas

# AWS Service Quotas - Solution Architect Professional Notes

## Core Purpose

- Helps you monitor and manage your AWS service limits (quotas).
- Enables proactive notifications when you are approaching service quota thresholds.
- Prevents unexpected throttling or service disruptions due to reaching limits.

## Functionality

- AWS services have default quotas to prevent abuse and ensure resource availability.
- Service Quotas allows you to view the default and applied quotas for various AWS services in a specific region.
- You can request quota increases for most services through the Service Quotas console or API.
- **Key Feature:** You can directly create CloudWatch alarms based on service quota usage metrics within the Service Quotas console.

## Example: Monitoring Lambda Concurrent Executions

1. **Identify Quota:** In the Service Quotas console, find the quota you want to monitor (e.g., "Concurrent executions" for AWS Lambda in a specific region).
2. **Create CloudWatch Alarm:** From the Service Quotas console, you can set up a CloudWatch alarm for this quota.
3. **Define Threshold:** Specify a threshold value (e.g., 9,000 concurrent executions) at which the alarm should trigger.
4. **Notification:** Configure the CloudWatch alarm to send notifications (e.g., via SNS) when the threshold is breached.

## Benefits

- **Proactive Monitoring:** Get alerted before hitting service limits and experiencing throttling.
- **Capacity Planning:** Helps in understanding your resource consumption and planning for future needs.
- **Quota Increase Management:** Provides insights into when a quota increase might be necessary.
- **Resource Optimization:** Enables you to identify potential over-provisioning and shut down resources before hitting limits.

## Key Takeaway for the Exam

- Service Quotas is the central service for viewing and managing AWS service limits.
- You can directly create CloudWatch alarms from the Service Quotas console to monitor quota usage.
- This allows for proactive alerting and management of potential service limit issues, preventing disruptions.
- Remember the use case of setting alarms on critical service quotas like Lambda concurrent executions.