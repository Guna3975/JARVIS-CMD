from Speech.speak import speak
from Modules.command import open_system_app
from datetime import datetime
import os

os.system("cls")

def wish_me():
    """Greet user according to current time"""
    hour = datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    
    print(greeting)
    speak(greeting)

def personal_assistant():
    """Main loop for personal assistant"""
    wish_me()
    print("I am your assistant. You can ask me to open apps or chat with me. Type 'bye' to quit.")
    speak("I am your assistant. You can ask me to open apps or chat with me. Type 't' to quit.")


    while True:
        command = input("\nYou: ").strip()
        
        if command.lower() == "bye":
            print("Jarvis: Goodbye! Have a nice day.")
            speak("Goodbye! Have a nice day.")
            break

        # Try to open system app
        response = open_system_app(command)
        
        # If app not recognized, respond like a personal assistant
        if "don't know" in response:
            response = f"I'm here to help, but I can't open '{command}'. Maybe try another app?"

        print(f"Jarvis: {response}")
        speak(response)

if __name__ == "__main__":
    personal_assistant()
