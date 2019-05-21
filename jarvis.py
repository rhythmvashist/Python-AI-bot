import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

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
  return query

def sendMsg(to,msg):
  #you had to enable less secure apps for this method to work completely
  server =smtplib.SMPT('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login('sender email','password')
  server.sendmail('email sender',to,msg)
  server.close()

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
    
    elif 'open google' in quer:
      webbrowser.open("google.com")

    elif 'open Stackoverflow' in quer:
      webbrowser.open("stackoverflow.com")
    
    elif 'music' in quer:
      webbrowser.open("spotify.com")
    
    elif 'spotify' in quer:
      webbrowser.open("spotify.com")

    elif 'time' in quer:
      timerans=datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"sir, the time is {timerans}")
    
    elif 'open code' in quer:
      #path for the program to be opened i used it for vscode
      cpath = "C:\Users\vashi\Microsoft VS Code\Code.exe"
      os.startfile(cpath)

    elif 'message to buddies' in quer:
      try:
        speak("what should i say")
        msg=takeCommand()
        receiver='vashistrhythm1@gmail.com'
        sendMsg(receiver,msg)
        speak("email has been sent")
      except Exception as e:
        print(e)
        speak("sorry sir i wasn't able to send email")
      


