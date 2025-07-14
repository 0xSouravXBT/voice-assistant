from datetime import datetime
from utils.speech import speak

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    today = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")
