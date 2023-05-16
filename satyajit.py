import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')

#print(voices[1].id)

# engine.say("how can i help you satyajit")----it is used to speak
# engine.runAndWait()----- it is used to run the jarvix
def speak(audio):
    voices=engine.getProperty('voices')
    engine.setProperty(voices, voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good moening')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    else:
        speak('good night')


def takeCommand():
    #it take microphone input from user and returns string as output
    r=sp.Recognizer()
    with sp.Microphone() as source:
        print('listning....................')
        r.pause_threshold=3
        #print('working1')
        audio=r.listen(source)
       # print('working2')
    try:
        print('recognizing.......')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    except Exception as e:
        print(e)
        print('say once again....')
        return 'none'
    return query 


if __name__=='__main__':
    speak('hello satyajit welccome back thanakyou')
   
    #takeCommand()
    while True:
        query=takeCommand().lower()
        if'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia',"")
            reasult=wikipedia.summary(query,sentences=3)
            speak('your reasult is ready just listen care fully')
            speak(reasult)
           # break
        elif 'satyajit' in query or 'satyajeet' in query:
            speak('SATYAJIT IS NOW STAYING IN BANGLORE WHAT TYPE OF WORK DO YOU WANT from him')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')  
            break      
        elif 'open code' in query:
            codepath="E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            break
        elif 'open whatsapp' in query:
            print('its called')
            webbrowser.open('whatsapp.com')
            print('working')
        elif 'i want to talk to him' in query:
            speak(' note the number 9090760870')
            speak('just ping message or call him')
            takeCommand()
            if 'once again' in query:
                speak(' note the number 9090760870')
                break
            else:
                break
        elif 'date time' in query:
            date=datetime.datetime.now().strftime('%H:%M:%S')
            print(date)
            speak(date)
        elif 'stop' in query:
             wishMe()
             break
        
