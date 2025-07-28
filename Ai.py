# Importing Modules
import pyttsx3
import speech_recognition as sr
import webbrowser
from time import sleep
import pygame


# Function to speak text
def speak(text, delay = 170):

    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty('rate', delay)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Song Play
def play_song(song_name):
    query = song_name.replace(' ', '+')
    url = f"https://music.youtube.com/search?q={query}"
    webbrowser.open(url)

# Sound Play
def playsound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    sleep(1)

# Function to listen and recognize speech
def listen(word):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Say {word} Word...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, there was a problem with the speech service.")
    return ""

# Naming The AI
while True:
    speak("Say My Name ", delay = 150)
    name = listen('Name')

    if "heisenberg" in name.lower():
        AiName = name
        speak("You Got Damn Right")
        playsound("dam_right.mp3")
        sleep(2)
        break

    elif name != "":
        AiName = name
        speak(f"{name} Accepted")
        break
    else:
        speak("You Dont Get it.")

# Main Loop
while True:
    command = listen("Trigger")
    if AiName in command:
        playsound("start.mp3")
        speak("Hey , Whats My Command ?")
        next_command = listen("Command")

        if 'porn' in next_command and 'sex' in next_command and 'condom' in next_command and 'vidoes' in next_command:
            speak("You Dont Allow to Do that.")

        elif "open youtube" in next_command:
            speak("Opening YouTube")
            sleep(1)
            webbrowser.open("https://www.youtube.com/")

        elif "open insta" in next_command:
            speak("Opening Instagram")
            sleep(1)
            webbrowser.open("https://www.instagram.com/")

        elif "open youtube music" in next_command:
            speak("Opening YouTube Music")
            sleep(1)
            webbrowser.open("https://music.youtube.com/")

        elif "open netflix" in next_command:
            speak("Opening Netflix")
            sleep(1)
            webbrowser.open("https://www.netflix.com/")

        elif "play song" in next_command:
            order = next_command.split("song")
            if len(order) > 1 and order[1] != "":
                speak(f"Playing {order[1]}")
                sleep(1)
                play_song(order[1])
            else:
                speak("Please Mention the Song Name")

        elif "search" in next_command:
            search = next_command.split("search")
            if len(search) > 1 and search[1] !="":
                speak(f"Searching the Question {search[1]}")
                sleep(1)
                webbrowser.open(f"https://www.google.com/search?q={search[1]}")
            else:
                speak("Please Speak the Question")

        elif "shut down" in next_command or "shutdown" in next_command:
            speak("bye bye bye")
            break
        elif "open google" in next_command:
            speak("Opening Google")
            sleep(1)
            webbrowser.open("https://www.google.com")
        
        elif "how you doing" in next_command or "how are you" in next_command or "how r u" in next_command:
            speak("Great as Always , What About You ?")
            ask = listen("Feel")
            if "good" in ask or "great" in ask:
                speak("Glad To Hear to That.")
            else:
                speak("Sorry to Hear That.")

        elif "thank" in next_command:
            speak("My Pleasure.")

        else:
            speak("Sorry, I can't do that yet.")
        
        playsound("exit.mp3")
    else:
        print("Trigger word not detected.")
