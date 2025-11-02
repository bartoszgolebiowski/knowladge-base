# Load Balancer 2

## Cross-Zone Load Balancing

Cross-Zone Load Balancing is a feature that controls how a load balancer instance distributes traffic across all registered instances in all enabled Availability Zones (AZs).

**Scenario:**

Consider two Availability Zones (AZ1 and AZ2). AZ1 has a load balancer instance with 2 EC2 instances, and AZ2 has a load balancer instance with 8 EC2 instances, all part of the same logical load balancer. A client sends 50% of its traffic to the LB instance in AZ1 and 50% to the LB instance in AZ2.

**1. With Cross-Zone Load Balancing (Enabled):**

![image.png](image%2030.png)

- Each individual load balancer instance distributes incoming traffic **evenly across all registered instances** regardless of their AZ.
- In our example:
    - The LB instance in AZ1 will distribute its 50% client traffic across all 10 EC2 instances (10% to each).
    - The LB instance in AZ2 will also distribute its 50% client traffic across all 10 EC2 instances (10% to each).
- **Outcome:** Traffic is distributed uniformly across all EC2 instances.

**2. Without Cross-Zone Load Balancing (Disabled):**

- Each load balancer instance distributes traffic **only to the EC2 instances within its own Availability Zone.**
- In our example:
    - The LB instance in AZ1 (receiving 50% client traffic) will distribute it only to the 2 EC2 instances in AZ1 (25% of the total traffic to each instance in AZ1).
    - The LB instance in AZ2 (receiving 50% client traffic) will distribute it only to the 8 EC2 instances in AZ2 (6.25% of the total traffic to each instance in AZ2).
- **Outcome:** Traffic is contained within each AZ. If there's an imbalance in the number of EC2 instances per AZ, instances in AZs with fewer instances will receive more traffic per instance.

**Cross-Zone Load Balancing Behavior per Load Balancer Type:**

| Load Balancer Type | Default State | Inter-AZ Data Transfer Costs (if enabled) | Can be Disabled? |
| --- | --- | --- | --- |
| Classic Load Balancer (CLB) | Disabled | No charges if enabled | Yes |
| Application Load Balancer (ALB) | Always On | No charges | No |
| Network Load Balancer (NLB) | Disabled | Charges apply if enabled | Yes |
| Gateway Load Balancer (GWLB) | Disabled | Charges apply if enabled | Yes |

## Sticky Sessions (Session Affinity)

- **Concept:** Directs all subsequent requests from the same client to the same backend instance for the duration of a specified period.
- **Mechanism:** The load balancer uses a cookie (set in the client's browser) with an expiration date to track which instance served the initial request. Subsequent requests with the same cookie are routed to that instance.
- **Supported by:** Classic Load Balancer (CLB) and Application Load Balancer (ALB).
- **Use Case:** Maintaining user session data on a specific backend instance (e.g., user login information) without relying on shared session storage.
- **Potential Drawback:** Can lead to an imbalance in the load across backend instances if some users have very long or active sessions.

## Routing Algorithms

Load balancers use algorithms to determine which backend instance receives a new request.

- **Least Outstanding Requests (ALB, CLB):**
    - The next request is sent to the instance with the fewest currently pending (unfinished) requests.
    - Aims to distribute load to the least busy instances.
- **Round Robin (ALB, CLB):**
    - Requests are distributed to the backend instances sequentially, one after the other, regardless of the current load on each instance.
- **Flow Hash Request Routing (NLB):**
    - A target is selected based on a hash of the protocol, source/destination IP address, source/destination port, and TCP sequence number.
    - Ensures that all TCP or UDP connections from the same source to the same destination are consistently routed to the same target for the life of that connection.
    - This provides a form of session stickiness at the network level for NLBs.
    - When a client makes a request, the NLB hashes the connection details, and the resulting hash determines the target EC2 instance. Subsequent requests within the same TCP/UDP flow will be routed to the same instance.