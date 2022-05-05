import os
import time
import playsound # please use playsound==1.2.2 to avoid unexpected error
from gtts import gTTS

# langulage code list: https://developers.google.com/admin-sdk/directory/v1/languages

def speak(mytext, mylang="en"):
    try:
        print('make '+mylang+': '+mytext)
        time.sleep(1)
        tts = gTTS(text=mytext, tld="com", lang=mylang)
        filename = mylang+"_alarm_voice.mp3"
        tts.save(filename)
        play(filename)
        os.remove(filename)
    except:
        print('error when make '+mylang+': '+mytext)

def play(filename):
    try:
        print('play '+filename)
        playsound.playsound('./'+filename)
    except:
        print('error when play '+filename)

mytext="please wear on your mask"
language='en'
speak(mytext,language)
mytext="請戴上口罩"
language='zh-tw'
speak(mytext,language)
mytext="マスクを着用してください"
language='ja'
speak(mytext,language)

# according https://stackoverflow.com/a/64367776/17732660
# gTTS of gtts doc https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS