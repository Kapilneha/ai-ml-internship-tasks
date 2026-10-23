# Task 5: Prompt and Embedding Code Peer Review

## 1. LLM Prompt and Classification

The classification system uses the Groq API with an OpenAI-compatible client. The system prompt defines six categories: `bug_report`, `feature_request`, `billing`, `account_access`, `general_question`, and `other`.

The prompt was reviewed to clarify category definitions, require exactly three JSON fields (`category`, `confidence`, and `explanation`), constrain confidence to the range 0 to 1, and prohibit extra text outside the JSON object.

## 2. JSON Response Validation

The response parser checks for empty responses, invalid JSON, missing or unexpected fields, invalid categories, incorrect confidence types, out-of-range confidence values, and empty explanations.

All seven existing parser tests passed.

## 3. Classification Smoke Tests

| Input | Expected category | Actual category | Result |
|---|---|---|---|
| I was charged twice for my subscription | billing | billing | Passed |
| The application crashes whenever I click Login | bug_report | bug_report | Passed |

Both test inputs produced valid JSON with the expected categories. These two examples are functional checks, not a comprehensive accuracy evaluation.

## 4. Embedding and Semantic Search Review

The semantic search implementation uses `sentence-transformers/all-MiniLM-L6-v2` to generate 384-dimensional embeddings. Document embeddings are generated once and reused for subsequent queries. Cosine similarity is used to rank documents, and the top three results are returned.

The five manually selected semantic search queries previously tested all returned their expected topic as the highest-ranked result. This is an observed top-1 success rate of 5/5 on the selected examples, not a guarantee of general retrieval accuracy.

## 5. Accuracy and Cost Considerations

The embedding model runs locally, avoiding per-request charges to a hosted embedding API. Local execution still uses computation, memory, storage, and an initial model download.

The classification system uses a hosted Groq API, so its cost and availability depend on the applicable model pricing, usage limits, and service terms. No formal monetary cost or latency benchmark was performed.

## 6. Recommended Improvements

- Expand the classification and retrieval test datasets.
- Test ambiguous inputs and cases that do not fit any category.
- Measure Precision@3, Recall@3, and Mean Reciprocal Rank for semantic search.
- Improve API error handling and test malformed or empty model responses.
- Measure response latency and token usage.
- Keep API keys in environment variables and never commit `.env` files.

## Conclusion

The reviewed implementation has a clear separation between API calls, prompt construction, JSON parsing, and semantic retrieval. All seven parser tests passed, and both classification smoke tests returned the expected categories. Broader testing and formal performance measurements are needed before making general accuracy or cost-efficiency claims.