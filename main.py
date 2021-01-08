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
        with sr.Microphone() as sourse:
            print('listening...')
            vioce = listener.listen(sourse)
            command = listener.recognize_google(vioce)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # talk(command)
                print(command)
    except:
        pass
    return command

def run_command():
    command = take_command()   
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        #print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi') 
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'stop processing' in command:
        talk('bye')
        quit()
    else:
        talk('say the command again.')

while True:
    run_command()

