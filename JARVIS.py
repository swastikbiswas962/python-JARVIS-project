import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def acceptCommand():
    r =sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except:
        print("Unable to recognise for errors...")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def changeAudio(audio):
    if 'male' in audio:
        engine.setProperty('voice', voices[0].id)
    elif 'female' in audio:
        engine.setProperty('voice', voices[1].id)
    else:
        print("Unable to change audio...")

if __name__ == "__main__":
    print("Patching system...")
    speak("Patching system.")
    print("")
    print("")
    print("J.A.R.V.I.S has started...")
    speak("JARVIS has started.")
    print()
    print()
    print("Input your OS Username to proceed further...")
    speak("Input your O S username to proceed further.")
    user = input(">> ")
    print()
    print(f"Welcome {user}, this is Just A Rather Very Intelligent System, or J.A.R.V.I.S in short.")
    speak(f"Welcome {user}, this is Just A Rather Very Intelligent System, or JARVIS in short.")
    print("You can now do whatever you want to, and when you need my help, just call me up.")
    speak("You can now do whatever you want to, and when you need my help, just call me up.")
    print()
    while True:
        query = acceptCommand().lower()
        if 'jarvis' in query:
            if 'time now' in query or 'the time' in query:
                time24 = datetime.datetime.now().strftime("%H:%M")
                time12 = datetime.datetime.now().strftime("%M")
                hour = int(datetime.datetime.now().hour)
                suffix = 'AM'
                if hour > 12:
                    hour = hour - 12
                    suffix = 'PM'
                print(f"The time now is: {time24}, or {hour}:{time12}{suffix}.")
                speak(f"The time now is {time24}, or {hour}:{time12}{suffix}.")
            elif 'wikipedia' in query:
                query = query.replace("wikipedia","").replace("jarvis","").replace("according to","")
                summary = wikipedia.summary(query, sentences=2)
                print("According to Wikipedia, ")
                speak("According to Wikipedia, ")
                print(summary)
                speak(summary)
                page = wikipedia.page(query)
                print(f"To learn more, visit {page.url}")
                speak(f"To learn more, visit the link mentioned.")
            elif 'open google' in query:
                if 'drive' in query:
                    print("Opening Google Drive...")
                    speak("Opening Google Drive.")
                    webbrowser.open_new_tab("https://drive.google.com/")
                elif 'docs' in query or 'document' in query or 'documents' in query:
                    print("Opening Google Documents...")
                    speak("Opening Google Documents.")
                    webbrowser.open_new_tab("https://docs.google.com/document/")
                elif 'sheet' in query or 'sheets' in query or 'shit' in query or 'shits' in query or 'spreadsheet' in query or 'spreadsheets' in query or 'excel' in query:
                    print("Opening Google Sheets...")
                    speak("Opening Google Sheets.")
                    webbrowser.open_new_tab("https://docs.google.com/spreadsheets/")
                elif 'slide' in query or 'slides' in query or 'presentation' in query or 'presentations' in query:
                    print("Opening Google Slides...")
                    speak("Opening Google Slides.")
                    webbrowser.open_new_tab("https://docs.google.com/presentations/")
                elif 'drive' in query or 'drives' in query:
                    if 'my' in query:
                        print("Opening My Drive in Google Drive...")
                        speak("Opening My Drive in Google Drive.")
                        webbrowser.open_new_tab("https://drive.google.com/drive/u/0/my-drive")
                    elif 'share' in query or 'shared' in query:
                        print("Opening Shared with Me in Google Drive...")
                        speak("Opening Shared with me in Google Drive.")
                        webbrowser.open_new_tab("https://drive.google.com/drive/u/0/shared-with-me")
                    elif 'recent' in query:
                        print("Opening Recent in Google Drive...")
                        speak("Opening Recent in Google Drive.")
                        webbrowser.open_new_tab("https://drive.google.com/drive/u/0/recent")
                    elif 'star' in query or 'starred' in query or 'stars' in query:
                        print("Opening Starred in Google Drive...")
                        speak("Opening Starred in Google Drive.")
                        webbrowser.open_new_tab("https://drive.google.com/drive/u/0/starred")
                    elif 'bin' in query or 'trash' in query or 'dustbin' in query:
                        print("Opening Bin in Google Drive...")
                        speak("Opening Bin in Google Drive.")
                        webbrowser.open_new_tab("https://drive.google.com/drive/u/0/trash")
                    print("Opening Google Drive...")
                    speak("Opening Google Drive.")
                    webbrowser.open_new_tab("https://drive.google.com/")
                elif 'duo' in query:
                    print("Opening Google Duo...")
                    speak("Opening Google Duo.")
                    webbrowser.open_new_tab("https://duo.google.com/")
                elif 'account' in query or 'accounts' in query:
                    print("Opening Google Accounts...")
                    speak("Opening Google Accounts.")
                    webbrowser.open_new_tab("https://myaccount.google.com/")
                elif 'mail' in query:
                    if 'inbox' in query:
                        print("Opening your Inbox in Google Mail...")
                        speak("Opening your Inbox in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                    elif 'star' in query or 'starred' in query or 'stars' in query:
                        print("Opening your Starred messages in Google Mail...")
                        speak("Opening your Starred messages in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#starred")
                    elif 'draft' in query or 'drafts' in query:
                        print("Opening your Drafts in Google Mail...")
                        speak("Opening your Drafts in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#drafts")
                    elif 'snooze' in query or 'snoozed' in query:
                        print("Opening your Snoozed messages in Google Mail...")
                        speak("Opening your Snoozed messages in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#snoozed")
                    elif 'sent' in query or 'send' in query:
                        print("Opening your Sent messages in Google Mail...")
                        speak("Opening your Sent messages in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")
                    elif 'important' in query or 'importance' in query:
                        print("Opening your Important messages in Google Mail...")
                        speak("Opening your Important messages in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#imp")
                    elif 'chats' in query or 'chat' in query:
                        print("Opening your Chats in Google Mail...")
                        speak("Opening your Chats in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#chats")
                    elif 'all' in query:
                        print("Opening All Mails in Google Mail...")
                        speak("Opening All Mails in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#all")
                    elif 'bin' in query or 'trash' in query or 'dustbin' in query:
                        print("Opening your Bin in Google Mail...")
                        speak("Opening your Bin in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#trash")
                    else:
                        print("Opening your Inbox in Google Mail...")
                        speak("Opening your Inbox in Google Mail.")
                        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                else:
                    print("Opening Google.com...")
                    speak("Opening Google dot com.")
                    webbrowser.open_new_tab("https://www.google.com/")
            elif 'open youtube' in query:
                if 'pewdipy' in query or 'pewdiepie' in query:
                    print("Opening PewDiePie's channel on YouTube...")
                    speak("Opening PewDiePie's channel on YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/user/PewDiePie")
                elif 'mister beast' in query:
                    print("Opening Mr. Beast's channel on YouTube...")
                    speak("Opening Mister Beast's channel on YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/user/mrbeast6000")
                elif 'dan t d m' in query or 'dan' in query or 'dantdm' in query:
                    print("Opening DanTDM's channel on YouTube...")
                    speak("Opening DanTDM's channel on YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/user/TheDiamondMinecart")
                elif 'dude perfect' in query:
                    print("Opening Dude Perfect's channel on YouTube...")
                    speak("Opening Dude Perfect's channel on YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/user/corycotton")
                elif 'alan walker' in query:
                    print("Opening Alan Walker's channel on YouTube...")
                    speak("Opening Alan Walker's channel on YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/user/DjWalkzz")
                else:
                    print("Opening YouTube...")
                    speak("Opening YouTube.")
                    webbrowser.open_new_tab("https://www.youtube.com/")
            elif 'open stackoverflow' in query or 'stack overflow' in query:
                print("Opening Stack Overflow...")
                speak("Opening Stack Overflow.")
                webbrowser.open_new_tab("https://www.stackoverflow.com/")
            elif 'open discord' in query:
                speak("Opening Discord...")
                print("Opening Discord.")
                webbrowser.open_new_tab("https://www.discord.gg/")
            elif 'open khan academy' in query:
                print("Opening Khan Academy...")
                speak("Opening Khan Academy.")
                webbrowser.open_new_tab("https://www.khanacademy.org/")
            elif 'open twitter' in query:
                print("Opening Twitter...")
                speak("Opening Twitter.")
                webbrowser.open_new_tab("https://www.twitter.com/home/")
            elif 'open facebook' in query:
                print("Opening Facebook...")
                speak("Opening Facebook.")
                webbrowser.open_new_tab("https://www.facebook.com/")
            elif 'open whats app' in query or 'open whatsup' in query or 'open whats up' in query:
                print("Opening WhatsApp Web...")
                speak("Opening WhatsApp Web.")
                webbrowser.open_new_tab("https://web.whatsapp.com/")
            elif 'open tumbler' in query or 'open tumblur' in query or 'open tumblr' in query:
                print("Opening Tumblr...")
                speak("Opening Tumblr.")
                webbrowser.open_new_tab("https://www.tumblr.com/")
            elif 'open wix' in query or 'open wicks' in query:
                print("Opening Wix.com...")
                speak("Opening Wix dot com.")
                webbrowser.open_new_tab("https://www.wix.com/")
            elif 'open wordpress' in query or 'open word press' in query:
                print("Opening Wordpress...")
                speak("Opening Wordpress.")
                webbrowser.open_new_tab("https://www.wordpress.com/")
            elif 'open github' in query:
                print("Opening GitHub...")
                speak("Opening GitHub.")
                webbrowser.open_new_tab("https://www.github.com/")
            elif 'open amazon' in query:
                print("Opening Amazon...")
                speak("Opening Amazon.")
                webbrowser.open_new_tab("https://ww.amazon.com/")
            elif 'open flipkart' in query or 'open flipcart' in query:
                print("Opening Flipkart...")
                speak("Opening Flipkart.")
                webbrowser.open_new_tab("https://www.flipkart.com/")
            elif 'open twitch' in query:
                print("Opening Twitch...")
                speak("Opening Twitch.")
                webbrowser.open_new_tab("https://www.twitch.tv/")
            elif 'open fortnite' in query or 'open fort night' in query or 'play fortnite' in query or 'play fort night' in query:
                print("Opening Epic Games' Fortnite...")
                speak("Opening Epic Games' Fortnite.")
                try:
                    os.startfile("C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteLauncher.exe")
                except:
                    print("Error: Could not load Fortnite on your desktop...")
                    print("Would you like to download Fortnite for desktop from the Epic Games Laucher?")
                    speak("Error: Could not load Fortnite on your desktop. Would you like to download Fortnite for desktop from the Epic Games Laucher?")
                    query = acceptCommand().lower()
                    
                    if 'yes' in query or 'download' in query or 'install' in query:
                        try:
                            print("Redirecting you to the Epic Games Launcher...")
                            speak("Redirecting you to the Epic Games Launcher.")
                            os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
                        except:
                            print("Error: Could not load Epic Games Launcher on your desktop...")
                            print("Would you like to download Epic Games Launcher for desktop?")
                            speak("Error: Could not load Epic Games Launcher on your desktop. Would you like to download Epic Games Launcher for desktop?")
                            query = acceptCommand().lower()
                            
                            if 'yes' in query or 'download' in query or 'install' in query:
                                print("Redirecting you to Epic Game's download page...")
                                speak("Redirecting you to Epic Game's download page.")
                                webbrowser.open_new_tab("https://www.epicgames.com/store/en-US/download")
                            else:
                               print("Request cancelled...")
                               speak("Request cancelled.")
            elif 'open spotify' in query:
                print("Opening Spotify...")
                speak("Opening Spotifi.")
                try:
                    os.startfile(f"C:\\Users\\{user}\\AppData\\Roaming\\Spotify\\Spotify.exe")
                except:
                    print("Error: Could not load Spotify on your desktop...")
                    print("Would you like to download Spotify for desktop or rather use the web player?")
                    speak("Error: Could not load Spotifi on your desktop. Would you like to download Spotifi for desktop or rather use the web player?")
                    query = acceptCommand().lower()
                    
                    if 'download' in query or 'install' in query:
                        print("Redirecting you to Spotify's download page...")
                        speak("Redirecting you to Spotifi's download page.")
                        webbrowser.open_new_tab("https://www.spotify.com/in/download/")
                    elif 'web' in query:
                        print("Redirecting you to Spotify's web player...")
                        speak("Redirecting you to Spotifi's web player.")
                        webbrowser.open_new_tab("https://open.spotify.com/")
                    else:
                        print("Request cancelled...")
                        speak("Request cancelled.")
            elif 'open vs code' in query:
                print("Opening VS Code...")
                speak("Opening V S Code.")
                try:
                    os.startfile(f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                except:
                    print("Error: Could not load VS Code on your desktop...")
                    print("Would you like to download VS Code for desktop?")
                    speak("Error: Could not load VS Code on your desktop. Would you like to download VS Code for desktop?")
                    query = acceptCommand().lower()
                    
                    if 'yes' in query or 'download' in query or 'install' in query:
                        print("Redirecting you to VS Code's download page...")
                        speak("Redirecting you to V S Code's download page.")
                        webbrowser.open_new_tab("https://code.visualstudio.com/download/")
                    else:
                        print("Request cancelled...")
                        speak("Request cancelled.")
            elif 'open epic games' in query:
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher.")
                try:
                    os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
                except:
                    print("Error: Could not load Epic Games Launcher on your desktop...")
                    print("Would you like to download Epic Games Launcher for desktop?")
                    speak("Error: Could not load Epic Games Launcher on your desktop. Would you like to download Epic Games Launcher for desktop?")
                    query = acceptCommand().lower()
                    
                    if 'yes' in query or 'download' in query or 'install' in query:
                        print("Redirecting you to Epic Game's download page...")
                        speak("Redirecting you to Epic Game's download page.")
                        webbrowser.open_new_tab("https://www.epicgames.com/store/en-US/download")
                    else:
                        print("Request cancelled...")
                        speak("Request cancelled.")
            elif 'open chrome' in query:
                print("Opening Chrome...")
                speak("Opening Chrome.")
                try:
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                except:
                    print("Error: Could not load Chrome on your desktop...")
                    print("Would you like to download Chrome for desktop?")
                    speak("Error: Could not load Chrome on your desktop. Would you like to download Chrome for desktop?")
                    query = acceptCommand().lower()
                    
                    if 'yes' in query or 'download' in query or 'install' in query:
                        print("Redirecting you to Chrome's download page...")
                        speak("Redirecting you to Chrome's download page.")
                        webbrowser.open_new_tab("https://www.google.com/intl/en_in/chrome/")
                    else:
                        print("Request cancelled...")
                        speak("Request cancelled.")
            elif 'open' in query and 'explorer' in query:
                print("Opening Windows Explorer...")
                speak("Opening Windows Explorer.")
                try:
                    os.startfile("C:\\Windows\\explorer.exe")
                except:
                    print("Error: Could not load Windows Explorer...")
                    speak("Error: Could not load Windows Explorer.")
            elif 'open' in query and 'edge' in query:
                print("Opening Microsoft Edge...")
                speak("Opening Microsoft Edge.")
                try:
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                except:
                    print("Error: Could not load Edge in your desktop...")
                    print("Would you like to download Edge for desktop?")
                    speak("Error: Could not load Edge in your desktop. Would you like to download Edge for desktop?")
                    query = acceptCommand().lower()
                    
                    if 'yes' in query or 'download' in query or 'install' in query:
                        print("Redirecting you to Microsoft Edge's download page...")
                        speak("Redirecting you to Microsoft Edge's download page.")
                        webbrowser.open_new_tab("https://www.microsoft.com/en-us/edge")
                    else:
                        print("Request cancelled...")
                        speak("Request cancelled.")
            elif 'covid' in query or 'kovid' in query or 'coronavirus' in query or 'corona virus' in query:
                myurl = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
                urlClient = url(myurl)
                html = urlClient.read()
                urlClient.close()
                page_soup = soup(html, "html.parser")

                containers = page_soup.find_all("table", {"id":"thetable"})
                container = containers[0]
                world_total = container.findAll("th",{"style":"text-align:right; font-weight: normal; padding: 0 2px;"})
                world_cases = world_total[0].text.replace(",","").replace("\n","")
                world_deaths = world_total[1].text.replace(",","").replace("\n","")
                world_recovered = world_total[2].text.replace(",","").replace("\n","")
                print("Here is the current situation of CoViD-19:")
                speak("Here is the current situation of CoViD-19")
                print()
                print("World:")
                print(f"    {world_cases} total recorded cases.")
                print(f"    {world_deaths} total recorded deaths.")
                print(f"    {world_recovered} total recorded recoveries.")
                speak(f"In the World: {world_cases} total recorded cases, {world_deaths} total recorded deaths, {world_recovered} total recorded recoveries.")
            elif 'who made you' in query:
                print("I was created by a very intelligent, but yet lonely person, Swastik. He's a school student who aspires to be more, and I seriously appreciate that. :)")
                speak("I was created by a very intelligent, but yet lonely person, Swastik. He's a school student who aspires to be more, and I seriously appreciate that.")
            else:
                query = query.replace("jarvis","").split(" ")
                len = len(query)
                parameter = "q="
                count = 0
                for x in query:
                    parameter = parameter + x
                    count = count + 1
                    finished = (count == len)
                    if finished:
                        break
                    else:
                        parameter = parameter + "+"
                try:
                    webbrowser.open_new_tab(f"https://www.google.com/search?{parameter}")
                    print("Here are some matching results according to Google.")
                    speak("Here are some matching results according to Google.")
                except:
                    print("Oops! Looks like you don't have internet connection. So I am unable to do the task.")
                    speak("Oops! Looks like you don't have internet connection. So I am unable to do the task.")
            print("")
