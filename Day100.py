# pip install pyaudio

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning mr. lucky !")

    elif hour >= 12 and hour < 18:
        speak("good afternoon mr. lucky !")

    else:
        speak("good evening mr. Utkarsh !")

    speak("I'm siri. Please tell me how may I help you ")


# virtual assistant. Please tell me how may I help you

def takeCommand():
    # It takes microphone input from the user and returns output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vinodsingh10071981@gmail.com', 'VINOD@sin07')
    server.sendmail('vinodsingh10071981@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chat' in query:
            webbrowser.open("https://chat.openai.com/chat")

        elif 'open police modern website ' in query:
            webbrowser.open("http://pms4bnpac.com/")

        elif 'play music' in query:
            from playsound import playsound
            playsound("Mala.mp3")

        elif 'time please' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Users/UTKARSH/AppData/Local/Programs/Python/Python310/python.exe"
            os.startfile(codePath)

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "businessutkarsh22@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        else:
            print("query doesn't matched")
