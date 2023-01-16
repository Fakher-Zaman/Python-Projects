import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import pyjokes
import time
import os

def speechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source) 
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand!")

def TextToSpeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hello" in speechToText():
        while True:
            data1 = speechToText()
            if "name" in data1:
                name = "my name is fakhar zaman"
                TextToSpeech(name)
            elif "old are you" in data1:
                age = "i am twenty two years old"
                TextToSpeech(age)
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                TextToSpeech(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'google' in data1:
                webbrowser.open("https://www.google.com/")
            elif 'github' in data1:
                webbrowser.open("https://github.com/Fakher-Zaman")
            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                TextToSpeech(joke_1)
            elif 'play song' in data1:
                add = "E:\Songs\All Audio songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif 'exit' in data1:
                TextToSpeech("Thank You!")
                break
            else:
                print("Not Matching")

            time.sleep(10)
    else:
        print("Voice App Over!")