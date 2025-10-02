from Speech.speak import speak
from Modules.command import open_system_app
from datetime import datetime
import os

os.system("cls")

def wish_me():
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
    
    # Instead of voice, take text input for now
    command = input("Which app do you want to open? ")
    
    response = open_system_app(command)
    print(response)
    speak(response)
