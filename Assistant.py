"""
Assistant
1. open youtube
2. open browser
3. open wikipedia article on our choice
4. tells date
5. wish us according to time interval
6. play music
"""
import random
import datetime
import calendar
import speech_recognition as sr
import wikipedia
import pyaudio
import datetime
import warnings
from gtts import gTTS
import os
from tkinter import messagebox
import webbrowser

# ignore warnings
warnings.filterwarnings('ignore')

# recognize speech
def recognize():
    # record audio
    r = sr.Recognizer()
    # open mic and start listening to user
    with sr.Microphone() as source:
        print('Yes, how can i help you.....')
        audio = r.listen(source)
    # recognize what the task is
    data = ''
    try:
        data = r.recognize_google(audio)
        print('Command: ----------> ' + data)
    except sr.UnknownValueError:
        print('GSR unable to understand')
    except sr.RequestError as e:
        print('Recognition service error: '+str(e))
    return data

# speaker
def speaker(text):
    print(text)
    my_obj = gTTS(text=text, lang='en', slow=False)
    my_obj.save('Assistant_Audio.mp3')
    os.system('start Assistant_Audio.mp3')

# wishing system
def wishMe():
    print("Hello! i'm Assistant")
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        print('Good Morning')
    elif hour >= 12 and hour < 17:
        print('Good Afternoon')
    elif hour >= 17 and hour < 21:
        print('Good Evening')
    else:
        print('Good Night')
wishMe()

# waking up
def waking(text):
    WAKE = ['hey listen', 'listen', 'assistant']
    text = text.lower()
    for format in WAKE:
        if format in text:
            return True
    return False

# play music
def playMusic(text):
    WISH = ['play music']
    text = text.lower()
    for phrase in WISH:
        if phrase in text:
            return True
    return False
'''def stopMusic(text):
    WISH = ['stop music']
    text = text.lower()
    for phrase in WISH:
        if phrase in text:
            return True
    return False'''

# get date
def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # e.g Monday
    month_num = now.month
    day_num = now.day

    # list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    # ordinal numbers
    ordinal_numbers = [
        '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
        '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
        '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th',
        '31st'
    ]
    return 'Today is ' + weekday + ' ' + month_names[month_num - 1] + ' the ' + ordinal_numbers[day_num - 1] + '.'

# wikipedia
def getPerson(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]
        if wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]
        if wordList[i].lower() == 'what' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]
        if wordList[i].lower() == 'recipe' and wordList[i + 1].lower() == 'for':
            return wordList[i + 2] + ' ' + wordList[i + 3]
        if wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'make':
            return wordList[i + 2] + ' ' + wordList[i + 3]
        if wordList[i].lower() == 'creator' and wordList[i + 1].lower() == 'of':
            return wordList[i + 2] + ' ' + wordList[i + 3]

# web browser
def browser(text):
    WISH = ['open broswer', 'google', 'open google']
    for phrase in WISH:
        if phrase in text.lower():
            return True
    return False
def youtube(text):
    WISH = ['open youtube', 'youtube',]
    for phrase in WISH:
        if phrase in text.lower():
            return True
    return False

# stopwords
def stopwords(text):
    WISH = ['goodbye', 'good bye', 'bye', 'talk yo you later']
    for phrase in WISH:
        if phrase in text.lower():
            return True
    return False

while True:
    listenAudio = sr.Recognizer()
    response = ''
    with sr.Microphone() as source:
        print('.....')
        audio = listenAudio.listen(source)
    try:
        dataAudio = listenAudio.recognize_google(audio)
        if (stopwords(dataAudio) == True):
            print('Good Bye')
            break
        if (waking(dataAudio) == True):
            text = recognize()
            if (playMusic(text) == True):
                mList = []
                music_dir = 'MusicFolder'
                songs = os.listdir(music_dir)
                mList.extend(songs)
                os.startfile(os.path.join(music_dir, random.choice(mList)))
            if ('date') in text:
                response = response + ' ' +  date()
                speaker(response)
            if (browser(text) == True):
                webbrowser.open('https://www.google.com/')
            if (youtube(text) == True):
                webbrowser.open('https://www.youtube.com/')
            if ('who is') in text:
                person = getPerson(text)
                page = wikipedia.summary(person, sentences=2)
                response = response + page
                speaker(response)
                messageResponse = messagebox.askyesno(str(person), 'like to open in web browser?')
                if messageResponse > 0:
                    load = wikipedia.page(person)
                    webbrowser.open(load.url, new=1)
                else:
                    pass
        else:
            pass
    except sr.UnknownValueError:
        print('GSR unable to understand')
    except sr.RequestError as e:
        print('Recognition service error: '+str(e))
