# IAM Identity Center

## **AWS IAM Identity Center (Successor to AWS Single Sign-On)**

AWS IAM Identity Center provides a centralized way to manage single sign-on (SSO) access to multiple AWS accounts and business applications.

### **Core Purpose & Benefits**

- **Single Sign-On (SSO):** Provides "one login" for users to access assigned resources.
- **Centralized Management:** Simplifies managing user access across your AWS Organization and integrated applications.
- **Improved User Experience:** Users log in once via a central portal to access all their permitted AWS accounts and applications without needing separate credentials for each.

### **Scope of Access**

IAM Identity Center facilitates SSO access to:

1. **Multiple AWS Accounts:** Seamlessly access different accounts within your AWS Organization.
2. **Business Cloud Applications:** Integrate with applications supporting SAML 2.0 (e.g., Salesforce, Microsoft 365, Box).
3. **Custom Applications:** Connect to internal or third-party applications that support SAML 2.0.
4. **EC2 Windows Instances:** Provides login capabilities for Windows instances (details not extensively covered in the text but mentioned as a capability).

### **Identity Sources**

You can manage your users and groups using:

1. **IAM Identity Center's Built-in Identity Store:** Create and manage users and groups directly within the service.
2. **External Identity Provider (IdP):** Connect to an existing directory service, such as:
    - AWS Managed Microsoft AD (Active Directory)
    - AD Connector (for on-premises Active Directory)
    - Other SAML 2.0 IdPs (e.g., Okta, Azure AD/Entra ID, OneLogin).

### **How It Works: Key Components**

1. **Users and Groups:** Represent the individuals and teams needing access. These are either created in the built-in store or synchronized/federated from your external IdP.
2. **Permission Sets:**
    - Define a collection of permissions. They essentially package one or more IAM policies (either AWS managed or customer managed).
    - These define *what* actions users assigned this permission set can perform.
    - Crucially, when you assign a permission set to a user/group for a specific account, **IAM Identity Center automatically creates a corresponding IAM role** within that target account. This role contains the permissions defined in the permission set.
3. **Assignments:** This is the process of linking:
    - A **User or Group**...
    - ...with a specific **Permission Set**...
    - ...to one or more **AWS Accounts** (often targeted via OUs within AWS Organizations).

### **User Login Flow**

1. The user navigates to the AWS access portal URL provided by IAM Identity Center.
2. They authenticate using credentials from the configured identity source (either the built-in store or the external IdP).
3. Upon successful authentication, the portal displays the AWS accounts and applications the user is authorized to access (based on their group memberships and assignments).
4. Clicking on an account allows the user to assume the predefined IAM role (created via the permission set) within that account's console without re-entering credentials.

### **Multi-Account Permissions & Assignments**

- Permission sets allow you to define granular access across multiple accounts centrally.
- Example: A "DatabaseAdmin" permission set could grant RDS/Aurora access and be assigned to the DBA group for both "Development" and "Production" accounts. When a DBA logs in and selects the Dev account, they assume the specific IAM role created by Identity Center in the Dev account, granting them the defined database permissions *only* in that account.

### **Attribute-Based Access Control (ABAC)**

- IAM Identity Center supports ABAC by allowing you to use user attributes (e.g., `CostCenter`, `Title`, `Locale`) stored in the Identity Center identity store.
- These attributes can be referenced within permission set policies to implement fine-grained access control.
- **Use Case:** Define a permission set once that grants access based on an attribute (like `CostCenter`). You can then change a user's access simply by modifying their `CostCenter` attribute, rather than changing multiple permission set assignments.

**Recommendation:** Using AWS IAM Identity Center is highly recommended for managing access in environments with multiple AWS accounts.