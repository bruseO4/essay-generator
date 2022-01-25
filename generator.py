import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(engine="text-ada-001", prompt="Say this is a test", max_tokens=6)
