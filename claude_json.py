
import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("Missing ANTHROPIC_API_KEY in .env")

client = Anthropic(api_key=api_key)

try:
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=150,
        messages=[
            {
                "role": "user",
                "content": (
                    "Return a JSON object with these fields: "
                    "topic (string), difficulty (string), "
                    "skills (array of strings). "
                    "Use topic Python, difficulty beginner, "
                    "and skills loops and lists. "
                    "Return only valid JSON."
                )
            }
        ]
    )

    response_text = response.content[0].text
    data = json.loads(response_text)

    print("Parsed JSON successfully!")
    print(json.dumps(data, indent=2))

except json.JSONDecodeError:
    print("Claude returned invalid JSON.")
except Exception as error:
    print(f"API request failed: {error}")
