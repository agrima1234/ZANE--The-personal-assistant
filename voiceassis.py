from cgitb import text
from operator import ge
import random
from urllib.request import CacheFTPHandler
import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import time
import subprocess
import tkinter
import pyjokes
from playsound import playsound
import keyboard
import cv2
from requests import get
import ctypes
import PIL
from PIL import ImageTk, Image
import pywhatkit as kit




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    print("Dash" + ":" + text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour < 12:
        speak("Hello Good Morning")
    elif hour >=12 and hour < 16:
        speak("Hello Good Afternoon")
    else:
        speak("Hello Good Evening")
    speak("I am Zane! How can I help you?")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 100
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=3)
        print("Stop")
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language= 'en-US')
        print('You:' + query )


    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query




def date():
    now = datetime.datetime.now()
    month_name= now.month
    day_name = now.day
    month_names = ['January', 'February','March','April','May', 'June','July', 'August', 'September','October', 'November', 'December']
    ordinalnames = ['1st', '2nd','3rd','4th', '5th', '6th', '7th', '8th','9th','10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    speak("Today is "+ month_names[month_name-1]+" " + ordinalnames[day_name-1]+ ".")
                                   

def process():
    run = 1
    if __name__ == '__main__':
            while run == 1:
                wishMe()
                statement = get_audio().lower()
                results = ''
                run +=1

            if "hello" in statement or "hi" in statement:
                speak("Sure")
            
            if "open notepad" in statement:
                speak("opening notepad")
                notepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\ notepad.exe"
                os.startfile(notepath)
     
            if "open command prompt" in statement:
                speak("opening command prompt")
                os.system("start cmd")

            if "open camera" in statement:
                speak("opening camera")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(100)
                    if k==27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
            if "play music" in statement:
                music_dir = "D:\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))


            if "ip address" in statement:
                ip = get("https://api.ipify.org").text
                speak(f"Your ip address is {ip}")

            if 'wikipedia' in statement:
                try:
                    speak('Searching Wikipedia')
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences = 3)
                    speak('According to wikipedia')
                    speak(results)
                    print(results)
                except:
                    speak('Error')

            if 'joke' in statement:
                speak(pyjokes.get_joke())

            if 'open youtube' in statement:
                webbrowser.open_new_tab("youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            if 'open google' in statement:
                speak("What should i search on google?")
                statement = get_audio().lower()
                webbrowser.open(f"{statement}")

           # if "send message" in statement:
            if 'send message' in statement:
                speak("sending message")
                kit.sendwhatmsg("+918318304004", "this is testing.",2,25)

            if 'open facebook' in statement:
                webbrowser.open_new_tab("www.facebook.com")
                speak("facebook is open now")
                time.sleep(9)

            if 'open gmail' in statement:
                webbrowser.open_new_tab("mail.google.com")
                speak("Google Mail is open now")
                time.sleep(5)

            if 'open news' in statement:
                webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/allahabad")
                speak("Here are some headlines from the Times Of India, Happy reading")
                time.sleep(5)

            if 'cricket' in statement:
                webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in statement:
                webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak("Here are the latest covid19 numbers")
                time.sleep(6)

            if 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in statement:
                date()

            if 'who are you' in statement:
                speak('I am Dash, your personal assistant. I am programmed to perform minor tasks and make you work easily.')

def main():
     root = tkinter.Tk()
     root.config(bg="black")
     bgImg = Image.open("bg1.png")
     root.title("Zane - Your Personal Assistant")
     clk_button = Image.open('—Pngtree—tech style start button element_5627179.png')
     resized = clk_button.resize((250,200),Image.ANTIALIAS)
     new_pic = ImageTk.PhotoImage(resized)
     m_button = tkinter.Button(root,image=new_pic,bg="black", command=process, borderwidth=0 )
     m_button.pack(side= tkinter.BOTTOM, padx=0, pady=0)
     

     canvas = tkinter.Canvas(root,width = 1000,height = 650)
     image=ImageTk.PhotoImage(bgImg)
     label = tkinter.Label(root, text='WELCOME TO YOUR PERSONAL ASSISTANT. KINDLY PRESS THE BUTTON TO START...')
     canvas.create_image(503,350, anchor= None, image=image)
     
     shape = canvas.create_oval(10,10,60,60,fill = "black")
     xspeed = random.randrange(1,10)
     yspeed = random.randrange(1, 10)

     shape2 = canvas.create_oval(10,10,60,60,fill = "black")
     xspeed2 = random.randrange(1,10)
     yspeed2 = random.randrange(1,10)

     canvas.pack()

     while True:
        canvas.move(shape,xspeed,yspeed)
        pos = canvas.coords(shape)
        if pos[3]>= 650 or pos[1] <=0:
            yspeed = -yspeed
        if pos[2] >= 1000 or pos[0] <=0:
            xspeed= -xspeed

        canvas.move(shape2,xspeed2,yspeed2)
        pos = canvas.coords(shape2)
        if pos[3]>= 650 or pos[1] <=0:
            yspeed2 = -yspeed2
        if pos[2] >= 1000 or pos[0] <=0:
            xspeed2= -xspeed2                                
        root.update()
        time.sleep(0.01)
     
    
def ball():
     canvas = tkinter.Canvas()
 



main()

root.mainloop()

