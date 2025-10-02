from Speech.speak import speak
from Modules.command import open_system_app
from datetime import datetime
import os

os.system("cls || clear")  # Clear console for Windows and Unix-based systems

from datetime import datetime
from Speech.speak import speak  # your existing speak function

def wish_me():
    now = datetime.now()
    hour = now.hour
    minute = now.minute

    # Determine greeting
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    # Format current time nicely
    current_time = now.strftime("%I:%M %p") 

    print(f"{greeting}")
    speak(greeting)

    time = f"The current time is {current_time}."
    print(time)
    speak(time)


if __name__ == "__main__":
    wish_me()
    print("I am ready to assist you.")
    speak("I am ready to assist you.")

    while True:
        command = input("\nYou: ").strip()
        if command.lower() == "bye ":
            speak("Goodbye! Take care.")
            print("Jarvis: Goodbye! Take care.")
            break

        elif command == "time":
            print("Jarvis: The current time is " + datetime.now().strftime("%I:%M %p"))
            speak("The current time is " + datetime.now().strftime("%I:%M %p"))

        # Check if user wants to open an app
        elif command.lower().startswith("open "):
            app_name = command[5:].strip()  # remove "open " from command
            if open_system_app(app_name):
                Response = f"Opening {app_name}..."
            else:
                Response = f"Sorry, I don't know how to open '{app_name}'."

        else:
            print(f"I'm here to help, but I can't perform '{command}'")
            speak(f"I'm here to help, but I can't perform '{command}'")

       
