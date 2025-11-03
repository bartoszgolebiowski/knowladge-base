# Redundant Connections

To make your connection between your data center and AWS redundant, you have several options, often involving establishing multiple connections and ensuring alternative paths for network traffic. Here's a breakdown of the common approaches:

**1. Active-Active VPN Connections:**

- Establish two or more VPN connections from your corporate data centers to your AWS Virtual Private Gateway (VGW).
- Deploy multiple VPN appliances in your data centers for redundancy on your side.
- Connect your corporate data centers with internal, high-bandwidth connectivity.
- **How it provides redundancy:** If one VPN connection fails, traffic can be routed through the active VPN connection from either data center. The internal connectivity between your data centers ensures that even if a single data center's VPN fails, the other can still provide a path to AWS.

**2. Redundant Direct Connect Connections:**

- Establish two or more Direct Connect connections to different AWS Direct Connect locations.
- These connections should ideally originate from different corporate data centers for maximum resilience against a single on-premises site failure.
- Ensure internal connectivity between your data centers.
- **How it provides redundancy:** If one Direct Connect connection or an entire Direct Connect location becomes unavailable, traffic can fail over to the other Direct Connect connection through the alternative data center.

**3. Hybrid Backup (VPN and Direct Connect):**

- Utilize a combination of Direct Connect and VPN connections.
- For example, have a primary Direct Connect connection for high bandwidth and low latency, and a secondary VPN connection as a backup over the public internet.
- This provides redundancy against failures in the Direct Connect infrastructure or your physical connection to it.
- **How it provides redundancy:** If the Direct Connect connection fails, traffic can automatically fail over to the VPN connection.

**4. Direct Connect Gateway SiteLink:**

![image.png](image%2042.png)

- This feature allows you to send data directly between your on-premises data centers connected to different Direct Connect locations, bypassing AWS Regions.
- While primarily for data center-to-data center communication, it indirectly contributes to overall resilience.
- **How it provides redundancy (Indirectly):** If connectivity to AWS through one Direct Connect location is disrupted, your data center at that location might still be able to communicate with your other data center (and potentially reach AWS through the other data center's connection).
- **Mechanism:** You connect your data centers to different Direct Connect locations. By enabling SiteLink on a Direct Connect Gateway, traffic between these locations can be routed directly at the Direct Connect location level, without traversing AWS Regions.

**Key Considerations for Redundancy:**

- **Diverse Paths:** Ensure your redundant connections utilize different physical paths and, where possible, terminate at different AWS Direct Connect locations or Availability Zones within a Region.
- **Autonomous Systems (ASNs):** When configuring BGP for routing over redundant connections, ensure proper ASN configuration to facilitate correct path selection and failover.
- **Monitoring and Alerting:** Implement robust monitoring to detect connection failures promptly and trigger automatic failover mechanisms.
- **Testing:** Regularly test your failover mechanisms to ensure they function as expected when a connection outage occurs.

By implementing one or a combination of these strategies, you can significantly improve the resilience and availability of your connectivity between your on-premises data centers and your AWS environment.