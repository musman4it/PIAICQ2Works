# helloagent.py

import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Setup external client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

# Setup model and agent
model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=external_client
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=model)

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")

user_question = st.text_input("Ask your question:")

if st.button("Submit") and user_question.strip():
    with st.spinner("Thinking..."):
        result = Runner.run_sync(agent, user_question)
        st.success(result.final_output)
