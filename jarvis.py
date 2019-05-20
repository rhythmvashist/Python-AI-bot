import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
  hour =int(datetime.datetime.now().hour)
  if hour >=0 and hour<12:
    speak("Good Morning")
  elif hour>12 and hour <18:
    speak("good afternoon")
  else:
    speak("good afternoon")

  speak("Hi I AM JARVIS ,HERE TO HELP")
  
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening ...")
    r.pause_threshold = 1
    audio=r.listen(source)

  try:
    print("Recognising...")
    query = r.recognize_google(audio,language='en-ca')
    print(f"user said:{query}\n")

  except Exception as e:
    print(e)
    speak("Sorry sir,I couldn't recognise what you said..")
    print("Say that again Please...")
    return "None"

  return query;


if __name__=="__main__":
  wishMe()
  while True:
    quer=takeCommand().lower()

    if 'wikipedia' in quer:
      speak("searching wikipedia...")
      quer =quer.replace("wikipedia","")
      results=wikipedia.summary(quer,sentences=2)
      speak("according to wkipedia")
      speak(results)
    
    elif 'open youtube' in quer:
      webbrowser.open("youtube.com")
    
    elif 'open open' in quer:
      webbrowser.open("open.com")

    elif 'open Stackoverflow' in quer:
      webbrowser.open("stackoverflow.com")
    
    elif 'music' in quer:
      webbrowser.open("spotify.com")
    
    elif 'spotify' in quer:
      webbrowser.open("spotify.com")

    




  #speak("hello sir")