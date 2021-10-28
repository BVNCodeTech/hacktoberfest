from _typeshed import Self
import random
import sys

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
from PyQt5 import QtWidgets, Qtcore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_Dialog


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 #print(voices[1].id)
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#To convert voices into text
def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("listening...")
       r.pause_threshold = 1
       audio = r.listen(source,timeout=1,phrase_time_limit=200)



   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')
       print(f"user said: {query}")

   except Exception as e:
       speak("Say that again please...")
       return "none"
   return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis at your service. please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvispy1@gmail.com', 'jsd@376264')
    server.sendmail('jarvispy1@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wish()
    while True:




        query = takecommand().lower()

        #logic building for tasks

        if "zoom" in query:
            zpath = "C:\\Users\\prithu narula\\AppData\\Roaming\\Zoom\\bin\\zoom.exe"
            os.startfile(zpath)

        if "notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)


        elif "open spotify" in query:
            os.system("start spotify")










        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for songs in  songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, rd))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("search wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open eco" in query:
            webbrowser.open("https://connect.eko.in")

        elif "open google" in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+918376930919", "this is testing protocol",16,33)

        elif "play song on youtube" in query:
            pywhatkit.playonyt("trndsttr")

        elif "send email to me" in query:
            try:
                speak("what should i send")
                content = takecommand().lower()
                to = "jarvispy1@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to prithu narula")

class MainThread(QThread)
   def __init__(Self):
       super(MainThread,Self).__init__()

    def run(self):
        self.Task   
   

            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email to prithu")

        elif "no thanks" in query:
            speak("ok ill just sit on the couch and chill , you can call me whenever you want to")
            sys.exit()
        speak("sir, do you have any other work")








