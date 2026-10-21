# AI/ML Engineering Internship Tasks

This repository contains my work for the AI/ML Engineering internship training roadmap, covering environment setup, LLM API integration, JSON response parsing, text embeddings, and vector similarity.

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

### Technologies
- Python
- Sentence Transformers
- PyTorch
- NumPy
- pandas

## Project Structure

```text
ai_ml_setup/
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
├── requirements.txt
├── .gitignore
└── README.md
```

The `.env` file is used for local API credentials and must not be committed to GitHub. The `semantic_search.py` file is reserved for subsequent work and is not claimed as completed in these tasks.

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
- [ ] Task 4: Semantic search over sample documents
- [ ] Task 5: Peer review and accuracy/cost notes

## Security

- Store API keys in `.env`.
- Keep `.env` listed in `.gitignore`.
- Never commit API keys or other credentials to version control.

## Author

Neha Kapil  
GitHub: [Kapilneha](https://github.com/Kapilneha)
