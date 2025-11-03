# App Sync

## **Core Concepts**

- **Managed GraphQL Service:** AppSync is a fully managed service that simplifies building GraphQL APIs.
- **GraphQL Focus:** Whenever you encounter "GraphQL," immediately associate it with AppSync.
- **Data Aggregation:** Enables applications to fetch precise data requirements, combining information from diverse sources.
- **Data Sources:** Integrates with various AWS data stores (DynamoDB, Aurora, Elasticsearch), HTTP APIs, and custom sources via Lambda.
- **Real-time Capabilities:** Supports real-time data updates using WebSockets or MQTT over WebSockets. This is a key differentiator for AppSync.
- **Mobile Optimization:** Provides features for local data access and synchronization for mobile applications.
- **Schema-Driven:** Development begins by defining a GraphQL schema.

## **AppSync Architecture**

- **Clients:** Mobile apps, web apps, real-time dashboards, and systems requiring offline synchronization interact with AppSync.
- **GraphQL Schema:** Defines the data structure, queries, mutations, and subscriptions available through the API.
- **Resolvers:** Act as the bridge between the GraphQL schema and the underlying data sources. They contain the logic to fetch and transform data.
- **Data Sources:** The various backend systems from which AppSync retrieves data:
    - DynamoDB
    - Aurora
    - Elasticsearch Service
    - Lambda (for custom data sources)
    - HTTP (for public HTTP APIs)
- **Monitoring:** Integrated with CloudWatch Metrics and Logs for observability.

## **Exam Relevance**

- **GraphQL:** AppSync is the primary AWS service for GraphQL APIs.
- **Real-time Data:** Crucial for scenarios requiring push-based updates to clients.

## **AppSync and Cognito Integration (Authorization)**

![image.png](image%2031.png)

- **Cognito-Based Authorization:** AppSync can enforce authorization based on Cognito User Pool user groups.
- **GraphQL Schema Directives:** Security rules based on Cognito groups are defined directly within the GraphQL schema using the `@aws_auth` directive.
    - Example:
        
        **GraphQL**
        
        `type Post @aws_auth(rules: [
          { allow: groups, groups: ["bloggers", "readers"], operations: [read] },
          { allow: groups, groups: ["bloggers"], operations: [create] }
        ]) {
          id: ID!
          title: String!
          content: String!
        }`
        
        - Both "bloggers" and "readers" can perform "read" operations (query).
        - Only users belonging to the "bloggers" group can perform "create" operations (mutation to add a post).
- **Solution Architecture Flow:**
    1. Client authenticates with Cognito User Pool.
    2. Cognito issues a JWT (JSON Web Token).
    3. Client includes the JWT in requests to the AppSync API.
    4. AppSync verifies the JWT and its validity with Cognito.
    5. AppSync checks the user's group membership against the authorization rules defined in the GraphQL schema.
    6. Resolvers can further inspect the user's group membership to implement fine-grained access control when interacting with backend data sources (e.g., DynamoDB).

In essence, AppSync simplifies the process of building robust and real-time APIs using GraphQL, with built-in integration for various data sources and strong security features through Cognito integration.