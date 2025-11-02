# Managed Logs

![image.png](image%2012.png)

## **Load Balancer Access Logs**

- **Description:** Detailed information about requests made to your load balancers.
- **Supported Load Balancers:** Application Load Balancer (ALB), Network Load Balancer (NLB), and Classic Load Balancer (CLB).
- **Export Destination:** Amazon S3.

## **CloudTrail Logs**

- **Description:** Records of all API calls made within your AWS account.
- **Export Destinations:** Amazon S3 and Amazon CloudWatch Logs.

## **VPC Flow Logs**

- **Description:** Information about IP traffic going to and from network interfaces within your Virtual Private Cloud (VPC).
- **Export Destinations:** Amazon S3, Amazon CloudWatch Logs, and Amazon Kinesis Data Firehose.

## **Route 53 Access Logs**

- **Description:** Logs of all DNS queries received by Amazon Route 53.
- **Export Destination:** Amazon CloudWatch Logs (streamed directly).

## **S3 Access Logs**

- **Description:** Details about access requests made to your Amazon S3 buckets.
- **Export Destination:** Another S3 bucket (specified by you).

## **CloudFront Access Logs**

- **Description:** Detailed information about every user request received by Amazon CloudFront.
- **Export Destination:** Amazon S3.

## **AWS Config Information**

- **Description:** Configuration details of your AWS resources.
- **Export Destination:** Amazon S3 (for backup and analysis).