
import argparse
import json

from src.groq_client import classify_text


def main():
    parser = argparse.ArgumentParser(
        description="Classify text using Groq"
    )

    parser.add_argument(
        "text",
        help="The text you want to classify"
    )

    args = parser.parse_args()

    try:
        result = classify_text(args.text)
        print(json.dumps(result, indent=2))

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
