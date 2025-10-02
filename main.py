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

def assistant_response(command):
    """Default assistant response"""
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

        # Check if user wants to open an app
        if command.lower().startswith("open "):
            app_name = command[5:].strip()  # remove "open " from command
            if open_system_app(app_name):
                response = f"Opening {app_name}..."
            else:
                response = f"Sorry, I don't know how to open '{app_name}'."
        else:
            # Normal assistant response
            response = assistant_response(command)

        print(f"Jarvis: {response}")
        speak(response)
