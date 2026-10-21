# AI/ML Engineering Internship

## Overview

This repository contains my work for Tasks 1 and 2 of the AI/ML Engineering internship training roadmap. The tasks focus on setting up the development environment, understanding Git and GitHub workflows, integrating an LLM API, and parsing structured JSON responses.

## Task 1: Development Environment and API Setup

### Objectives
- Configure Git and SSH authentication.
- Clone and configure the training repository.
- Set up a Python virtual environment.
- Make a working API test call.

### Work Completed
- Configured Git and SSH authentication for GitHub.
- Set up the project locally using Python and VS Code.
- Created and activated a Python virtual environment.
- Installed the required Python packages.
- Created scripts to explore API connectivity and JSON responses.
- Tested LLM API integration using Groq.

### Files
- `claude_api_check.py`
- `claude_json.py`
- `requirements.txt`
- `.gitignore`

### Learning Outcomes
- Git and SSH configuration.
- Python virtual environments and package management.
- API keys and environment variables.
- Sending API requests and processing responses.

**Implementation note:** The original training task mentions the Claude API. Due to the Anthropic API credit limitation, Groq was used for the working LLM API implementation.

## Task 2: Git Branch/PR Workflow and JSON Response Parsing

### Objectives
- Learn the Git branch and pull request workflow.
- Create a script that calls an LLM API.
- Parse and validate the JSON response.

### Work Completed

#### 1. Git and GitHub Workflow
- Worked with the task branch `task-1-2-claude-api`.
- Staged and committed project changes.
- Synced local changes with the remote repository.
- Prepared a pull request targeting the `main` branch.

#### 2. LLM API Integration
- Integrated the Groq API using the OpenAI-compatible Python SDK.
- Sent user messages to the model for text classification.
- Requested structured JSON output.

#### 3. JSON Parsing and Validation
- Parsed model responses into Python dictionaries.
- Checked required fields: `category`, `confidence`, and `explanation`.
- Validated the supported category values.
- Checked confidence values and data types.
- Rejected invalid JSON, missing fields, and unexpected fields.

#### 4. Command-Line Interface
- Created a command-line entry point to classify user-provided text.
- Displayed the classification result as formatted JSON.

#### 5. Automated Testing
- Created unit tests using pytest.
- Tested valid responses, invalid JSON, missing fields, unexpected fields, incorrect data types, confidence ranges, and classification behavior using a mocked client.

### Files
- `src/main.py`
- `src/groq_client.py`
- `src/response_parser.py`
- `src/__init__.py`
- `test_parser.py`
- `run_groq.py`

### Example Usage

```powershell
python -m src.main "I was charged twice for my subscription."
```

### Example Output

```json
{
  "category": "billing",
  "confidence": 0.95,
  "explanation": "The user reports being charged twice for a subscription, indicating a billing issue."
}
```

The confidence score and explanation may vary between model responses.

### Testing

Run the automated tests:

```powershell
python -m pytest -v
```

**Result:** All 7 tests passed during local verification.

## Technologies Used

- Python
- Groq API
- OpenAI Python SDK
- JSON
- python-dotenv
- pytest
- Git and GitHub

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
├── requirements.txt
├── .gitignore
├── .env
├── embeddings_similarity.ipynb
└── semantic_search.py
```

The `.env` file contains local credentials and must not be committed to GitHub. The embeddings and semantic-search files are retained for subsequent internship tasks and are not claimed as completed work here.

## Current Scope

This README documents **Task 1 and Task 2 only**. Embeddings, vector similarity, and semantic search belong to later tasks and are outside the scope of this progress report.
