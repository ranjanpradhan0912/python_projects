import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing")
            data = recognizer.recognize_whisper(audio)
            # print(data)
            return data

        except sr.UnknownValueError as e:
            print("Sorry I dont get it")


def text_to_speech(txt):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'voices[0].id')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(txt)
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':

    while True:
        data1 = speech_to_text().lower()
        # print(data1)
        if "name" in data1:
            age = " hello,my name is jarvis"
            text_to_speech(age)
        elif "how are you" in data1:
            where_about = "I'm just a program, but I'm here to help you!"
            text_to_speech(where_about)
        elif "what can you do" in data1:
            task = "I can help you with various tasks like answering questions, providing information, and more!"
            text_to_speech(task)
        elif "weather" in data1:
            weather = "Please provide me with a location so I can check the weather for you."
            text_to_speech(weather)
        elif "reminder" in data1:
            reminder = "What would you like to be reminded about?"
            text_to_speech(reminder)
        elif "play music" in data1:
            music = "Sure! What genre do you want to listen to?"
            text_to_speech(music)
        elif "time" in data1:
            current_time = datetime.datetime.now().strftime("%I%M%p")
            text_to_speech(f"The current time is {current_time}.")
        elif "favorite color" in data1:
            color = "I don’t have preferences, but I think blue is nice!"
            text_to_speech(color)
        elif "quote" in data1:
            quote = "Here's a quote: 'The only way to do great work is to love what you do.' - Steve Jobs."
            text_to_speech(quote)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke = pyjokes.get_joke(language="en", category="neutral")
            text_to_speech(joke)
        # elif "picture" in data1:
        #     add="path"
        #     list_picture=os.listdir(add)
        #     os.startfile(os.path.join(add,list_picture[0]))
        elif "exit" in data1:
            text_to_speech("Meet you soon")
            break

        time.sleep(5)
