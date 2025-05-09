import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def test_gemini_flash():
    # Use Gemini 1.5 Flash model
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # Important to use full model name
    response = model.generate_content("Hello! What can you do?")
    print("Gemini Flash says:", response.text)

def main():
    # Step 1: Define Gemini agent behavior
    instructions = """
    You are JobMate, a friendly and resourceful job search assistant.
    Your job is to provide users with helpful career suggestions, job-hunting tips,
    and links to relevant job boards or remote work platforms.
    Be motivational and practical. If a user mentions a job role or domain,
    suggest at least 3 specific websites or platforms where they can apply.
    End with a reflective or guiding question to encourage action.
    """

    # Step 2: Get user input
    user_query = input("Ask JobMate a question about your career or job search:\n> ")

    prompt = f"{instructions}\n\nUser: {user_query}"

    # Step 3: Use Gemini
    model = genai.GenerativeModel('models/gemini-1.5-flash')  # Use correct model name
    response = model.generate_content(prompt)

    # Step 4: Show result
    print("\nJobMate Response:")
    print(response.text)

    # Optional: Save to README
    with open("README.md", "a", encoding="utf-8") as readme:
        readme.write(f"\n### User Prompt:\n{user_query}\n")
        readme.write(f"\n### Agent Response:\n{response.text}\n")

if __name__ == "__main__":
    test_gemini_flash()
    main()
