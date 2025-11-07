import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        talk("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        talk("Network error.")
        return ""

def run_jarvis():
    talk("Hello, I am Jarvis. How can I help you?")
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")

        elif 'search' in command:
            query = command.replace('search', '')
            pywhatkit.search(query)
            talk(f"Searching {query} on the web")

        elif 'youtube' in command:
            webbrowser.open("https://youtube.com")
            talk("Opening YouTube")

        elif 'google' in command:
            webbrowser.open("https://google.com")
            talk("Opening Google")

        elif 'facebook' in command:
            webbrowser.open("https://www.facebook.com") 
            talk("opening facebook")   

        elif 'play music' in command:
            music_path = 'C:\\Music\\sample.mp3'  # Change this path to an actual file
            if os.path.exists(music_path):
                os.startfile(music_path)
                talk("Playing music")
            else:
                talk("Music file not found")

        elif 'stop' in command or 'exit' in command or 'quit' in command:
            talk("Goodbye!")
            break

        elif command != "":
            talk("I didn’t understand that. Please try again.")

if __name__ == "__main__":
    run_jarvis()
