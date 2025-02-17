import openai
from config import OPENAI_API_KEY

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def get_code_improvements(code):
    """
    Sends code to OpenAI API for analysis and returns optimization suggestions.
    """
    prompt = f"""
    Here is a piece of code:
    ```
    {code}
    ```
    Please analyze this code, identify potential issues, and provide detailed suggestions along with an optimized version.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can also use GPT-4
            prompt=prompt,
            max_tokens=1000,
            temperature=0.5,
            n=1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
