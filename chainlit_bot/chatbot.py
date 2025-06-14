import chainlit as cl
import google.generativeai as genai
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get env vars
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_MODEL = os.getenv("GEMINI_API_MODEL")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")

# Gemini setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_API_MODEL)

# Weather tool
def get_weather(city: str) -> str:
    url = f"{WEATHER_API_URL}/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The weather in {location} is {condition} with {temp_c}°C."
    except Exception as e:
        return f"🌧️ Failed to fetch weather data: {str(e)}"

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat", model.start_chat())
    await cl.Message("👋 Hi! I'm Gemini 2.0 Flash. Ask me anything or type 'weather in [city]'").send()

@cl.on_message
async def on_message(message: cl.Message):
    content = message.content.lower().strip()

    if content.startswith("weather in"):
        city = content.replace("weather in", "").strip()
        weather = get_weather(city)
        await cl.Message(weather).send()
    else:
        chat = cl.user_session.get("chat")
        response = chat.send_message(message.content)
        await cl.Message(response.text).send()
