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
                    "Classify the user's message. Return a JSON object "
                    "with category, confidence, and explanation. "
                    "category must be one of: bug_report, feature_request, "
                    "billing, account_access, general_question, other. "
                    "confidence must be a number from 0 to 1. "
                    "explanation must be a non-empty string."
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
