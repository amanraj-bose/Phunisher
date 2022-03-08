import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 177)

def say(text) -> str:
    engine.say(text)
    engine.runAndWait()