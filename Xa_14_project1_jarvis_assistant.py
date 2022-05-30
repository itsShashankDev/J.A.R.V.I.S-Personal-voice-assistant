from msilib.schema import tables
import webbrowser
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speecg recognition
import wikipedia  #pip install wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5') # here sapi5 is the microsoft software which provides us the male/female assistant voices 
voices = engine.getProperty('voices') #it gets the informatiion about the latest voices stored in the sapi5 of male/female assistants
#print(voices[1].id) #tells about the name of the 1str voice i.e david
engine.setProperty('voice', voices[0].id)


def speak(audio):
    pass
    engine.say(audio) #engine will asy this audio string
    engine.runAndWait() #Runs an event loop until all commands
    # queued u until this method call complete. 
    # Blocks during the event loop and returns when the queue is cleared.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening. I hope that you are having a great day today")
    speak("I am Jarvis sir. Please tell me how may i help you ")

def takeCommand(): 
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('kumarshashank822@gmail.com', 'Keashu@1955')
    server.sendmail('kumarshashank822@gmail.com', to, content)
    server.close()

def search_on_google(query):
    kit.search(query)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #Converting user query into lower case
        
        if 'wikipedia' in query:  #if the word wikipedia is present when user wanted to search anything from it then the wikipedia search will happen
            speak('searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) # only 2 sentences will be printed related to that information
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
        
        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        
        elif 'open bharatacharya' in query:
            webbrowser.open("https://www.bharatacharyaeducation.com/")
        
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number:  93151 14959 ")
            speak("What is the message sir?")
            # message = take_user_input().lower()
            # send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
            
        
        elif 'email to' in query:
            try:
                speak("What should i say?")
                content =  takeCommand()
                to = "keashu897@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry my friend Shashank. I am not able to send this email")