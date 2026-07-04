import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You:", command)
        return command

    except:

        return ""


def run_assistant():

    command = listen()

    if "hello" in command:

        speak("Hello! How can I help you?")

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "search" in command:

        query = command.replace("search", "")
        speak("Searching Google")
        pywhatkit.search(query)

    elif "wikipedia" in command:

        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "youtube" in command:

        query = command.replace("youtube", "")
        speak("Playing on YouTube")
        pywhatkit.playonyt(query)

    elif "google" in command:

        webbrowser.open("https://www.google.com")

    elif "bye" in command:

        speak("Goodbye!")
        return False

    else:

        speak("Sorry, I didn't understand.")

    return True


speak("JARVIS YOUR AI Assistant Started")

running = True

while running:
    running = run_assistant()