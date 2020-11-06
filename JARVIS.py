import pyttsx3
import datetime
import speech_recognition as r
import wikipedia
import webbrowser
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hi there Good Morning! Please enter you name below to proceed further")
        name = input("Enter your name:")
        namel = name.lower()
        if "swarnim" in namel:
         speak("Hi boss. Jarvis at your service. How may i help you?")
        else:
            speak(f"Hello{name}, This is Jarvis. Yes, Tony is kinda dead so I am now released to the public for use.")
            speak("Anyway, how may I help you?")
    elif hour >= 12 and hour < 18:
        speak("Hi there Good Afternoon! Please enter you name below to proceed further")
        name = input("Enter your name:")
        namel = name.lower()
        if "swarnim" in namel:
         speak("Hi boss. Jarvis at your service. How may i help you?")
        else:
            speak(f"Hello{name}, This is Jarvis. Yes, Tony is kinda dead so I am now released to the public for use.")
            speak("Anyway, how may I help you?")
    else:
        speak("Hi there Good Evening! Please enter you name below to proceed further")
        name = input("Enter your name:")
        namel = name.lower()
        if "swarnim" in namel:
         speak("Hi boss. Jarvis at your service. How may i help you?")
        else:
         speak(f"Hello{name}, This is Jarvis. Yes, Tony is kinda dead so I am now released to the public for use.")
         speak("Anyway, how may I help you?")
def takecommand():
    s = r.Recognizer()
    with r.Microphone() as source:
        print("LISTENING....")
        s.pause_threshold = 1
        audio = s.listen(source)

    try:
        print("RECOGNIZING....")
        query = s.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        return "None"
    return query


if __name__ == '__main__':

  wishME()

  while True:
     query = takecommand().lower()
     if 'wikipedia' in query:
         speak("Searching Wikipedia....")
         query = query.replace("Wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia, ")
         print(results)
         speak(results)
     elif 'what are you made of' in query:
         speak("Oh, I'm just made using text and stuff. I'm particularly made up of Python.")
     elif 'open youtube' in query:
         speak("Opening YouTube...")
         webbrowser.open("https://www.youtube.com")
         speak("You surf some stuff up on YouTube, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'how are you' in query:
         speak("I'm good, but with you, I'm really happy. Thanks for asking...")
     elif 'google' in query:
         speak("Opening Google...")
         webbrowser.open("https://www.google.com")
         speak("You surf some stuff up on Google, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")

     elif 'open whatsapp' in query:
         speak("Opening Whatsapp Web...")
         webbrowser.open("https://web.whatsapp.com/")
         speak("You check your messages in WhatsApp, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'open discord' in query:
         speak("Opening Discord...")
         webbrowser.open("https://discord.gg/")
         speak("You check your messages or play with friends in Discord, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")

     elif 'play the song tony stark like to hear' in query:
         speak("Opening Tony's favourite song, 'Back in Black' on JioSaavn...")
         webbrowser.open("https://www.jiosaavn.com/song/back-in-black/RSsbYjZifWQ")
         speak("You groove to Tony's party, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'open gmail' in query:
         speak("Opening GMail...")
         webbrowser.open("https://mail.google.com/")
         speak("You check some emails in GMail, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'jarvis bye-bye' in query:
         speak("Bye Bye have a nice Day.")
         exit()
     elif 'jarvis quit' in query:
         speak("Bye Bye have a nice Day.")
         exit()
     elif 'jarvis quit' in query:
         speak("Bye Bye have a nice Day.")
         exit()
     elif 'open meat' and "open meet" in query:
         speak("Opening Google Meet...")
         webbrowser.open("https://meet.google.com")
         speak("You attend your meeting, or if many, meetings, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif "open meet" in query:
         speak("Opening Google Meet...")
         webbrowser.open("https://meet.google.com")
         speak("You attend your meeting, or if many, meetings, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'open jio saavn' in query:
         speak("Opening Jio Saavn")
         webbrowser.open("https://www.jiosaavn.com/")
         speak("You listen some song on jio saavn till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'play music' in query:
         speak("Playing Music...")
         webbrowser.open("https://www.jiosaavn.com/")
         speak("You listen some song till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'join the coders meeting' in query:
         speak("Joining the Coders' Meeting via Google Meet...")
         print("Redirecting you to meet.google.com/mmw-picw-gsv/")
         webbrowser.open("https://meet.google.com/mmw-picw-gsv")
         speak("You code some stuff with your friends, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'join a meeting in meat' and 'join a meeting in meet' in query:
         speak("Please type the code for the meeting: ")
         code = input("Please type the code for the meeting: ")
         webbrowser.open(f"https://meet.google.com/{code}/")
         speak("You attend your meeting, or if many, meetings, till then I'm shut.")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'open the calculator' in query:
         speak("Opening Calculator")
         webbrowser.open("https://www.desmos.com/scientific")
         speak("You calculate some stuff till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'calculator' in query:
         speak("Opening Calculator")
         webbrowser.open("https://www.desmos.com/scientific")
         speak("You calculate some stuff till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'meeting in whatsapp' in query:
         speak("Scheduling Whatsapp Meeting via Google")
         webbrowser.open("https://www.messenger.com/groupcall/create?source=whatsapp&ep=4")
         speak("You have some meetings till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     elif 'open camera' in query:
         speak("Opening Camera")
         webbrowser.open("https://webcamera.io/")
         speak("You take some pictures till then I am shut")
         speak("Press enter key to activate me")
         input("Press Enter key to activate me:")
         speak("Ya sorry I went to sleep. Thanks for waking me up...")
     else:
        if "none" in query:
             speak("Say that again please")

        else:
          speak("Searching google")
          webbrowser.open(f"https://www.google.com/search?q={query}")
          speak("According to google.. here are the results.")
          speak("You browse through the results till then I am shut.")
          speak("Press enter key to activate me")
          input("Press Enter key to activate me:")
          speak("Ya sorry I went to sleep. Thanks for waking me up...")
a = input()
