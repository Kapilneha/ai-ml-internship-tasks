
import json

REQUIRED_FIELDS = ("category", "confidence", "explanation")

CATEGORIES = (
    "bug_report",
    "feature_request",
    "billing",
    "account_access",
    "general_question",
    "other",
)


def parse_json_response(text):
    if not text or not text.strip():
        raise ValueError("Response is empty")

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON") from exc

    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")

    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    if set(data) != set(REQUIRED_FIELDS):
        raise ValueError("Unexpected fields found")

    if not isinstance(data["category"], str):
        raise ValueError("category must be a string")

    if data["category"] not in CATEGORIES:
        raise ValueError("Unknown category")

    confidence = data["confidence"]

    if isinstance(confidence, bool) or not isinstance(
        confidence, (int, float)
    ):
        raise ValueError("confidence must be a number")

    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")

    if not isinstance(data["explanation"], str):
        raise ValueError("explanation must be a string")

    if not data["explanation"].strip():
        raise ValueError("explanation cannot be empty")

    return data
