
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load the API key from the .env file
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

# Create a Claude API client
client = Anthropic(api_key=api_key)

# Send a test request to Claude
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: Claude API is working!"
        }
    ]
)

# Display Claude's response
print(response.content[0].text)
