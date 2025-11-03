# SSL/TLS encyrption

# **SSL/TLS and Man-in-the-Middle (MITM) Attacks**

## **SSL vs. TLS**

- **SSL (Secure Socket Layer):** An older protocol for encrypting connections.
- **TLS (Transport Layer Security):** A newer and more secure version of SSL.
- **Common Usage:** Despite TLS being the standard, the term "SSL" is still widely used to refer to TLS certificates and encryption. When you hear "SSL," it generally means TLS.

## **SSL Certificates and Certificate Authorities (CAs)**

- **Public SSL Certificates:** Issued by trusted third-party organizations called Certificate Authorities (CAs).
- **Examples of CAs:** Comodo, Symantec, GoDaddy, GlobalSign, Digicert, Letsencrypt, etc.
- **Expiration:** Certificates have an expiration date and must be renewed before expiry to maintain service availability.

## **How SSL Encryption Works (Simplified)**

1. **Asymmetric Handshake:** The initial connection between the client and server uses asymmetric encryption (which is computationally expensive).
2. **Symmetric Key Exchange:** During the handshake, the client and server negotiate and exchange a shared, unique symmetric key for the current session.
3. **Symmetric Encryption for Data Transfer:** For all subsequent communication during that session, the much faster symmetric encryption is used with the agreed-upon key.
4. **Handshake Details (High-Level):**
    - **ClientHello:** Client sends supported cipher suites and a random value.
    - **ServerHello:** Server responds with its chosen cipher suite, a server random value, and its SSL certificate.
    - **Certificate Verification:** The client verifies the authenticity of the server's SSL certificate.
    - **Master Secret:** The client generates a master symmetric key, encrypts it using the server's public key from the certificate, and sends it to the server.
    - **Optional Client Certificate:** If required (two-way SSL), the client sends its certificate.
    - **Secure Connection Established:** The server decrypts the master secret using its private key. Now both client and server share the master secret and establish a secure, symmetrically encrypted connection.

**Note:** The exam will likely not test you on the detailed steps of the SSL/TLS handshake, but understanding the high-level process is beneficial for a Solution Architect Professional.

## **SSL SNI (Server Name Indication)**

- **Problem Solved:** SNI allows a single web server to host multiple websites with different SSL certificates.
- **Mechanism:** During the initial SSL handshake, the client indicates the hostname it is trying to connect to.
- **Server Action:** The server uses this information to select and present the correct SSL certificate for that hostname. If no matching certificate is found, it may return a default certificate.
- **AWS Load Balancers and CloudFront:**
    - **Supported:** Application Load Balancer (ALB), Network Load Balancer (NLB), and CloudFront support SNI.
    - **Not Supported:** Classic Load Balancer (CLB) does **not** support SNI.

**Example with ALB:**

- An ALB with SNI enabled can have multiple SSL certificates loaded onto it, each associated with a different hostname (and potentially different target groups).
- When a client connects to `www.mycorp.com`, the ALB uses the SSL certificate associated with that hostname and routes the traffic to the corresponding target group.
- Similarly, a connection to `Domain1.example.com` will use its respective SSL certificate and target group.

**Implication for CLB:** If you need to serve multiple applications with different SSL certificates using a Classic Load Balancer, you would need to provision multiple CLBs (one for each application/certificate).

## **Protecting Against SSL Man-in-the-Middle (MITM) Attacks**

**Scenario:** A malicious "Pirate Server" intercepts communication between a user and a "Good Server."

**HTTP Vulnerability:** With plain HTTP, the Pirate Server can easily intercept and modify traffic. This is why using HTTP for public-facing services is highly discouraged.

**HTTPS and Fake Certificates:** With HTTPS, the Pirate Server might try to present a fake SSL certificate to the user.

- **Detection:** If the user's machine is not compromised, the browser will typically detect the fake certificate and warn the user, preventing the connection.
- **Compromise:** If the Pirate Server has managed to make its certificate trusted on the user's machine (e.g., through malware), the user might unknowingly establish a secure connection with the attacker.

**Prevention Strategies:**

1. **Use HTTPS:** Always use HTTPS (HTTP over SSL/TLS) for public-facing servers. This encrypts the communication between clients and servers, making it much harder for attackers to eavesdrop or tamper with data.
2. **Implement DNSSEC (DNS Security Extensions):**
    - **DNS Attack Vector:** Attackers can forge DNS responses to redirect users to malicious servers.
    - **DNSSEC Protection:** DNSSEC adds cryptographic signatures to DNS records, allowing clients to verify the authenticity and integrity of DNS responses. This prevents DNS spoofing and cache poisoning attacks.
    - **Amazon Route 53 and DNSSEC:**
        - Supports DNSSEC for domain registration.
        - As of December 2020, also supports DNSSEC for the DNS service itself using KMS.
    - **Alternative:** You could run custom DNS servers (e.g., Bind, dnsmasq, KnotDNS, PowerDNS) on EC2 instances and configure DNSSEC directly. However, Route 53 now offers managed DNSSEC.

**Key Takeaway:** To protect against MITM attacks, enforce HTTPS to encrypt communication and implement DNSSEC to secure the DNS resolution process.