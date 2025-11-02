# DDoS Protection

## **Understanding DDoS Attacks**

- **Definition:** Distributed Denial of Service. Aims to make an instance unavailable by overwhelming it with malicious traffic, preventing legitimate users from accessing the application.
- **Mechanism:**
    - Attacker controls master computers.
    - Masters create a large number of bots.
    - Bots send numerous, often non-conventional, requests to the application server.
    - The server becomes overwhelmed and unable to respond to legitimate requests, leading to a denial of service.
- **Common and Dangerous:** A prevalent threat on the internet.

## **Types of DDoS Attacks**

### **Infrastructure Level (Network Based)**

- **SYN Flood (Layer 4):** Overwhelming the server with TCP connection requests.
- **UDP Reflection:** Exploiting other servers to send large UDP requests to the target server.
- **DNS Flood Attack:** Overwhelming the DNS server, preventing users from resolving the website's address.
- **Slow Loris (Layer 7):** Opening and maintaining many HTTP connections, exhausting server resources (threads).

### **Application Level Attacks**

- **More Complex and Specific:** Requires understanding the target application's functionality.
- **Examples:**
    - **Cache Bursting Strategy:** Overloading the backend database by invalidating the cache with numerous requests.
    - Requesting too many resources or sending excessively large packets.
- **Vulnerability Dependent:** Exploits security weaknesses in the application code.

## **DDoS Protection on AWS**

AWS offers various services and features to mitigate DDoS and application-level attacks:

- **AWS Shield Standard:**
    - Free service enabled by default for all AWS customers.
    - Protects against common, frequently occurring network and transport layer DDoS attacks (Layer 3 and 4).
    - Provides always-on monitoring and automatic inline mitigations.
- **AWS Shield Advanced:**
    - Paid service offering enhanced DDoS protection.
    - Provides 24/7 premium DDoS protection for EC2, ELB, CloudFront, AWS Global Accelerator, and Route 53.
    - Offers access to the AWS DDoS Response Team (DRT) for expert assistance during attacks.
    - Includes DDoS cost protection, shielding you from increased AWS usage charges due to scaling during an attack.
    - Protects against more sophisticated and larger attacks.
- **AWS WAF (Web Application Firewall):**
    - Not specifically for DDoS but helps filter malicious requests based on customizable rules (e.g., blocking requests exceeding a certain size).
    - Primarily focused on application-level (Layer 7) protection against attacks like SQL injection and cross-site scripting.
    - Can contribute to DDoS mitigation by blocking known bad actors or suspicious patterns.
- **Amazon CloudFront and AWS Route 53:**
    - Benefit from built-in AWS Shield Standard protection.
    - Provide availability protection through their globally distributed edge networks.
    - Absorb and mitigate a significant portion of DDoS traffic at the edge, preventing it from reaching the core application.
- **AWS Auto Scaling:**
    - Automatically scales the number of instances based on metrics like CPU utilization.
    - Increases the cost for attackers to overwhelm the infrastructure by requiring them to target more instances.
    - Provides resilience by distributing the attack across a larger pool of resources.
- **Separation of Static and Dynamic Resources:**
    - Host static content (e.g., images, CSS, JavaScript) on Amazon S3 and distribute it via CloudFront. This infrastructure is highly resilient to DDoS attacks.
    - Handle dynamic requests through smaller, scalable components like REST APIs on EC2 behind an Application Load Balancer (ALB).

## **Sample DDoS Protection Architecture on AWS**

1. **DNS (Route 53):** Protected by AWS Shield Standard by default.
2. **Content Delivery Network (CloudFront):**
    - Protected by AWS Shield Standard by default.
    - Can be integrated with AWS WAF for application-level filtering.
3. **Load Balancer (ALB/NLB):** Benefits from AWS Shield protection (Standard or Advanced).
4. **Compute (Auto Scaling Group of EC2 Instances):** Auto Scaling helps handle increased traffic by adding more instances.

## **Key Takeaways for the Exam**

- Understand the different types of DDoS attacks (network vs. application layer).
- Know the purpose and capabilities of AWS Shield Standard (free, basic Layer 3/4 protection) and Shield Advanced (paid, enhanced protection for various resources, DRT access, cost protection).
- Recognize how AWS WAF, CloudFront, Route 53, and Auto Scaling contribute to a comprehensive DDoS mitigation strategy.
- Be aware of the recommended architecture for separating static and dynamic content for improved resilience.
- Understand the cost implications and benefits of Shield Advanced for enterprise customers facing sophisticated attacks.