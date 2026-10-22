# AI/ML Engineering Internship Tasks

This repository contains my work for the AI/ML Engineering internship training roadmap, covering environment setup, LLM API integration, JSON response parsing, text embeddings, vector similarity, and semantic search.

## Task 1: Environment Setup and API Connectivity

### Objectives
- Configure Git and SSH authentication.
- Set up the Python development environment.
- Create and activate a virtual environment.
- Test connectivity to an LLM API.

### Work Completed
- Configured Git and GitHub SSH authentication.
- Set up the project using Python and VS Code.
- Created and activated a Python virtual environment.
- Installed the required dependencies.
- Created scripts to explore API connectivity and JSON responses.
- Successfully tested text classification using the Groq API.

### Files
- `claude_api_check.py`
- `claude_json.py`
- `requirements.txt`
- `.gitignore`

**Implementation note:** The original training roadmap specifies the Claude API. Since the Anthropic API account had insufficient credits, Groq was used for the working LLM integration.

## Task 2: LLM API Integration and JSON Response Parsing

### Objectives
- Learn the Git branch and pull request workflow.
- Write a script that calls an LLM API.
- Parse and validate the JSON response.

### Work Completed

**LLM API integration**
- Integrated Groq using the OpenAI-compatible Python SDK.
- Sent user messages to the model for text classification.
- Requested structured JSON responses.

**Response parsing and validation**
- Parsed the model's response into a Python dictionary.
- Validated required fields: `category`, `confidence`, and `explanation`.
- Checked that the category belongs to the supported categories.
- Validated data types and confidence values between `0` and `1`.
- Rejected invalid JSON, missing fields, and unexpected fields.

**Command-line interface**
- Created an entry point to classify text supplied through command-line arguments.
- Printed formatted JSON results.

**Automated testing**
- Created unit tests using pytest.
- Tested valid responses, missing fields, invalid JSON, incorrect data types, unexpected fields, confidence range validation, and classification behavior with a mocked client.

### Files
- `src/main.py`
- `src/groq_client.py`
- `src/response_parser.py`
- `src/__init__.py`
- `test_parser.py`
- `run_groq.py`

### Example

Command:

```powershell
python -m src.main "I was charged twice for my subscription."
```

Example output:

```json
{
  "category": "billing",
  "confidence": 0.95,
  "explanation": "The user reports being charged twice for a subscription."
}
```

The exact confidence score and explanation may vary between model responses.

### Testing

```powershell
python -m pytest -v
```

**Last reported result:** All seven automated tests passed.

## Task 3: Text Embeddings and Vector Similarity

### Objectives
- Learn the fundamentals of text embeddings.
- Generate embeddings for five text samples.
- Calculate and compare vector similarity scores.

### Work Completed
- Loaded the `sentence-transformers/all-MiniLM-L6-v2` embedding model.
- Generated embeddings for five sample sentences.
- Obtained an embedding shape of `(5, 384)`, representing five sentences with 384 dimensions each.
- Calculated cosine similarity between two related sentences.
- Generated a complete similarity matrix for the five samples.
- Identified the most similar pair of distinct sentences.
- Printed similarity scores and interpreted their semantic relationship.

### Example Result

The similarity score between:

- "I love learning artificial intelligence."
- "I enjoy studying AI."

was approximately `0.807` in the earlier run.

A higher cosine similarity indicates that two embedding vectors point in more similar directions. It does not represent an exact percentage of shared meaning.

### File
- `embeddings_similarity.ipynb`

## Task 4: Semantic Search

### Objectives
- Implement semantic search over a collection of text documents.
- Generate document and query embeddings.
- Rank documents by cosine similarity.
- Evaluate retrieval results using sample queries.

### Work Completed
- Created a collection of 20 sample documents covering machine learning, programming, databases, networking, cybersecurity, and other technical topics.
- Loaded the pretrained `sentence-transformers/all-MiniLM-L6-v2` model.
- Generated 384-dimensional embeddings for all 20 documents.
- Converted user queries into embeddings using the same model.
- Calculated cosine similarity between a query and the document embeddings.
- Ranked documents by similarity and returned the top three results.
- Tested the search implementation with five sample queries.

### Example Result

Query:

```text
How do computers learn from data?
```

Top result:

```text
Machine learning allows computers to learn patterns from data.
```

Observed cosine similarity: `0.6891`.

Another test query, "How can I protect my computer from hackers?", returned the cybersecurity document as its top result, with a cosine similarity score of `0.4660`.

These scores represent similarity between embedding vectors, not probabilities or accuracy percentages.

### Evaluation

The evaluation uses five manually selected queries covering:
- Machine learning
- Databases
- Version control
- Web development
- Cybersecurity

The initial results show that the system can retrieve relevant documents based on semantic similarity. The collection is small, so broader testing would be needed to assess retrieval quality more thoroughly.

### Files
- `semantic_search.py`
- `evaluation_report.md`

### Technologies
- Python
- Sentence Transformers
- PyTorch
- NumPy

## Project Structure

```text
ai-ml-internship-tasks/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── groq_client.py
│   └── response_parser.py
├── test_parser.py
├── run_groq.py
├── claude_api_check.py
├── claude_json.py
├── embeddings_similarity.ipynb
├── semantic_search.py
├── evaluation_report.md
├── requirements.txt
├── .gitignore
└── README.md
```

The `.env` file is used for local API credentials and must not be committed to GitHub. The `.venv` directory and model cache are local environment artifacts and should remain excluded from version control.

## Technologies Used

- Python
- Groq API
- OpenAI Python SDK
- JSON
- python-dotenv
- pytest
- Sentence Transformers
- PyTorch
- NumPy
- pandas
- Git and GitHub

## Current Progress

- [x] Task 1: Environment setup and API connectivity
- [x] Task 2: LLM integration and JSON response parsing
- [x] Task 3: Text embeddings and vector similarity
- [x] Task 4: Semantic search over sample documents
- [ ] Task 5: Peer review and accuracy/cost notes

## Security

- Store API keys in `.env`.
- Keep `.env` listed in `.gitignore`.
- Never commit API keys or other credentials to version control.

## Author

Neha Kapil  
GitHub: [Kapilneha](https://github.com/Kapilneha)
