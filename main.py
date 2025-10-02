from Speech.speak import speak
from Modules.command import open_system_app
from datetime import datetime
import os
import platform

# Clear console based on OS
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def wish_me():
    now = datetime.now()
    hour = now.hour

    # Determine greeting
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    # Format current time
    current_time = now.strftime("%I:%M %p") 

    print(f"{greeting}")
    speak(greeting)

    time_msg = f"The current time is {current_time}."
    print(time_msg)
    speak(time_msg)


if __name__ == "__main__":
    wish_me()
    print("I am ready to assist you.")
    speak("I am ready to assist you.")

    while True:
        command = input("\nYou: ").strip()

        # Exit condition
        if command.lower() in ["bye", "exit", "quit"]:
            print("Jarvis: Goodbye! Take care.")
            speak("Goodbye! Take care.")
            break

        # Time check
        elif command.lower() == "time":
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Jarvis: The current time is {current_time}")
            speak(f"The current time is {current_time}")

        # Open app check
        elif command.lower().startswith("open "):
            app_name = command[5:].strip()  # remove "open " from command
            success, response = open_system_app(app_name)
            print(f"Jarvis: {response}")
            speak(response)


        # Default response
        else:
            response = "I'm here to help, but I can't perform"
            print(f"Jarvis: {response}")
            speak(response)
