import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Send a test prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what a syllabus is in two sentences."
)

print(response.text)