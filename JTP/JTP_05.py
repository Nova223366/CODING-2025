'''import speech_recognition as si
import pyttsx3
import pywhatkit
import wikipedia
import pyiokes
import datetimé
# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
# Set female voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices [1].id) # You can use [0] for male voice def talk(text) :
# Convert text to speech
print("Alexa:", text)
engine.say (text)
engine.runAndWait()
def take command():
try:
command m 三
with sr.Microphone() as source:
print("Listening...")
1istener.adjust_ for_ambient_noise(source)
voice = listener.1isten(source)
command = listener.cecognize_google (voice)
command = command.lower()if 'alexa' in comnand:
command = command.replace ('alexa', "").strip ()
print("You said:", command)
except sr.UnknownValueError:
print ("Sorry, I didn't understand that.")
except sr,RequestError:
print ("Network error. check your internet connection.")
teturn command
puzшыo၁ ခчว ခzFuб၀z puв ခFon s, zaen oร uอวฐฬт *
def run_alexa():
# Process the command and respond accordingly
command = take_command ()if 'play' in command:
song - command.replace ('play', "1).strip()
talk("Plavying ” + song)pywhatkit.playonyt(song)
elif 'time' in command:
time = datetime.datetime.now().strftime('용I:용M 即p')
talk ("The current time is " t time)
elif 'who igl in command or 'who the heck igl in command:
person - command.replace ('who the heck is', ").ceplace('who is', "I).strip()
info = wikipedia.summary(person, 1)
print (info)
talk (info)
elif 'datel in command:
talk ("Sorry, I have a headache today.")
elif 'are you singlel in command:
talk ("I am in a relationship with wi-Fi.")elif 'joke' in command:
talk (pyjokes.get_joke ())elif command != ":
talk ("Please say the command again.")else:
pass # No voice detected, ignore silently
# Run Alexa continuously
while True:
run alexa ()
'''



'''import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use [0] for male

def talk(text):
    """Convert text to speech"""
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for voice input and return command"""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '').strip()

            print("You said:", command)
            return command

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""

    except sr.RequestError:
        print("Network error. Check your internet connection.")
        return ""

def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is " + time)

    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk("Sorry, I have a headache today.")

    elif 'are you single' in command:
        talk("I am in a relationship with Wi-Fi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif command != "":
        talk("Please say the command again.")

# Run Alexa continuously
while True:
    run_alexa()
'''




# import speech_recognition as sr
# import pyttsx3
# import datetime

# # Initialize
# listener = sr.Recognizer()
# engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def talk(text):
#     print("Alexa:", text)
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             listener.adjust_for_ambient_noise(source)
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()

#             if 'alexa' in command:
#                 command = command.replace('alexa', '').strip()

#             print("You said:", command)
#             return command

#     except:
#         return ""

# def run_alexa():
#     command = take_command()

#     if 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk("The current time is " + time)

#     elif 'hello' in command:
#         talk("Hello! How can I help you?")

#     elif command != "":
#         talk("Please say the command again")

# # Run continuously
# while True:
#     run_alexa()
