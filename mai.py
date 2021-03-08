import speech_recognition as sr
import webbrowser
import pyttsx3


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("What can I help you with?")
        speak("What can I help you with?")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
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

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue    
if 'open youtube' in statement:
    webbrowser.open_new_tab("https://www.youtube.com")
    
    speak("Youtube is open now")
    time.sleep(5)        