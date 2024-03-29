# libraries used : text to speech,datetime,speechRecognition,wikipedia,webbrowser,os,random,smtplib,sys,pywhatkit,getpass,cv2
import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import pywhatkit
import getpass
import cv2

# setting up engines and voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

# speak function will speak the audio passed


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish command wishes the user


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis Sir. Please tell me how may I help you.")

# take command function to take microphone input from the user and return string output


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1  # sets a pause of 1 second
        audio = r.listen(source)
    try:
        print("Recognising.....")
        # use google engine to recognise voice from microphone
        # query = r.recognize_google(audio, language=code) => provide language code from here -: https://cloud.google.com/speech-to-text/docs/languages
        # I have used English India ,you can choose as per your choice
        query = r.recognize_google(audio, language="en-IN").lower()
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


wishMe()
while True:
    query = take_command()

    if "wikipedia" in query:
        speak("Say what to search...")
        query = take_command()
        speak("Searching wikipedia...")
        results = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        print("Opening youtube....")
        speak("Opening youtube....")
        # webbrowser module will open the browser and particular site
        webbrowser.open("youtube.com")

    elif "open google" in query:
        print("Opening google....")
        speak("Opening google....")
        webbrowser.open("google.com")

    elif "open stackoverflow" in query:
        print("Opening stackoverflow....")
        speak("Opening stackoverflow....")
        webbrowser.open("stackoverflow.com")


    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif "open vs code" in query:
        # provide path of the application to os module to open any application from your desktop
        path = "C:\\Users\\91951\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)


    elif "send whatsapp message" in query:
        try:
            to = ""
            while True:
                speak("To whom you wish to send message ?")
                to = take_command()  # provide recievers mail
                if to in whatsAppContacts:
                    to = whatsAppContacts[to]
                    break
                else:
                    print("Sorry,contact doesn't exist!")
                    speak("Sorry,contact doesn't exist!")
            speak("What should I message ?")
            message = take_command()
            # pywhatkit.sendwhatmsg_instantly("phone number on which to send number with country code", message)
            pywhatkit.sendwhatmsg_instantly(to, message)
            speak("Successfully Sent!")
        except Exception as e:
            speak("Sorry , Failed to send message!")

    elif "search google" in query:
        try:
            speak("What should I search ?")
            content = take_command()
            pywhatkit.search(content)
        except Exception as e:
            speak("Sorry , Failed to search!")

    elif "search topic" in query:
        try:
            speak("What should I search ?")
            content = take_command()
            # pywhatkit.info(content, lines=n) : provide n as number of lines you want to fetch
            pywhatkit.info(content, lines=2)
        except Exception as e:
            speak("Sorry , Failed to search!")

    elif "open team" in query:
        path = "C:\\Users\\91951\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
        try:
            os.startfile(path)
        except Exception as e:
            print(e)

    elif "stop" in query:
        speak("Ok sir, have a good day!")
        sys.exit(0)