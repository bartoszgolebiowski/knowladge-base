# EC2 instance connect

![image.png](image%2015.png)

EC2 Instance Connect enables secure SSH or SSH-like connections to your EC2 instances directly from the AWS Management Console or AWS CLI, without needing to manage SSH keys on the instances themselves. It leverages the `SendSSHPublicKey` API.

## **Workflow:**

1. **Security Group Configuration:**
    - The EC2 instance's security group needs an inbound rule allowing SSH traffic on port 22.
    - The **Source** of this rule should be restricted to the IP address ranges used by the EC2 Instance Connect service for the specific AWS region. These prefixes can be found at a designated AWS URL.
2. **User Initiates Connection:**
    - A user accesses the EC2 Instance Connect API (via the AWS Console or CLI).
3. **`SendSSHPublicKey` API Invocation (Behind the Scenes):**
    - Upon initiating a connection, the EC2 Instance Connect service (or a user directly using the API) calls the `SendSSHPublicKey` API.
    - This API pushes a **temporary, one-time-use SSH public key** onto the target EC2 instance.
4. **Key Validity:**
    - The uploaded SSH public key is only valid for **60 seconds**.
5. **SSH Connection:**
    - During this 60-second window, the user can connect to the EC2 instance using the corresponding **private SSH key**. The connection goes through the established SSH port 22 allowed by the security group rule.
6. **Connection Establishment:**
    - The EC2 instance authenticates the incoming SSH connection using the temporarily stored public key.

## **Key Points:**

- **Temporary Key:** EC2 Instance Connect does not require persistent SSH keys to be stored on the instance.
- **`SendSSHPublicKey` API:** This API is the core mechanism for securely injecting the temporary public key. You can use this API directly as well.
- **Security:** By using short-lived keys, the risk of compromised long-term keys is mitigated.
- **Auditability:** All connection attempts using the `SendSSHPublicKey` API and the EC2 Instance Connect API are logged in AWS CloudTrail, providing full audit and visibility.

You **do** need to open port 22 in the security group of your EC2 instance to allow SSH connections via the EC2 Instance Connect API.

Here's why:

In summary, EC2 Instance Connect simplifies secure remote access to EC2 instances by dynamically pushing a short-lived SSH public key using the `SendSSHPublicKey` API, allowing a brief window for SSH connection using the corresponding private key. The security group must be configured to allow SSH traffic from the EC2 Instance Connect service's IP ranges.

- **SSH Protocol:** EC2 Instance Connect, despite its convenience of not needing traditional key management, still relies on the SSH protocol for establishing the connection to your instance. The temporary public key pushed by the `SendSSHPublicKey` API is used for SSH authentication.
- **Security Group Rules:** Security groups act as virtual firewalls controlling inbound and outbound traffic at the instance level. To allow any SSH connection to your instance, regardless of the authentication method (key pair or EC2 Instance Connect), you must have an inbound rule allowing traffic on TCP port 22.
- **Source Restriction (Recommended):** While you need to open port 22, it's a security best practice to restrict the **Source** of this inbound rule. Instead of allowing from `0.0.0.0/0` (anywhere), you should ideally limit it to the IP address ranges used by the EC2 Instance Connect service for your specific AWS region. You can find these IP ranges in the AWS documentation or by querying AWS services.

**In summary, opening port 22 in your instance's security group, with the source ideally restricted to the EC2 Instance Connect service's IP ranges for your region, is a prerequisite for using the EC2 Instance Connect API to SSH into your EC2 instance.**