
from unittest.mock import patch, MagicMock

import pytest

from src.response_parser import parse_json_response
from src.groq_client import classify_text


def test_valid_response():
    text = """
    {
        "category": "billing",
        "confidence": 0.95,
        "explanation": "The user reports a billing problem."
    }
    """

    result = parse_json_response(text)

    assert result["category"] == "billing"
    assert result["confidence"] == 0.95
    assert result["explanation"] == "The user reports a billing problem."


def test_missing_field():
    text = """
    {
        "category": "billing",
        "confidence": 0.95
    }
    """

    with pytest.raises(ValueError, match="Missing field"):
        parse_json_response(text)


def test_wrong_data_type():
    text = """
    {
        "category": "billing",
        "confidence": "high",
        "explanation": "The user reports a billing problem."
    }
    """

    with pytest.raises(ValueError, match="confidence must be a number"):
        parse_json_response(text)


def test_classify_text():
    fake_response = MagicMock()
    fake_response.choices[0].message.content = """
    {
        "category": "billing",
        "confidence": 0.95,
        "explanation": "The user reports a billing problem."
    }
    """

    with patch("src.groq_client.create_groq_client") as mock_client_factory:
        mock_client = mock_client_factory.return_value
        mock_client.chat.completions.create.return_value = fake_response

        result = classify_text("I was charged twice.")

    assert result["category"] == "billing"
    assert result["confidence"] == 0.95
    assert result["explanation"] == "The user reports a billing problem."


def test_invalid_json():
    text = "{invalid json}"

    with pytest.raises(ValueError, match="Invalid JSON"):
        parse_json_response(text)


def test_unexpected_field():
    text = """
    {
        "category": "billing",
        "confidence": 0.95,
        "explanation": "Duplicate charge reported.",
        "extra": "unexpected value"
    }
    """

    with pytest.raises(ValueError, match="Unexpected fields"):
        parse_json_response(text)


def test_confidence_out_of_range():
    text = """
    {
        "category": "billing",
        "confidence": 1.5,
        "explanation": "Duplicate charge reported."
    }
    """

    with pytest.raises(ValueError, match="confidence must be between 0 and 1"):
        parse_json_response(text)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
