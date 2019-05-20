import pyttsx3
from datetime import datetime

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour =int(datetime.datetime.now().hour)
  if hour >=0 & hour<12:
    speak("Good Morning")
  elif hour>12 and hour <18:
    speak("good afternoon")
  else:
    speak("good afternoon")

  speak("Hi I AM JARVIS ,HERE TO HELP")
  


if __name__=="__main__":
  speak("hello sir")