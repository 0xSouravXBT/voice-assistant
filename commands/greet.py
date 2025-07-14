from utils.speech import speak
from datetime import datetime

def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
