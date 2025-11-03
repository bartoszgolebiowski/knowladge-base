# CloudGuru

## **Amazon CodeGuru - Key Concepts**

Amazon CodeGuru is a machine learning-powered service designed to improve code quality and application performance through:

1. **Automated Code Reviews (CodeGuru Reviewer)**
2. **Application Performance Recommendations (CodeGuru Profiler)**

## **CodeGuru Reviewer**

- **Purpose:** Performs automated code reviews using static code analysis.
- **Trigger:** Analyzes code pushed to repositories like CodeCommit, GitHub, and Bitbucket.
- **Benefits:**
    - Identifies potential bugs, memory leaks, and other issues early in the development cycle.
    - Can detect issues that human reviewers might miss due to its machine learning capabilities.
    - Provides actionable recommendations directly within the code repository.
    - Helps implement coding best practices.
    - Detects resource leaks and potential security vulnerabilities (e.g., input validation issues).
- **Mechanism:** Uses machine learning models trained on code reviews from thousands of open-source projects and Amazon's internal repositories.
- **Supported Languages:** Currently supports Java and Python.
- **Integrations:** Works with popular code repositories like GitHub, Bitbucket, and AWS CodeCommit.

## **CodeGuru Profiler**

- **Purpose:** Provides insights and recommendations for application performance during runtime (pre-production and production).
- **Benefits:**
    - Detects and helps optimize expensive lines of code before deployment.
    - Identifies performance bottlenecks and cost improvement opportunities in live applications.
    - Helps remove code inefficiencies and improve application performance (e.g., reduce CPU utilization).
    - Can decrease compute costs.
    - Provides heap summaries to identify memory-intensive objects.
    - Offers anomaly detection for unusual application behavior.
- **Scope:** Can monitor applications running on AWS Cloud or even on-premises with minimal overhead.

## **Exam Relevance**

Remember the high-level distinction:

- **CodeGuru Reviewer:** Focuses on **static code analysis** to find potential issues *before* runtime.
- **CodeGuru Profiler:** Focuses on **runtime behavior** to identify performance bottlenecks and cost optimization opportunities *during* application execution.

Understanding these two components and their primary functions is key for the exam.