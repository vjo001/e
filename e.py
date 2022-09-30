from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("690x420")
root.configure(background = "purple")

label = Label(root, text = "WELCOME TO YOUR PERSONAL DESKTOP ASSISTANT", bg = "Lightblue", font = ("Forte", 13, "italic"))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognizer = sr.Recognizer()
    speak("How May I Help You?")
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognizer.recognize_google(audio, language = 'en-in')
        except sr.UnknownValueError:
            print('Please Repeat. I Could Not Understand That.')
            speak('Please Repeat. I Could Not Understand That.')
            r_audio()
        respond(voice_data)