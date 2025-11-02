# Kendra

## **Amazon Kendra - Key Concepts**

Amazon Kendra is a fully managed, machine learning-powered document search service.**1** It enables users to extract specific answers from within various types of documents, including:

- Text
- PDF
- HTML
- PowerPoint
- Microsoft Word
- FAQs
- And more

## **Functionality**

1. **Data Source Integration:** Kendra can connect to numerous data sources where documents are stored (examples shown in the lecture include Amazon S3, SharePoint, databases, etc.).
2. **Intelligent Indexing:** Kendra indexes the content of these documents, building a knowledge index powered by machine learning.
3. **Natural Language Search:** End-users can perform searches using natural language questions, similar to using a search engine like Google
    - *Example:* Instead of searching for keywords, a user can ask, "Where is the IT support desk?"
    - Kendra can understand the intent and provide a direct answer, such as "1st floor," if that information is present in the indexed documents.

1. **Incremental Learning:** Kendra learns from user interactions and feedback to improve search result relevance over time, promoting preferred results.
2. **Search Result Fine-tuning:** Administrators can adjust search results based on factors like data importance, freshness, or custom filters.

## **Exam Relevance**

For the exam, the key takeaway is that **Amazon Kendra is the AWS service for document search**.**11** If a question involves searching within documents and extracting answers using natural language, Kendra is the service to consider.