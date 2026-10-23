# Semantic Search Evaluation Report

## 1. Objective

The objective of Task 4 was to build a semantic search system that retrieves relevant documents by comparing query and document embeddings using cosine similarity.

The system was evaluated using five manually selected test queries against a collection of 20 sample documents.

## 2. Implementation

- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Document collection:** 20 sample documents
- **Embedding dimensions:** 384
- **Similarity measure:** Cosine similarity
- **Retrieval method:** Rank documents by similarity score in descending order
- **Number of results returned:** Top 3 documents per query
- **Execution:** Local Python environment using Sentence Transformers and PyTorch

Document embeddings are generated once when the program starts and reused for subsequent queries. Each search query is embedded separately and compared against the stored document embeddings.

## 3. Test Queries and Results

| No. | Test query | Expected topic | Top-ranked result | Similarity score |
|---|---|---|---|---:|
| 1 | How do computers learn from data? | Machine learning | Machine learning | 0.6891 |
| 2 | How can I store and retrieve information from a database? | SQL or PostgreSQL | SQL | 0.4743 |
| 3 | How do I track changes in my code? | Git | Git | 0.4744 |
| 4 | How can I build a website? | HTML, CSS, or Python | HTML | 0.4050 |
| 5 | How can I protect my computer from hackers? | Cybersecurity | Cybersecurity | 0.4660 |

All five queries returned ranked results, and the expected topic appeared as the highest-ranked result in each case.

## 4. Accuracy Evaluation

### Observed Top-1 Success Rate

The expected topic was the highest-ranked result for all five test queries.

Observed top-1 success rate:

5 / 5 × 100 = 100%

This result applies only to the five manually selected test queries. It should not be interpreted as proof that the system has 100% accuracy on unseen queries or real-world datasets.

### Evaluation Limitations

- The document collection contains only 20 sample documents.
- The test set contains only five manually selected queries.
- The expected topics were defined manually.
- Some queries may have multiple valid results. For example, a website-related query could match HTML, CSS, or Python.
- Similarity scores measure semantic similarity; they are not probabilities or accuracy percentages.
- The top-ranked document may not always contain enough information to answer a user's question.

### Future Evaluation Improvements

- Test with a larger and more diverse set of queries.
- Define relevant documents for each query before testing.
- Measure Precision@3, Recall@3, and Mean Reciprocal Rank (MRR).
- Include ambiguous queries and queries whose answers are absent from the document collection.
- Compare retrieval results across different embedding models.

## 5. Efficiency and Cost Analysis

### Embedding Efficiency

The system generates embeddings for all 20 documents once during initialization and reuses them for subsequent searches. This avoids repeatedly processing the entire document collection for every query.

Each query requires one query embedding and cosine similarity calculations against the stored document embeddings.

### Cost Considerations

The `all-MiniLM-L6-v2` model runs locally, so generating embeddings does not require a paid embedding API. However, local execution still uses CPU or GPU resources, memory, and storage. The model may also need to be downloaded before its first use.

The current system uses a small collection of 20 documents, making it suitable for a learning prototype. As the collection grows, a vector index such as FAISS may help improve retrieval efficiency.

No formal latency benchmark or monetary cost measurement was performed as part of this evaluation.

## 6. Limitations

- The system searches only the documents provided in its collection.
- Retrieval quality depends on the embedding model and the content of the documents.
- The current implementation uses an in-memory collection rather than a persistent vector database.
- The system retrieves relevant documents but does not independently generate answers from them.
- The small evaluation dataset limits the conclusions that can be drawn about general retrieval quality.

## 7. Conclusion

The semantic search prototype successfully converts documents and queries into embeddings, calculates cosine similarity, and ranks documents by relevance.

All five manually selected test queries returned the expected topic as the highest-ranked result. This demonstrates that the prototype works for the selected examples, while further testing is needed to assess general retrieval quality.

The implementation also avoids repeated document embedding computation by generating document embeddings once and reusing them. Future work can improve the evaluation methodology, measure latency, expand the document collection, and integrate retrieval with a language model to build a Retrieval-Augmented Generation (RAG) system.