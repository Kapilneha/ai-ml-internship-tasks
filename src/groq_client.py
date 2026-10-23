import os

from dotenv import load_dotenv
from openai import OpenAI

from src.response_parser import parse_json_response


load_dotenv()

GROQ_BASE_URL = "https://api.groq.com/openai/v1"
DEFAULT_MODEL = "openai/gpt-oss-20b"


def create_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from .env")

    return OpenAI(
        api_key=api_key,
        base_url=GROQ_BASE_URL
    )


def classify_text(text):
    client = create_groq_client()

    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                        "Classify the user's message into exactly one category: "
                        "bug_report, feature_request, billing, account_access, "
                        "general_question, or other. "
                        "Use bug_report for reports of errors or broken behavior. "
                        "Use feature_request for requests to add or improve functionality. "
                        "Use billing for payments, invoices, or charges. "
                        "Use account_access for login or account recovery issues. "
                        "Use general_question for other ordinary questions. "
                        "Use other when no category fits. "
                        "Return a JSON object with exactly three fields: "
                        "category, confidence, and explanation. "
                        "confidence must be a number between 0 and 1. "
                        "explanation must briefly justify the selected category. "
                        "Base the classification only on the user's message. "
                        "Do not include Markdown fences or text outside the JSON object."
                    )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={"type": "json_object"},
        max_completion_tokens=1024
    )

    response_text = response.choices[0].message.content

    return parse_json_response(response_text)
