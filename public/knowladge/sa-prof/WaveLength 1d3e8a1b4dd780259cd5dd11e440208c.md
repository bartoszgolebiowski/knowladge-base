# WaveLength

# AWS Wavelength

AWS Wavelength Zones are infrastructure deployments that embed AWS compute and storage services within telecommunications providers' (telcos) data centers at the edge of 5G networks. This brings AWS services closer to 5G devices and end-users, enabling ultra-low latency for innovative applications.

**Key Association:** Think **5G** when you encounter **Wavelength** in exam questions.

## Core Concept

Deploy AWS services (like EC2, EBS, VPC) directly at the edge of 5G networks to achieve extremely low latency for applications accessed by 5G mobile devices.

## Architecture

- **Telco 5G Network Integration:** Wavelength Zones are located within the data centers of telecommunication carriers that have deployed 5G networks.
- **Carrier Gateway:** A mechanism that enables connectivity to the Wavelength Zone.
- **AWS Services at the Edge:** You can deploy specific AWS resources, such as:
    - Amazon EC2 instances
    - Amazon EBS volumes
    - Amazon VPC (subnets within a Wavelength Zone)
- **Proximity to 5G Users:** Applications deployed in a Wavelength Zone are physically closer to end-users on 5G networks, minimizing network hops and latency.
- **Traffic Flow:** Traffic from a 5G device to an application in a Wavelength Zone can remain within the Communication Service Provider (CSP) network and may not need to traverse back to the main AWS Region for processing.
- **Connectivity to Parent Region:** Wavelength Zones are connected to their parent AWS Region. This allows resources in the Wavelength Zone to securely access a broader range of AWS services in the parent Region (e.g., RDS, DynamoDB). Standard AWS networking principles apply for this connectivity.

## Pricing

There are **no additional charges or service agreements specifically for using Wavelength Zones** beyond the standard pricing for the AWS resources you deploy within them (e.g., EC2, EBS).

## Use Cases (Requiring Ultra-Low Latency via 5G)

- **Smart Cities:** Real-time processing of data from connected devices.
- **ML-assisted Diagnostics:** Low-latency inference for medical imaging and analysis.
- **Connected Vehicles:** Real-time communication and processing for autonomous driving and vehicle-to-everything (V2X) applications.
- **Interactive Live Video Streams:** Low-delay streaming for interactive broadcasts and events.
- **AR/VR (Augmented and Virtual Reality):** Immersive experiences with minimal lag.
- **Real-time Gaming:** Cloud gaming with responsiveness comparable to local gaming.
- Any application demanding extremely low latency and proximity to mobile users on 5G networks.

In essence, AWS Wavelength brings the power of AWS compute and storage to the edge of 5G networks, unlocking new possibilities for ultra-low latency applications and enhancing the user experience for mobile devices.