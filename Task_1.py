import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Initialize speech recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Function to speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Function to listen to user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, there is a problem with the speech recognition service.")
            return ""

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""


# Main voice assistant
def voice_assistant():

    speak("Hello! I am your voice assistant. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        # Hello command
        if "hello" in command or "hi" in command:
            speak("Hello! Nice to meet you. How can I help you?")

        # Time command
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Date command
        elif "date" in command or "today" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        # Web search command
        elif "search" in command:
            search_query = command.replace("search", "").strip()

            if search_query:
                speak("Searching for " + search_query)
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)

            else:
                speak("What would you like me to search for?")

        # Exit command
        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        # Unknown command
        else:
            speak("Sorry, I don't understand that command. Please try again.")


# Run the program
if __name__ == "__main__":
    voice_assistant()