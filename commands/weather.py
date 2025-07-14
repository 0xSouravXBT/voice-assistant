import requests
from utils.speech import speak

API_KEY = "e86dba3f0c8dcd3297b205a45b8b13e1"
CITY = "Kolkata"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        temp = res['main']['temp']
        desc = res['weather'][0]['description']
        speak(f"The temperature in {CITY} is {temp}°C with {desc}.")
    except:
        speak("Unable to get weather information.")
