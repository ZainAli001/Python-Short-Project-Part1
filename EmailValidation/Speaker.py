import pyttsx3
import speech_recognition as sr

# sapi5 is used in windows to detect or recived voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# two voices male and female by default 
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

r= sr.Recognizer()

r.pause_threshold= 1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def shortLength():
    speak("lenght is shorter")
    
def firstLetter():
    speak("Your Email first letter must contain a alphabet")
    
def checkAtTheRat():
    speak("Your Email Must contain @ at once only")
    
def dotCheck():
    speak("Your Email Must contain dot  ")


def randomError():
    speak("Check Your Email Again ")

def capitalLetter():
    speak("Your Email Must Contain Small Letters")

def notSpace():
    speak("Your Email Not Contain a Space")
    
    

    
def rightEmail():
    speak("You Entered right Email ! ")

