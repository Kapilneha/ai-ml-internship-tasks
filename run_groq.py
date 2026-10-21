
import json
from src.groq_client import classify_text

text = "I was charged twice for my subscription."

try:
    result = classify_text(text)
    print("Classification successful!")
    print(json.dumps(result, indent=2))

except Exception as error:
    print(f"Request failed: {error}")
