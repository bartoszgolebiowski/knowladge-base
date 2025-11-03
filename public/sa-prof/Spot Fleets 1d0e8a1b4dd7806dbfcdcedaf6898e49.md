# Spot Fleets

## **EC2 Spot Instances**

- **Discount:** Offer discounts up to 90% compared to On-Demand instances.
- **Pricing:** Based on supply and demand; fluctuates in real-time per Availability Zone (AZ) and instance type.
- **Bidding:** You define a **maximum spot price** you are willing to pay.
- **Instance Availability:** You get the instance as long as the current spot price is below your maximum bid.
- **Reclamation:** AWS can reclaim spot instances with a **two-minute warning** if the spot price exceeds your maximum bid or due to capacity constraints.
    
    **1**
    
- **Handling Reclamation:** The two-minute grace period allows for:
    - Shutting down applications gracefully.
    - Saving data.
    - Performing necessary cleanup.
- **Ideal Use Cases:**
    - Batch jobs
    - Data analysis
    - Workloads resilient to interruption
    - Development and testing
- **Not Suitable For:**
    - Critical production workloads
    - Databases or stateful applications where data loss is unacceptable

### **Spot Price Behavior**

- Spot prices vary by:
    - Instance type (e.g., m4.large)
    - Availability Zone (e.g., us-east-1a, us-east-1b)
    - Time
- **User-Defined Max Price:** Setting a higher max price increases the likelihood of getting and retaining the instance but reduces potential savings. Setting a lower max price increases savings but also the risk of interruption.
- **Graph Interpretation:** Demonstrates how the spot price fluctuates compared to the On-Demand price and a user's maximum bid.

## **EC2 Spot Fleets**

- **Concept:** A collection of Spot Instances and optionally On-Demand Instances, allowing you to define a target capacity and price constraints.
- **Goal:** The Spot Fleet attempts to meet your target capacity using the most cost-effective Spot Instances available within your defined parameters.
- **Launch Pools:** You define multiple launch specifications (instance types, AMIs, AZs, subnets). The fleet will choose from these pools.
- **Termination:** Instances are launched until the fleet reaches your target capacity or your defined budget is met.

### **Spot Fleet Allocation Strategies**

- **`lowestPrice`:** The fleet launches instances from the pools with the lowest current spot price. This is often the most cost-optimized strategy for short workloads.
    
    **2**
    
- **`diversified`:** The fleet distributes instances across all specified pools. This enhances availability and is suitable for longer workloads as it reduces the impact of price spikes or capacity limitations in a single pool.
    
    **3**
    
- **`capacityOptimized`:** The fleet launches instances from the pools with the most available capacity for the instance types you've selected. This aims to minimize the risk of instances being interrupted due to lack of capacity.
- **`priceCapacityOptimized`:** The fleet prioritizes pools with optimal capacity and then selects the lowest price within those capacity-optimized pools. This is often the best balance of cost savings and availability for many workloads.

### **Benefits of Spot Fleets**

- **Greater Cost Savings:** Intelligent selection of the lowest-priced Spot Instances across multiple pools.
- **Increased Availability (with `diversified` strategy):** Reduces the risk of losing all your Spot Instances simultaneously.
- **Flexibility:** Ability to specify multiple instance types and Availability Zones.
- **Simplified Management:** The fleet manages the process of requesting and maintaining the desired capacity.

### **Key Differences: Spot Instance Request vs. Spot Fleet**

| **Feature** | **Spot Instance Request** | **Spot Fleet** |
| --- | --- | --- |
| **Scope** | Requests a specific instance type in a specific AZ. | Requests a *fleet* of instances (Spot and optionally On-Demand) across multiple pools. |
| **Flexibility** | Limited to the specified instance type and AZ. | Highly flexible with multiple instance types, AZs, and allocation strategies. |
| **Cost Optimization** | Relies on your manual selection of instance and bid. | Automatically selects the lowest-priced instances based on the chosen strategy. |
| **Availability** | Higher risk of interruption if that specific instance or AZ has price spikes or capacity issues. | Can improve availability by diversifying across pools. |
| **Management** | Simpler for a single instance. | Manages a collection of instances based on defined capacity and strategy. |

Understanding the nuances of Spot Instances and Spot Fleets, including their pricing models, interruption risks, and allocation strategies, is crucial for designing cost-effective and resilient solutions on AWS, particularly for workloads that can tolerate interruptions. This is a likely topic for the AWS Solution Architect Professional exam.

Okay, let's break down the `capacityOptimized` and `priceCapacityOptimized` Spot Fleet allocation strategies with illustrative examples.

**`capacityOptimized` Strategy**

- **Goal:** Prioritize launching Spot Instances in pools (combinations of instance type and Availability Zone) where AWS currently has the most spare capacity. This strategy aims to reduce the likelihood of your instances being interrupted due to AWS needing that capacity back.
- **Scenario:** Imagine you need to launch 10 `m5.large` Spot Instances. You've configured your Spot Fleet to consider the following pools:
    - **Pool A:** `m5.large` in `us-east-1a` - Available Capacity: **High**
    - **Pool B:** `m5.large` in `us-east-1b` - Available Capacity: **Medium**
    - **Pool C:** `m5.large` in `us-east-1c` - Available Capacity: **Low**
- **How `capacityOptimized` Works:** The Spot Fleet service will analyze the current available capacity in each of these pools for the `m5.large` instance type. It will then prioritize launching your 10 instances in **Pool A** because it has the highest available capacity. If Pool A doesn't have enough capacity for all 10, it will then look at Pool B, and so on.
- **Example Outcome:** Your Spot Fleet will likely launch all 10 `m5.large` instances in `us-east-1a`.
- **Why Choose `capacityOptimized`?**
    - **Minimize Interruptions:** By launching in pools with ample capacity, you reduce the chances of AWS reclaiming those instances due to a sudden surge in demand.
    - **Longer Workloads:** Suitable for workloads that are sensitive to interruptions, even if it means potentially paying a slightly higher spot price compared to a less available pool.
- **Trade-off:** You might not always get the absolute lowest spot price at the moment of launch, as the primary focus is on capacity availability.

**`priceCapacityOptimized` Strategy**

- **Goal:** First, identify the pools with the most available capacity for your selected instance types. Then, among those capacity-optimized pools, select the ones with the lowest current spot price to launch your instances. This strategy attempts to balance cost savings with a reduced risk of interruption.
- **Scenario (Continuing the previous example):** Let's say the current spot prices for `m5.large` are:
    - **Pool A:** `m5.large` in `us-east-1a` (High Capacity) - Price: $0.08/hour
    - **Pool B:** `m5.large` in `us-east-1b` (Medium Capacity) - Price: $0.07/hour
    - **Pool C:** `m5.large` in `us-east-1c` (Low Capacity) - Price: $0.06/hour
- **How `priceCapacityOptimized` Works:**
    1. **Capacity Assessment:** The Spot Fleet first determines the available capacity in each pool. In our example, Pool A has the highest capacity.
    2. **Price Selection within Capacity-Optimized Pools:** Since Pool A is the most capacity-optimized, the fleet will select instances from Pool A. It will then consider the price in Pool A ($0.08/hour). If there were other pools with similarly high capacity but lower prices, the fleet would prioritize those. In this simplified example, since only Pool A has the highest capacity, it will launch instances there at $0.08/hour.
- **Example Outcome:** Your Spot Fleet will likely launch all 10 `m5.large` instances in `us-east-1a` at a price of $0.08/hour. Even though Pool C had the lowest price ($0.06/hour), it was not chosen because its capacity was low, increasing the risk of interruption.
- **Why Choose `priceCapacityOptimized`?**
    - **Balance:** A good compromise between cost savings and minimizing interruptions.
    - **Most Workloads:** Often considered the best general-purpose strategy for many workloads that can tolerate some level of interruption but want to optimize costs.
    - **Intelligent Selection:** Leverages AWS's knowledge of capacity availability to make more informed pricing decisions.
- **Trade-off:** You might not always get the absolute lowest possible spot price available across all pools, as capacity is a primary consideration.

**In Summary:**

- **`capacityOptimized` focuses purely on minimizing the risk of interruption by choosing pools with the most spare capacity, potentially at a slightly higher price.** Think of it as prioritizing stability and longer uptime.
- **`priceCapacityOptimized` tries to find the sweet spot by first ensuring good capacity availability and then selecting the lowest price *within those highly available pools*.** This strategy aims for a balance between cost efficiency and reduced interruption risk, making it a generally recommended approach for many production-like Spot Fleet deployments.

Understanding these nuances will help you choose the most appropriate Spot Fleet allocation strategy based on the specific requirements and constraints of your workload. This is a key aspect to consider for the AWS Solution Architect Professional exam.