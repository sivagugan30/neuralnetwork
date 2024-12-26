import os

# Access the API_KEY environment variable
api_key = os.getenv("key10")

if not api_key:
    raise ValueError("API_KEY is not set. Ensure it's passed in the environment variables.")

print(f"My API Key is: {api_key}")
# Use the API key for API requests or other logic
