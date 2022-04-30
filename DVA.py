# To run this project installextra  modules
# installation modules
# pip install pyttsx3
# pip install speechRecognition
#pip install wikipedia


import datetime
import os
import pyttsx3
import speech_recognition as sr
import wikipedia 
import webbrowser
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        print("Good Morning")
        speak("Good Morning")
        
    elif hour<17:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("Hello Sir ! I am Your Desktop Voice Assistant,  Please tell me  How may I help you")
    speak("Hello Sir ! I am Your Desktop Voice Assistant,  Please tell me  How may I help you")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en')
        print(f"user said {query}")
    except:
        speak("Sorry Sir, Say it Again")
        print("Sorry Sir, Say it Again")
        return "None"
    return query
if __name__=='__main__': 
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=1)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'hi' in query:
            print('Hello Sir')
            speak("Hello Sir")
            
        elif 'who are you' in query:
            print('I  yours Desktop Voice assistant')
            speak('I  yours Desktop Voice assistant')
        
        elif 'how are you' in query:
            print('I am Fine Sir')
            speak('I am Fine Sir')
        
        elif 'create' in query or 'creator' in query:
            print("Zainul Creates Me")
            speak("Zainul Creates Me")
            
        elif 'open youtube' in query:
            print("Ok sir , I am opening Youtube")
            speak("Ok sir , I am opening Youtube")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            print("Ok sir , I am opening Google")
            speak("Ok sir , I am opening Google")
            webbrowser.open("google.com")
            
        elif 'open wikipedia' in query:
            print("Ok sir , I am opening Wikipedia")
            speak("Ok sir , I am opening Wikipedia")
            webbrowser.open("wikipedia.com")
            
        elif 'open facebook' in query:
            print("Ok sir , I am opening Facebook")
            speak("Ok sir , I am opening Facebook")
            webbrowser.open("facebook.com")
            
        elif 'open stackoverflow ' in query:
            print("Ok sir , I am opening Stackoverflow")
            speak("Ok sir , I am opening Stackoverflow")
            webbrowser.open("stackoverflow.com")
        
        elif 'music' in query:
            while True:
                print("Please Tell me Song Name Sir")
                speak('Please Tell me song name Sir')
                song_name=takecommand().lower()
                music_dir=r'E:\My own music'
                songs=os.listdir(music_dir)
                print(song_name)
                if 'quit' in song_name:
                    print('Ok Sir ! I am Quitting \n Have a Nice Day')
                    speak('Ok Sir ! I am Quitting \n Have a Nice Day')
                    quit()
                elif 'random' in song_name:
                    print('I am Playing any random Song')
                    speak('I am Playing any random Song')
                    no_of_songs=len(songs)
                    play=random.randint(0,no_of_songs)
                    os.startfile(os.path.join(music_dir,songs[play]))
                    
                for present_song in songs:
                    if song_name in present_song.lower():
                        speak(f"Ok sir , I am Playing {present_song}")
                        print(f"Ok sir , I am Playing '{present_song}' ")
                        ind_of_song=songs.index(present_song)
                        os.startfile(os.path.join(music_dir,songs[ind_of_song]))
                        quit()
                print("Song Not Found Sir")
                speak("Song Not Found Sir")
            
        elif 'time' in query:
            the_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(the_time)
            speak(f"Sir , The time is {the_time}")   
            
        elif 'open code' in query:
            print("Ok sir , I am opening Visual Studio Code")
            speak("Ok sir , I am opening Visual Studio Code")
            code_path=r"C:\Users\Zainul Abedeen\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
            
        elif 'quit' in query:
            print('Thank you sir. I am quitting \n Have a Nice Day')
            speak('Thank you sir. I am quitting \n Have a Nice Day')
            exit()
              