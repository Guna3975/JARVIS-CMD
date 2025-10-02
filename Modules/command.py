from Speech.speak import speak
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

def assistant_response(command):
    return f"I'm here to help, but I can't perform '{command}'."

if __name__ == "__main__":
    wish_me()
    speak("I am ready to assist you. Type 'exit' to quit.")

    while True:
        command = input("\nYou: ").strip()
        if command.lower() == "exit":
            speak("Goodbye! Take care.")
            print("Jarvis: Goodbye! Take care.")
            break

        if command.lower().startswith("open "):
            app_name = command[5:].strip()
            response = open_system_app(app_name)
        else:
            response = assistant_response(command)

        print(f"Jarvis: {response}")
        speak(response)
