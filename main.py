from Speech.speak import speak
from datetime import datetime

def wish_me():
    """Greet user according to current time"""
    hour = datetime.now().hour

    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    
    speak(greeting)
    print(greeting)

if __name__ == "__main__":
    wish_me()
