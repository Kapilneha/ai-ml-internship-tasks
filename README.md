# AI/ML Internship Tasks

This repository contains my AI/ML internship practice tasks, including Git/GitHub setup, Claude API integration, text embeddings, and semantic search.

## Task 1: Environment Setup

- Configured Git and GitHub SSH authentication.
- Created and activated a Python virtual environment.
- Installed the required Python packages.

### Verify SSH Authentication

```powershell
ssh -T git@github.com
```

Expected result: GitHub confirms successful authentication.

## Task 2: Claude API and JSON Parsing

### Files

- `claude_test.py`: Sends a basic request to Claude using the Anthropic Python SDK.
- `claude_json.py`: Requests a JSON-formatted response and parses it using Python's `json` module.

### Setup

Activate the virtual environment and install the dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install anthropic python-dotenv
```

Create a local `.env` file in the project root:

```text
ANTHROPIC_API_KEY=your_api_key_here
```

Never commit the `.env` file or share your API key.

### Run the scripts

```powershell
python claude_test.py
python claude_json.py
```

### Testing Status

- GitHub SSH authentication: successful.
- Claude API test: attempted, but blocked because the Anthropic account has insufficient API credits.
- JSON parsing with a live Claude response: pending successful API access.

The scripts are prepared, but successful live API execution has not yet been verified.

## Project Structure

```text
ai-ml-internship-tasks/
├── claude_test.py
├── claude_json.py
├── embeddings_similarity.ipynb
├── semantic_search.py
├── README.md
└── .gitignore
```
