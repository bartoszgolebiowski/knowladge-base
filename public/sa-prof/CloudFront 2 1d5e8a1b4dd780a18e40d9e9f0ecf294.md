# CloudFront 2

# AWS Solution Architect Professional - More on Amazon CloudFront

## Geo Restriction

- **Purpose:** Control which users can access your CloudFront distribution based on their geographic location.
- **Mechanism:** Uses a third-party Geo-IP database within CloudFront to determine the user's country.
- **Types of Restriction:**
    - **Allow List (Whitelist):** Only users from specified countries can access the content.
    - **Block List (Blacklist):** Users from specified countries are blocked from accessing the content.
- **Use Case:** Enforcing copyright laws, restricting access from unwanted regions.
- **Geo Customization:** CloudFront automatically adds the `CloudFront-Viewer-Country` header to requests, allowing your origin or Lambda@Edge functions to customize content based on the viewer's country.

## CloudFront Pricing

- **Edge Location Costs:** Data transfer costs vary based on the geographic location of the Edge Location.
- **Price Table:** Costs generally range from lower (e.g., US, Mexico, Canada) to higher (e.g., India).
- **Price Classes:** Used to reduce costs by limiting the number of Edge Locations used for your distribution.
    - **Price Class All:** Uses all CloudFront Edge Locations globally (best performance, highest cost).
    - **Price Class 200:** Includes most regions but excludes the most expensive ones (cost reduction with good performance).
    - **Price Class 100:** Includes only the least expensive regions (maximum cost reduction, potentially lower performance for some users).
- **Considerations:** Choosing a price class involves a trade-off between cost and performance for your global user base.

## Signed URLs

- **Purpose:** Control access to specific content in your CloudFront distribution for a limited time.
- **Mechanism:** Generates a time-limited URL that grants access to a specific resource.
- **Workflow:**
    1. Client requests access to protected content.
    2. Client authenticates and is authorized by your application server.
    3. Application server (with a trusted signer configuration) uses the AWS SDK to generate a signed URL for the requested content on CloudFront.
    4. The signed URL is returned to the client.
    5. The client can then directly access the content on CloudFront using the signed URL before it expires.
- **Use Case:** Protecting content in S3 or other origins so that not everything in the CloudFront distribution is publicly accessible.

### CloudFront Signed URLs vs. S3 Pre-Signed URLs

| Feature | CloudFront Signed URL | S3 Pre-Signed URL |
| --- | --- | --- |
| **Scope** | Access to a path within the CloudFront distribution (origin-agnostic). | Issues a request as the signing IAM principal for a specific S3 object. |
| **Signing Key Management** | Account-wide key pair managed by the root account only. | Uses the IAM key of the signing IAM principal. |
| **Filtering Capabilities** | By IP, path, date, expiration (more complex). | Limited lifetime. |
| **Operations** | Primarily for downloading content. | Can be used for both uploading and downloading. |
| **Caching** | Leverages CloudFront's caching features. | Bypasses CloudFront caching (direct S3 access). |

## Custom Error Pages

- **Purpose:** Return user-friendly custom error pages when the origin server returns HTTP error status codes (e.g., 4xx, 5xx) to CloudFront.
- **Mechanism:** You configure CloudFront to serve specific objects (e.g., HTML files) from your distribution (e.g., an S3 bucket) when it receives certain error responses from the origin.
- **Caching:** Custom error pages can also be cached at Edge Locations using a minimum TTL (Time-to-Live).
- **Workflow:**
    1. A user request is made to CloudFront.
    2. CloudFront forwards the request to the origin.
    3. The origin responds with an error code (e.g., 403, 500).
    4. Instead of sending the origin's error response to the client, CloudFront retrieves the configured custom error page from your specified location (e.g., S3).
    5. The custom error page is served to the client and can be cached at the Edge Location for subsequent similar errors.
- **Benefits:** Provides a better user experience by displaying informative and branded error pages instead of default origin error messages.