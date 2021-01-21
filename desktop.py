import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import sys
import pyjokes
import pyautogui
import psutil
from turtle import *
import pywhatkit
from Desktop_app import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("I didn't catch that. Please say that again")
        return "none"
    return query


def CurrentTime():
    timea = datetime.datetime.now().strftime("%H:%M:%S")
    speak(timea)


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    speak("sir, Friday at your service.")


# if hour >= 0 and hour < 11:
#     speak("good morning")
# elif hour >= 11 and hour <= 14:
#     speak("Noon.")
# elif hour > 14 and hour < 18:
#     speak("good afternoon")
# else:
#     speak("good evening")

# speak("Time is nearly about")
# CurrentTime()
# speak("What we gona do sir?")


def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\Nisha SS\\NA.png")
    speak("screenshot taken sir.")


def cpu():
    cpu = str(psutil.cpu_percent())
    speak(f"You have used {cpu} of cpu")


def net():
    value = True
    speak("What should I search sir?")
    while value:
        
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "muslim mastery" in query:
            webbrowser.open("https://www.youtube.com/watch?v=Hy-UWSimtHI&list=PL1pw3kCpenHcEZ6HfgArprRR7pUTrkc_r")

        elif "dashboard" in query:
            webbrowser.open("https://elearn.daffodilvarsity.edu.bd/my/")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open messenger" in query:
            webbrowser.open("https://www.facebook.com/messages/t/2078130032280037")

        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "news" in query:
            webbrowser.open("https://www.youtube.com/watch?v=KgiwN7ddb2U")

        elif "gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/4/#inbox")

        elif 'google search' in query:
            speak("opening google")
            query = query.replace('according to google', '')
            webbrowser.open("http://google.com/#q=" + query, new=2)

        elif 'google classroom' in query:
            speak("Opening classroom")
            webbrowser.open("https://classroom.google.com/u/4/h")

        elif 'out' in query:
            value = False
        
        elif "where" in query:
            speak("You are in net function sir.")


        
    speak("you are out of the net function sir.")



def draw():
    speak('drawing started.')
    begin_fill()
    color("red")
    left(50)
    forward(100)
    circle(40, 180)
    left(260)
    circle(40, 180)
    forward(100)
    end_fill()
    done()





def attack():
    speak("What you want to write sir?")
    text = takecommand().lower()
    for a in range(1):
        pyautogui.typewrite(text)
        pyautogui.press('enter')


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "app" in query:
            app()

        elif "net" in query:
            net()

        elif "terminate" in query:
            speak("Ok sir. I will be always there. Peace be upon you.")
            sys.exit()

        elif "close word" in query:
            speak("Closing word")
            os.system("taskkill/f /im Winword.exe")

        elif "studio" in query:
            speak("Closing visual studio code")
            os.system("taskkill/f /im Code.exe")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "thanks" in query:
            speak("welcome sir.")

        elif "what time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif "are you" in query:
            speak("For you sir, always.")

        elif "close notepad" in query:
            speak("I am closing notepad sir.")
            os.system('taskkill /f /im notepad.exe')

        elif "close reader" in query:
            speak("I am closing Adobe reader sir.")
            os.system('taskkill /f /im AcroRd32.exe')

        elif "close browser" in query:
            speak("Closing browser")
            os.system('taskkill /f /im chrome.exe')

        elif "close music" in query:
            speak("Closing music player")
            os.system('taskkill/f /im mpc-hc.exe')

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "write some" in query:
            speak("What should I write down sir?")
            note = takecommand().lower()
            remember = open("data.txt", 'w')
            remember.write(note)
            remember.close()
            speak("I have write down that sir.")

        elif "remind me" in query:
            remember = open('data.txt', 'r').read()
            speak("Yes sir you told me to remember " + remember)

        elif "take a pic" in query:
            screenshot()

        elif "status" in query:
            cpu()

        elif "hello" in query:
            speak("hi sir.")

        elif "screenshot" in query:
            os.startfile("D://Nisha SS")

        elif "open drive" in query:
            speak("Opening drive.")
            os.startfile("F://")
        
        elif "tom" in query:
            speak("Opening tom and jerry")
            os.startfile("G://TV//CN//tom and jerry")

        elif "tom and jerry" in query:
            os.startfile("G://TV//CN//tom and jerry")

        elif "tarak mehta" in query:
            os.startfile("H://Tarek metha ka ulta chasma")

        elif "write" in query:
            attack()

        elif "draw" in query:
            draw()

        elif "ok" in query:
            speak("yes.")

        elif "hey" in query:
            speak("yaa buddy.")

        elif 'why' in query:
            speak("Allah knows")

        elif 'camera' in query:
            camera()
        
        elif 'where' in query:
            speak('You are in main stream control sir.')

        elif 'auto' in query:
            auto()
        
        elif 'yes' in query:
            speak('Ohh')
        
      
        
        
