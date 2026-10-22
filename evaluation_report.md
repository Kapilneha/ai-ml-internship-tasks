
# Task 4: Semantic Search Evaluation

## Objective
Build a semantic search system that retrieves relevant documents
by comparing query and document embeddings using cosine similarity.

## Implementation
- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Documents: 20 sample documents
- Embedding dimensions: 384
- Similarity measure: cosine similarity
- Retrieval: Top 3 documents ranked by similarity score

## Test Queries

| No. | Query | Expected Relevant Topic |
|---|---|---|
| 1 | How do computers learn from data? | Machine learning |
| 2 | How can I store and retrieve information from a database? | SQL or PostgreSQL |
| 3 | How do I track changes in my code? | Git |
| 4 | How can I build a website? | HTML, CSS, or Python |
| 5 | How can I protect my computer from hackers? | Cybersecurity |

## Results and Observations

The five queries were executed successfully.

The cybersecurity query returned the cybersecurity document
as its highest-ranked result, with a cosine similarity score
of 0.4660.

The first query previously returned the machine learning
document as its highest-ranked result, with a score of 0.6891.

The remaining query results should be reviewed to determine
whether the expected topics appear near the top.

## Limitations
- The document collection contains only 20 sample documents.
- Similarity scores are not probabilities or accuracy percentages.
- Some lower-ranked results may be only loosely related to a query.
- Evaluation is based on a small, manually selected set of queries.

## Conclusion
The prototype successfully converts text into embeddings,
calculates cosine similarity, and ranks documents for a query.
Further testing with more documents and queries would help
evaluate its retrieval quality.
