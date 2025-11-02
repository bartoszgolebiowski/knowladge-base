# IAM Advanced Conditions

IAM conditions allow you to control when a policy statement is in effect. They add granular control over permissions based on various factors. Conditions can be applied to:

- IAM user policies
- Resource-based policies (e.g., S3 bucket policies)
- Endpoint policies
- And more.

Here are some key IAM conditions:

## **`aws:SourceIP`**

- **Purpose:** Restricts access based on the originating IP address of the API call.
- **Example:**
This policy denies all actions unless the API call originates from one of the specified IP address ranges.
    
    **JSON**
    
    `{
        "Effect": "Deny",
        "NotPrincipal": "*",
        "Action": "*",
        "Condition": {
            "NotIpAddress": {
                "aws:SourceIP": [
                    "203.0.113.0/24",
                    "192.0.2.0/28"
                ]
            }
        }
    }`
    
- **Use Case:** Restricting AWS access to your company's network.

## **`aws:RequestedRegion`**

- **Purpose:** Restricts the AWS region to which the API calls are being made.
- **Example:**
This policy denies all EC2, RDS, and DynamoDB actions if the request is made to the `eu-central-1` or `eu-west-1` regions.
    
    **JSON**
    
    `{
        "Effect": "Deny",
        "Action": [
            "ec2:*",
            "rds:*",
            "dynamodb:*"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "aws:RequestedRegion": [
                    "eu-central-1",
                    "eu-west-1"
                ]
            }
        }
    }`
    
- **Use Case:** Enforcing regional compliance or restricting resource deployment to specific geographic locations (can be applied at the SCP level).

## **`ec2:ResourceTag/TagKey`**

- **Purpose:** Restricts access based on tags applied to EC2 resources. The prefix `ec2:` indicates it applies to EC2 resource tags.
- **Example:**
This policy allows starting and stopping any EC2 instance that has a tag with the key `Project` and the value `DataAnalytics`.
    
    **JSON**
    
    `{
        "Effect": "Allow",
        "Action": [
            "ec2:StartInstances",
            "ec2:StopInstances"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "ec2:ResourceTag/Project": "DataAnalytics"
            }
        }
    }`
    

## **`aws:PrincipalTag/TagKey`**

- **Purpose:** Restricts access based on tags applied to the IAM principal (user or role) making the request. The prefix `aws:` indicates it's a general AWS condition, and `PrincipalTag` specifies it's about the principal's tags.
- **Example (in conjunction with the previous one):**
This policy allows starting and stopping EC2 instances tagged with `Project:DataAnalytics` only if the IAM user or role making the request is tagged with `Department:Data`.
    
    **JSON**
    
    `{
        "Effect": "Allow",
        "Action": [
            "ec2:StartInstances",
            "ec2:StopInstances"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "ec2:ResourceTag/Project": "DataAnalytics",
                "aws:PrincipalTag/Department": "Data"
            }
        }
    }`
    

## **`aws:MultiFactorAuthPresent`**

- **Purpose:** Enforces the use of multi-factor authentication (MFA) for specific actions.
- **Example:**
This set of statements allows all EC2 actions but explicitly denies stopping or terminating instances if MFA is not present during the request.
    
    **JSON**
    
    `{
        "Effect": "Allow",
        "Action": "ec2:*",
        "Resource": "*"
    },
    {
        "Effect": "Deny",
        "Action": [
            "ec2:StopInstances",
            "ec2:TerminateInstances"
        ],
        "Resource": "*",
        "Condition": {
            "Bool": {
                "aws:MultiFactorAuthPresent": "false"
            }
        }
    }`
    

## **Resource Policies and `aws:PrincipalOrgID`**

- **Purpose:** Restricts access to resources (like S3 buckets) to principals belonging to a specific AWS Organization. This condition is used in resource-based policies.
- **Example (S3 Bucket Policy):**
This bucket policy allows `GetObject` and `PutObject` actions on all objects within `your-bucket-name` only if the requesting principal belongs to the AWS Organization with the ID `o-xxxxxxxxxxxxx`. Access from accounts outside this organization will be denied.
    
    **JSON**
    
    `{
        "Sid": "AllowOrganizationAccess",
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
            "s3:GetObject",
            "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::your-bucket-name/*",
        "Condition": {
            "StringEquals": {
                "aws:PrincipalOrgID": "o-xxxxxxxxxxxxx"
            }
        }
    }`
    

**Key Takeaways:**

- IAM conditions provide fine-grained control over permissions.
- The prefix of the condition key (e.g., `aws:`, `ec2:`) indicates the context of the condition.
- Resource-based policies (like S3 bucket policies) use different ARNs for bucket-level and object-level permissions.
- `aws:PrincipalOrgID` is crucial for restricting resource access within an AWS Organization.
- Understanding and utilizing IAM conditions is essential for implementing secure and advanced AWS solutions.