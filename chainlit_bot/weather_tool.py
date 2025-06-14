import requests
from my_secrets import Secrets

def get_weather(city: str) -> str:
    url = f"{Secrets.WEATHER_API_URL}/current.json"
    params = {
        "key": Secrets.WEATHER_API_KEY,
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
        return f"🌧️ Sorry, I couldn't fetch weather data: {str(e)}"
