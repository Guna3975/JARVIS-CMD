import pyttsx3

engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')


# Set female voice (choose one from the list)
engine.setProperty('voice', voices[1].id)  # usually index 1 is female on Windows

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


