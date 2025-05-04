from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from rich import print
import aysncio

load_dotenv()
# Load environment variables from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")
#print(gemini_api_key)    _API_KEY",

external_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_provider)
set_default_openai_api("Chat_completion")
set_tracing_disabled(True)

def run_global():
    agent = Agent (
        name = " assistant",
        instructions = "You are a helpful assistant",
        model = OpenAIChatCompletionsModel(
            model = "gemini-2.0-flash",
            openai_client = external_provider
        ) 
        
    )
    result = Runner.run_sync(
        agent,
        "What is AI , Please Respond ?"
        "how many countries are in the world ?"
        "What is the capital of Pakistan ?")
    print (result.final_output)


