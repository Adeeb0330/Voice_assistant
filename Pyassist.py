# Importing a module related to music functionality (could be custom or third-party)
import music
# Importing the pyttsx3 text-to-speech library and aliasing it as 'px'
import pyttsx3 as px
# Importing the speech recognition library and aliasing it as 'sr'
import speech_recognition as sr
# Importing everything (*) from the News module (likely custom/third-party for fetching/displaying news)
from News import *
# Importing the randfacts library to generate random facts
import randfacts
# Importing everything (*) from the joke module to generate jokes
from joke import *
# Importing the 'infow' function/class from the Pyweb module (likely for web scraping or retrieving information)

# Importing 'temp' (temperature) and 'des' (description) from the weather module to fetch weather data
from weather import temp, des
# Importing everything (*) from the youtubeauto module for automating YouTube interactions
from youtubeauto import *
#import bulit-in datetime to work with dates and times
import datetime
#importing the pyaudio library for capturing and playing audio
import pyaudio

engine = px.init()  #initialize pyttsx3 text-to-speech engine
rate = engine.getProperty('rate') #Get the current speaking rate of the engine
engine.setProperty('rate',160) #Set speaking rate to 160 words per minute
voices = engine.getProperty('voices') #Get the list of voice
engine.setProperty('voice',voices[1].id) #Female voice (2nd voice)


def speak(text):  #Define a function 'speak' that takes 'text' as an argument
    engine.say(text) #Use pyttsx3 engine to convert the text to speech
    engine.runAndWait() #Process the voice command and wait for the speech to finish

def wishme(): # Define a function 'wishme' to greed based on the current time of day
    hour = int(datetime.datetime.now().hour)  #Get the current hour as an integer(24-hour format)
    if hour>=0 and hour<12: #if the current hour between 0 and 12 , return good morning
        return "Good Morning"
    elif hour>=12 and hour<18: #if the current hour between 12 and 18 , return good morning
        return "Good Afternoon"
    else:
        return "Good Evening" #if the current hour is 18 are later, return 'Good evening'

today_date = datetime.datetime.now() # To get the current date and time and store it in the variable 'today_date'
r = sr.Recognizer()  #assign sr recognizer to r

print('Hello, i am your voice assistant')
speak('Hello, '+wishme()+', i am your voice assistant')

#today_date.strftime("%d"): Gets the current day of the month.
#today_date.strftime("%B"): Gets the full name of the current month
#today_date.strftime("%A"): Gets the full name of the current weekday
print('Today is ' + today_date.strftime(" %d ") + " of " + today_date.strftime(" %B ") + " And its currently " + today_date.strftime(" %A ") + ".")
speak('Today is ' + today_date.strftime(" %d ") + " of " + today_date.strftime(" %B ") + " And its currently " + today_date.strftime(" %A ") + ".")

#Calls the temp() function to get the current temperature, coverting into string
#Calls the des() function to get the weather description, coverting into string
print('Current Temperature is ' + str(temp())+ " and with " + str(des()))
speak('Current Temperature is ' + str(temp())+ " and with " + str(des()))
print('What can i do for you')
speak('What can i do for you')

with sr.Microphone() as source: # Use the default microphone as the audio input source
    r.energy_threshold = 10000 # Set the energy threshold for speech recognition (high sensitivity)
    r.adjust_for_ambient_noise(source,1.2)  # Adjust the recognizer to ignore ambient noise for a duration of 1.2 seconds
    print('Listening...')
    audio = r.listen(source) # Capture the audio input from the microphone until silence is detected
    text2 = r.recognize_google(audio)  # Convert the captured audio into text using Google's speech recognition

if 'information' in text2: #Check the word information in voice to process this block of code
    print('You need Information related to which topic ? ')
    speak('You need Information related to which topic ? ')

    with sr.Microphone() as source: # Use the default microphone as the audio input source
        r.energy_threshold = 10000 # Set the energy threshold for speech recognition (high sensitivity)
        r.adjust_for_ambient_noise(source,1.2) # Adjust the recognizer to ignore ambient noise for a duration of 1.2 seconds
        print('Listening...')
        audio = r.listen(source) # Capture the audio input from the microphone until silence is detected
        infor = r.recognize_google(audio) # Convert the captured audio into text using Google's speech recognition
    print('Searching {} in wikipedia'.format(infor))
    speak('Searching {} in wikipedia'.format(infor))

#infow() is a class in python used to retrieve information
    assist = infow() # Creating an instance of the infow class
    assist.get_info(infor) #Retriving data from infor

elif 'play' and 'video' in text2: #Check the word play and video in voice to process this block of code
    print("which video do you want to play")
    speak("which video do you want to play")
    with sr.Microphone() as source: # Use the default microphone as the audio input source
        r.energy_threshold = 10000 # Set the energy threshold for speech recognition (high sensitivity)
        r.adjust_for_ambient_noise(source, 1.2) #Adjust the recognizer to ignore ambient noise for a duration of 1.2 seconds
        print('Listening...')
        audio = r.listen(source) # Capture the audio input from the microphone until silence is detected
        vid = r.recognize_google(audio) # Convert the captured audio into text using Google's speech recognition
    print('Playing {} on youtube'.format(vid))
    speak('Playing {} on youtube'.format(vid))
    assist = Music() #Creating object(assist) and assign to the clsss(Music)
    assist.play(vid) ## This will open the YouTube video in the default browser

elif "news" in text2: #Check the word 'news' in voice to process this block of code
    print("Sure, Now I will read news for you")
    speak("Sure, Now I will read news for you")
    arr=news() # This calls the news function again and assigns the result to arr
    for i in range(len(ar)): # Loop to get the top 3 articles
        print(ar[i])
        speak(ar[i])

elif "joke" in text2: #Check the word 'joke' in voice to process this block of code
    print("Sure, Get ready for some chuckles")
    speak("Sure, Get ready for some chuckles")
    arr = joke()  #This calls the joke function again and assigns the result to arr
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "fact" or "facts" in text2: #Check the word 'fact' and 'facts' in voice to process this block of code
    print("Sure, Now I will read facts")
    speak("Sure, Now I will read facts")
    x = randfacts.get_fact() # Fetches a random fact and stores it in the variable x
    print(x)
    speak("Did you know that, "+x) # Uses a speak function to say the fact aloud


