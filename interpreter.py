import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 155)
en.setProperty('volume', 0.5)
voices = en.getProperty('voices')
en.setProperty('voice', voices[2].id)


def speak(msg):
    en.say(msg)
    en.runAndWait()

