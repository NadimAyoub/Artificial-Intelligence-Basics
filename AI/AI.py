import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is ")
    speak(day)
    speak(month)
    speak(year)


def hello():
    speak("Welcome Sir!")
    time()
    date()
    speak("How can i help you today Sir?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query


def email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ept.companyy@gmail.com', 'eptcompany')
    server.sendmail('ept.companyy@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    hello()
    while True:
        query = command().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("search", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif'email' in query:
            try:
                speak("What should i say?")
                content = command()
                to = 'ept.companyy@gmail.com'
                email(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Email not sent.")
        elif 'search' in query:
            speak("What should i search")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = command().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system("Shutdown -l")
        elif 'shutdwon' in query:
            os.system("Shutdown /s/t 1")
        elif 'restart' in query:
            os.system("Shutdown /r/t 1")
        elif 'offline' in query:
            quit()
