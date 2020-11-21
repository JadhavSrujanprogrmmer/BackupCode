import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import numpy as np
import cv2
import pyautogui
import calendar
import pyjokes
import math


print("Welcome to J.A.R.V.I.S. program")
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[8].id) #getting details of current voice
engine.setProperty('voice', voices[0].id)
volume  = engine.getProperty("volume")
engine.setProperty("volume", 12)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def AcessCam():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")




def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\Jarvis\\screenshot\\photo.png")


def password():
    a = input("Enter the passowrd:")
    if a == "JB12as":
        speak("Welcome back sir")
    else:
        speak("not verified")
        exit()






def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"sir said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say it again please sir ")

        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'hello jarvis' in query:
            speak("hello sir")

        elif 'jarvis describe yourself' in query:
            speak("hello \nthere my name is\n jarvis")
            speak("speed hundered online running")
            speak("memory 1 terabyte")

        elif 'thanks' in query:
            speak("No problem sir!!")

        elif 'how are you' in query:
            speak("I am fine \n   how are you sir")

        elif 'what is my name jarvis' in query:
            speak("your name is srujan jadhav")

        elif 'i am fine' in query:
            speak("ok, sir")

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google classroom' in query:
            speak("opening Google Classroom")
            webbrowser.open("https://classroom.google.com")

        elif 'search on the browser jarvis' in query:
            speak("what should i write there sir")
            search = takeCommand()
            chromepath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chorme %s'
            webbrowser.get(chromepath).open_new_tab(search+'.com')

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'i am bored now' in query:
            speak("this will make you laugh sir")
            joke = pyjokes.get_joke('en', category='neutral')
            speak(joke)

        elif 'jarvis note down' in query or 'make a note jarvis' in query:
            speak("what should i write there sir")
            note = takeCommand()
            make = open("date.txt", 'w')
            make.write(note)
            make.close()
            speak("Sucessfully written sir" + note)

        elif 'did i have anything in to do list' in query:
            make = open('date.txt', 'r').read()
            speak("yes this is the thing sir you have told me to note down:\n" + make)
            print(make)

        elif 'open command prompt' in query:
            speak("opening command prompt")
            codePath = "C:\\Users\\Srujan--Avdhut\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(codePath)

        elif 'turn on the webcam jarvis' in query:
            speak("turning on the webcam sir")
            AcessCam()    

        elif 'open code' in query:
            speak("opening code")
            codePath = "C:\\Users\\Srujan--Avdhut\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(codePath)

        elif 'change the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'mute all' in query:
            pyautogui.keyDown("alt")
            time.sleep(1)
            pyautogui.press("f4")
            pyautogui.keyUp("alt")

        elif 'jarvis on the lock system' in query:
            speak("forcing the system to locking fuction sir")
            password()

        elif 'capture this jarvis' in query or 'take a screenshot' in query:
            speak("ok, capturing screenshot sir")
            screenshot()

        elif 'open zoom' in query:
            speak("opening zoom meeting")
            codePath = "C:\\Users\\Srujan--Avdhut\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Start Zoom"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = "C:\\Users\\Srujan--Avdhut\\Favorites\\songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play my favourite song jarvis' in query:
            music_dir = "C:\\Users\\Srujan--Avdhut\\Favorites\\songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open control panel' in query:
            speak("opening control panel")
            codePath = "C:\\Users\\Srujan--Avdhut\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
            os.startfile(codePath)

        elif 'open google chrome' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
            os.startfile(codePath)

        elif 'open calendar' in query:
            print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2020))
            print("Defult first weekday:", calendar.firstweekday())
            calendar.setfirstweekday(calendar.SUNDAY)

        elif 'go to sleep jarvis' in query:
            speak("bye sir, have a good day")
            exit()
