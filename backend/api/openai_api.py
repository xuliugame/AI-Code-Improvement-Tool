import os
import openai
from dotenv import load_dotenv

# Load local .env file (for local development)
load_dotenv()

# Try to get API key from GitHub Secrets first, then fallback to .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

# Ensure OpenAI API Key is set
if not OPENAI_API_KEY:
    raise ValueError("Error: OpenAI API Key not found. Please set it in GitHub Secrets or a local .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def optimize_code(code_snippet):
    """
    Sends the provided code snippet to OpenAI for optimization suggestions.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI assistant helping improve code quality."},
                {"role": "user", "content": f"Analyze and optimize this code:\n{code_snippet}"}
            ]
        )

        # Extract the optimized suggestion from the response
        return response.choices[0].message.content.strip()

    except openai.APIConnectionError:
        return "Error: Unable to connect to OpenAI API. Check your internet connection."
    except openai.AuthenticationError:
        return "Error: Invalid OpenAI API Key. Please verify your key."
    except openai.APIError as e:
        return f"Error: OpenAI API returned an error: {e}"
    except Exception as e:
        return f"Error: {str(e)}"

