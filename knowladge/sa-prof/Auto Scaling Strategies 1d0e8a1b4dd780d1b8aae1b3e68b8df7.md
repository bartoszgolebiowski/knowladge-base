# Auto Scaling Strategies

This lecture highlights the various strategies for updating applications running within an Auto Scaling Group (ASG) and the architectural implications of each approach. There isn't a single "best" way; the choice depends on factors like risk tolerance, complexity preference, and application requirements.

Here are the discussed strategies:

## **1. In-Place Update with Single ASG and Single Target Group**

![image.png](image%2017.png)

- **Process:**
    1. Keep the existing ASG.
    2. Create a **new Launch Template** (or Launch Configuration) with the updated application version.
    3. Gradually, the ASG will launch new instances based on the new template alongside the existing instances using the old template. This might require temporarily increasing the desired capacity.
    4. Both sets of instances belong to the **same Target Group**, so the Application Load Balancer (ALB) distributes traffic across all instances, running both versions of the application simultaneously.
    5. Once confident in the new version, terminate the instances running the old version.
- **Architecture:**
    
    `[Clients] --> [ALB] --> [Target Group] --> [ASG (Mixed Instances: Old & New Version)]`
    
- **Implications:**
    - **Simplicity:** Relatively straightforward to implement.
    - **Mixed Versions:** Traffic is served by both old and new application versions concurrently, which might be acceptable or problematic depending on compatibility.
    - **No Granular Testing:** Difficult to test the new version with a specific subset of traffic before a full rollout.
    - **Potential for Issues:** If the new version has critical bugs, it could impact all users receiving traffic to those instances.

## **2. Blue/Green Deployment with Two ASGs and Two Target Groups**

![image.png](image%2018.png)

- **Process:**
    1. Maintain the existing ASG (the "blue" environment) and its associated Target Group.
    2. Create a **new ASG** (the "green" environment) with the updated application version and a **new Target Group**.
    3. Configure the ALB to initially send all traffic to the "blue" Target Group.
    4. Gradually shift a small percentage of traffic from the "blue" Target Group to the "green" Target Group using the ALB's traffic splitting capabilities.
    5. Monitor the "green" environment for performance and errors.
    6. If successful, gradually increase the traffic to the "green" environment until it handles 100%.
    7. Once the "green" environment is stable, the "blue" ASG and Target Group can be retired.
- **Architecture:**
    
    `[Clients] --> [ALB] --> [Target Group (Blue)] --> [ASG (Old Version)]
                       \--> [Target Group (Green)] --> [ASG (New Version)]`
    
- **Implications:**
    - **Reduced Risk:** Allows for thorough testing of the new version with a small subset of live traffic before a full cutover.
    - **Easy Rollback:** If issues are found in the "green" environment, traffic can be quickly shifted back to the "blue" environment.
    - **No Version Conflicts:** Only one version of the application serves traffic at a time for each target group.
    - **Increased Complexity:** Requires managing two ASGs and two Target Groups during the deployment phase.
    - **Cost:** May incur higher costs temporarily due to running two sets of infrastructure.

## **3. Canary Deployment with Two ALBs and Route 53 Weighted Records**

![image.png](image%2019.png)

- **Process:**
    1. Maintain the existing ALB (ALB1) connected to the ASG with the old application version.
    2. Create an **entirely new ALB** (ALB2) and a **new ASG** with the updated application version.
    3. Configure **Route 53** with a DNS record (e.g., a CNAME) that uses **weighted records** to distribute traffic between the DNS names of ALB1 and ALB2.
    4. Initially, assign a small weight to ALB2, directing a small percentage of client DNS requests to the new ALB and its ASG.
    5. Monitor the new application version accessed through ALB2.
    6. Gradually increase the weight of ALB2 in Route 53 to shift more traffic to the new environment.
    7. Once ALB2 handles all the traffic, the weight for ALB1 can be set to zero, and eventually, ALB1 and its ASG can be retired.
- **Architecture:**
    
    `[Clients] --> [Route 53 (Weighted Records)] --> [ALB1] --> [ASG (Old Version)]
                                             \--> [ALB2] --> [ASG (New Version)]`
    
- **Implications:**
    - **Independent Testing:** Allows for thorough and isolated testing of the new application version behind ALB2 before exposing it to the majority of users.
    - **Client-Side Load Balancing:** Relies on clients making DNS queries and respecting the Time-To-Live (TTL) for traffic shifting. Poorly behaving clients might not switch promptly.
    - **Slower Rollout:** Traffic shifting is gradual and dependent on DNS propagation and client behavior.
    - **Increased Complexity:** Involves managing two ALBs and Route 53 configurations.
    - **Potential for Inconsistent Experience:** Clients might experience different application versions depending on when they last resolved the DNS.

## **Key Takeaways for the Exam**

- **Multiple Valid Solutions:** There are often several ways to achieve a goal in AWS.
- **Context Matters:** The "best" solution depends on the specific requirements, risk tolerance, and complexity considerations of the scenario.
- **Architectural Implications:** Each approach has different implications for traffic management, testing, rollback, cost, and complexity.
- **Understanding Trade-offs:** As a Solution Architect, you need to understand the trade-offs of each approach to recommend the most appropriate solution.
- **Focus on the "Most Appropriate":** The exam often presents multiple correct answers, but you must identify the one that best fits the given constraints and objectives.

This lecture effectively illustrates the decision-making process of an AWS Solution Architect, considering various factors to choose the optimal approach for a seemingly simple task like application updates in an Auto Scaling Group.