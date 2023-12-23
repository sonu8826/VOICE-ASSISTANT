import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
from bs4 import BeautifulSoup
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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
            if 'zira' in command:
                command = command.replace('zira', ' ')
                print(command)
    except:
        pass
    return command


def search_on_google(command):
    pywhatkit.search(command)


def sendwhatmsg_instantly(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}",message)

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')

        talk('Current time is ' + time)
    elif "send whatsapp message" in command:
        talk(
            'On what number should I send the message sir? Please enter in the console: ')
        number = input("Enter the number: ")
        talk("What is the message sir?")
        message = take_command().lower()
        sendwhatmsg_instantly(number, message)
        talk("I've sent the message sir.")



    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search on google' in command:
        talk('What do you want to search on Google, sir?')
        command = take_command().lower()
        search_on_google(command)
    elif 'who is lavish' in command:
        talk('lavish is your friend')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'hello zira' in command:
        talk('hello sir i am zira your personal assistant i hope you are doing good what i can do for you')
    elif 'how are you'  in command:
        talk('i am fine sir how are you..')
    elif 'who is ujjwal' in command:
        talk('ujjwal is your friend...')
    elif 'what is the temperature' in command:
        search = 'temperature in gurugram'
        per = command.replace('what is the temperature', '')
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        talk(f"current{search}is{temp}")
    elif 'who is shweta'  in command:
        talk('shweta is your sister')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')




while True:
    run_alexa()