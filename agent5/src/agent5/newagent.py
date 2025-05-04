from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

#gemini-2.0-flash
load_dotenv()
# set the gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True) #study later what is tracing
model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = external_client
)


def agentn_func():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant",model=model)

    result = Runner.run_sync(agent, "top ten best army of the world?")
    print(result.final_output)