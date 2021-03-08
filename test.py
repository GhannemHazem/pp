import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import sys


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good morning!")
        print("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
        print("Good afternoon!")
    else:
        speak("Good evening!")
        print("Good evening!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("What can I help you with?")
        speak("What can I help you with?")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en')
            print(f"You said: {statement}\n")

        except sr.UnknownValueError:
            speak("I'm sorry, I didn't catch that")
            takeCommand()
        return statement

print("Please wait while your assistant loads...")
speak("Please wait while your assistant loads")
wishMe()
if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

if "bye" in statement or "stop" in statement:
  speak('Glad to help you! I will shut down now')
  print('Glad to help you! I will shut down now')
  time.sleep(2)
  sys.exit()

elif 'wikipedia' in statement:
  speak('Searching Wikipedia...')
  statement =statement.replace("wikipedia", "")
  results = wikipedia.summary(statement, sentences=3)
  speak("According to Wikipedia")
  print(results)
  speak(results)


elif 'open youtube' in statement:
    #webbrowser.open_new_tab("https://www.youtube.com")
    url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.get().open(url)
    speak("Youtube is open now")
    time.sleep(5)

elif 'open google' in statement:
  webbrowser.open_new_tab("https://www.google.com")
  speak("Google is open now")
  time.sleep(5)

elif 'open gmail' in statement:
  webbrowser.open_new_tab("gmail.com")
  speak("Gmail is open now")
  time.sleep(5)

elif 'time' in statement:
  strTime=datetime.datetime.now().strftime("%H:%M:%S")
  speak(f"the time is {strTime}")

elif 'news' in statement:
  news = webbrowser.open_new_tab("https://bbc.com")
  speak('Here are some headlines from the BBC news, Happy reading!')
  time.sleep(6)

elif 'search'  in statement:
  statement = statement.replace("search", "")
  webbrowser.open_new_tab(statement)
  time.sleep(5)

elif 'what is' in statement:
  speak('I can get you answers for computational and geographical problems. Please ask your question now')
  question=takeCommand()
  client = wolframalpha.Client('6QKTYA-66TGTQE6TX')
  res = client.query(question)
  answer = next(res.results).text
  speak(answer)
  print(answer)

elif 'who are you' in statement or 'what can you do' in statement:
  speak('I am your personal productivity assistant YourEdu. I am programmed to minor tasks like'
  'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia' 
  'get top headline news from BBC and you can ask me computational or geographical questions too!')

elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
  speak("I was built by Shishir Modi")
  print("I was built by Shishir Modi")

elif "log off" in statement or "sign out" in statement:
  speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
  time.sleep(10)
  subprocess.call(["shutdown", "/l"])

time.sleep(3)