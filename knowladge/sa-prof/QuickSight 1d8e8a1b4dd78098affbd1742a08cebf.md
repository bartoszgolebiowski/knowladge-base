# QuickSight

# **Amazon QuickSight - Serverless Business Intelligence Service**

## **Purpose and Goals**

- Serverless, machine-powered Business Intelligence (BI) service.
- Enables the creation of interactive dashboards and visualizations.
- Facilitates data-driven insights through analysis.

## **Core Concepts**

- **Interactive Dashboards:** Allows users to create rich and interactive visual representations of their data.
- **Fast and Scalable:** Designed for performance and automatic scaling to handle varying user loads.
- **Embedding:** Dashboards can be embedded within websites and applications.
- **Per-Session Pricing:** Cost model based on user sessions.

## **Use Cases**

- Business analytics
- Building data visualizations
- Performing ad-hoc visual analysis
- Gaining business insights from data

## **Data Source Connectivity**

QuickSight can connect to a wide range of data sources:

- **AWS Data Sources:**
    - Amazon RDS
    - Amazon Aurora
    - Amazon Redshift (Data Warehouse)
    - Amazon Athena (Serverless SQL for S3)
    - Amazon S3 (Direct data import)
    - Amazon OpenSearch Service
    - Amazon Timestream (Time Series Database)
- **Third-Party SaaS Applications (Examples):**
    - Salesforce
    - Jira (Full list available on the QuickSight website)
- **Third-Party Databases:**
    - Teradata
    - On-premises databases (via JDBC protocol)
- **Direct Data Import:**
    - Excel files (.xlsx, .xls)
    - CSV files (.csv)
    - JSON documents (.json)
    - TSV files (.tsv)
    - EFS CLF format (for logs)

## **SPICE Engine (Super-fast, Parallel, In-memory Calculation Engine)**

- **In-Memory Computation:** A fast, in-memory engine used by QuickSight.
- **Requirement:** Only utilized when data is **imported directly** into QuickSight.
- **Limitation:** Not used when QuickSight connects directly to external databases (e.g., Redshift, Athena).

## **User-Level Features (Enterprise Edition)**

- **Column-Level Security (CLS):** Allows administrators to control which columns are visible to specific users or groups based on their access rights.

## **Integration Highlights**

- **Common Exam Scenarios:** Frequently seen in conjunction with Amazon Athena and Amazon Redshift.

## **Dashboards and Analysis**

- **Users and Groups:**
    - **Users:** Available in the Standard edition.
    - **Groups:** Only available in the Enterprise edition.
    - **QuickSight Specific:** These users and groups are managed within the QuickSight service and are **separate from IAM users**. IAM users are primarily used for administrative access to AWS services, including QuickSight.
- **Analysis:** The environment where you create visualizations and explore data. It's a more complete and interactive workspace.
- **Dashboard:** A read-only snapshot of an analysis that can be shared with users or groups. It preserves the configuration (filters, parameters, sorting) of the analysis at the time of publishing.
- **Sharing:**
    - Both analyses and dashboards can be shared with specific QuickSight users and groups.
    - Dashboards need to be **published** before they can be shared.
    - Users with access to a dashboard can typically view the underlying data used in the visualizations.

## **Workflow**

1. Connect QuickSight to your desired data sources.
2. Create an **analysis** by selecting data fields and choosing appropriate visualizations.
3. Configure filters, parameters, controls, and sorting options within the analysis.
4. **Publish** the analysis as a **dashboard**.
5. **Share** the analysis or the published dashboard with specific QuickSight users and groups.

## **Key Takeaways for the Exam**

- Understand that QuickSight is a **serverless BI service** for creating interactive dashboards.
- Know about the **SPICE engine** and when it is utilized (direct data import).
- Be aware of **Column-Level Security** in the Enterprise edition.
- Recognize the common **AWS data sources** that QuickSight integrates with (RDS, Aurora, Redshift, Athena, S3, etc.).
- Understand the difference between **analysis** (the creation environment) and **dashboard** (the read-only shared view).
- Remember that QuickSight **users and groups are managed within the QuickSight service**, not through IAM.
- Be prepared to see scenarios involving QuickSight integrated with **Athena** and **Redshift**.