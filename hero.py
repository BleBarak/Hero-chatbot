import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Hero' in command:
                command = command.replace('Hero', '')
                print(command)

    except:
        pass
    return command


def run_hero():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song + 'on youtube')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%p')
        talk('the current time is' + time)
        print(time)
    elif 'what can you do for me' in command:
        talk('there is alot of things i can do, i can say joke'
             'play music from youtube and many more')
    elif 'who am i' in command:
        talk('you are Ble Barak my creator as well as developer')
    elif 'who are you' in command:
        talk('i am hero a chatbot as well as your personal assistant')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a headache')
    elif 'single' in command:
        talk('I am in a relationship with wifi')
    elif 'chat' in command:
        talk('sure, i enjoy chatting, what do you want us to talk about?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please, may you repeat that again')


# search_term = ""

while True:
    run_hero()
