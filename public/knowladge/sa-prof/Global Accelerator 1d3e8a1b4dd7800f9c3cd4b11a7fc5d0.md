# Global Accelerator

# AWS Global Accelerator

AWS Global Accelerator is a networking service that leverages the AWS global network infrastructure to improve the performance and availability of your applications for a global user base. It uses Anycast IP addresses to direct traffic to the closest AWS edge location, and then routes that traffic to your application endpoints over the low-latency, congestion-free AWS internal network.

## Key Concepts

- **Anycast IP Addresses:** Global Accelerator provisions two static Anycast IP addresses for your accelerator. These IPs are advertised from multiple AWS edge locations simultaneously. Clients connect to the nearest edge location using these IPs. The IPs remain constant throughout the lifecycle of the accelerator, simplifying whitelisting and preventing issues with client-side caching.
- **Edge Locations:** Global Accelerator utilizes the extensive network of AWS edge locations worldwide as entry points for user traffic.
- **AWS Global Network:** Once traffic reaches an edge location, it traverses the high-performance, low-latency AWS internal network to reach your application endpoints in the chosen AWS region(s).
- **Endpoints:** The backend resources that Global Accelerator directs traffic to. These can include:
    - Elastic IPs on EC2 instances
    - EC2 instances (private or public IPs)
    - Application Load Balancers (ALBs) (public or private)
    - Network Load Balancers (NLBs) (public or private)
- **Listeners:** You configure listeners on your accelerator to process incoming connections on specific ports and protocols (TCP or UDP).
- **Endpoint Groups:** Listeners direct traffic to endpoint groups, which are collections of your endpoints in one or more AWS regions. You can configure traffic dial percentages for endpoint groups to control traffic distribution across regions.
- **Health Checks:** Global Accelerator continuously monitors the health of your endpoints. If an endpoint becomes unhealthy, Global Accelerator stops directing traffic to it. Failover to healthy endpoints within the same or other regions typically occurs in less than one minute.

## Benefits

- **Performance Improvement:** By routing traffic over the AWS internal network from the nearest edge location, Global Accelerator reduces latency and improves application responsiveness for users globally.
- **Consistent Performance:** Intelligent routing based on real-time network conditions ensures optimal path selection and consistent user experience.
- **High Availability and Fast Regional Failover:** Health checks and the ability to configure endpoint groups in multiple regions enable automatic and rapid failover in case of endpoint or regional failures, enhancing disaster recovery capabilities.
- **Static IP Addresses:** The two Anycast IPs provide a stable entry point for your application, simplifying client whitelisting and avoiding DNS-related caching issues.
- **IP Preservation:** Global Accelerator can preserve the client IP address for endpoints other than Elastic IPs, allowing your backend applications to see the original source IP.
- **Security:** Benefits from AWS Shield Standard for DDoS protection at no additional cost. You only need to whitelist the two static Anycast IPs.
- **Global Reach:** Leverages the extensive AWS global network and edge locations to serve users worldwide.

## Use Cases

- Applications with a global user base requiring low latency and high availability.
- Gaming applications (UDP) benefiting from consistent low latency.
- IoT applications (MQTT) requiring reliable global connectivity.
- Voice over IP (VoIP) applications (UDP) needing low latency and stable IPs.
- HTTP/HTTPS applications that require static IP addresses for compliance or simplified firewall rules.
- Applications needing deterministic and fast regional failover for disaster recovery.

## Comparison with CloudFront

| Feature | AWS Global Accelerator | AWS CloudFront |
| --- | --- | --- |
| **Primary Goal** | Improve performance and availability using AWS network. | Deliver cached content at the edge with optional dynamic content acceleration. |
| **Content Delivery** | Proxies packets directly to application endpoints. | Caches content (static and dynamic) at edge locations. |
| **Protocols** | TCP and UDP (in addition to HTTP/HTTPS). | Primarily HTTP/HTTPS, with some support for other protocols. |
| **IP Addresses** | Provides two static Anycast IPs. | Uses dynamic IPs associated with edge locations. |
| **Caching** | No content caching at the edge. | Extensive content caching capabilities at edge locations. |
| **Best Suited For** | Performance-sensitive, non-HTTP use cases, static IPs, fast regional failover. | Content delivery (images, videos, static websites), dynamic content acceleration. |
| **DDoS Protection** | AWS Shield Standard included. | AWS Shield Standard included. |
| **Global Network** | Leverages the AWS global network. | Leverages the AWS global network and edge locations. |

In summary, while both services utilize the AWS global network and edge locations, **CloudFront** focuses on content caching and delivery at the edge, primarily for HTTP/HTTPS traffic. **Global Accelerator**, on the other hand, focuses on improving the performance and availability of applications by routing traffic over the AWS internal network directly to your endpoints, supporting a wider range of protocols and providing static Anycast IPs. They can also be used together in some architectures.