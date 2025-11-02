# Storage Class Analysis

# **Amazon S3 Analytics (Storage Class Analysis) - Summary Notes**

## **Purpose and Goals**

- **Storage Class Optimization:** A feature designed to help you determine the optimal time to transition objects to more cost-effective storage classes.
- **Recommendations:** Provides insights and recommendations for transitioning data between the **Standard** and **Standard-IA** storage classes.
- **Limited Scope:** Does **not** provide recommendations for One Zone-IA or Glacier storage classes.

## **Functionality**

- **Daily Report Generation:** Generates a report on storage class usage and access patterns on a daily basis.
- **Initial Data Availability:** It may take **24 to 48 hours** for the analysis to begin and for data to appear after enabling the feature on an S3 bucket.
- **Data Insights:** The report provides information about the storage class of objects, their age, and access frequency.
- **Amazon QuickSight Integration:** The generated data can be easily visualized and analyzed within Amazon QuickSight for deeper insights.

## **Workflow and Benefits**

- **First Step for Lifecycle Rules:** Utilizing Storage Class Analysis is a valuable initial step in creating or refining S3 Lifecycle Rules.
- **Identifying Optimal Transition Points:** Helps identify the ideal timeframes for transitioning objects to Standard-IA based on actual access patterns, maximizing cost savings without impacting performance for frequently accessed data.
- **Data-Driven Decisions:** Enables data-driven decisions regarding storage class optimization instead of relying on estimations.

## **Visual Representation**

`+---------------------+
|     S3 Bucket       |
+---------------------+
          |
          v
+---------------------+
| Storage Class       |
|     Analysis        |
+---------------------+
          |
          v
+---------------------+
| CSV Report          |
| (Daily Updates)     |
| - Storage Class     |
| - Object Age        |
| - Access Patterns   |
| - Recommendations   |
+---------------------+
          |
          v
+---------------------+
| Amazon QuickSight   |
| (Visualization &    |
|   Advanced Analysis)|
+---------------------+
          |
          v
+---------------------+
| S3 Lifecycle Rules  |
| (Automated          |
|   Tier Transitions)|
+---------------------+`

**In summary:** S3 Analytics (Storage Class Analysis) provides valuable insights into your data access patterns for Standard and Standard-IA, helping you make informed decisions for cost optimization through S3 Lifecycle Rules. Remember its limitations regarding One Zone-IA and Glacier.