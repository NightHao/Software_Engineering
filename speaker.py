import os
import time
import pygame
from gtts import gTTS # langulage code list: https://developers.google.com/admin-sdk/directory/v1/languages
    
class Speaker():
    """
    docstring for speaker.
    Speaker is for speaking waring.
    set_warning(), get_texts(), show_setting_gui(), speak_warning() and test() is public func can be called.
    speak_warning(int) - speak the setted warning texts.0: with mask 1: no mask 2: no proper mask.
    set_language(string mylang) - set the language.
    set_warning(int situation, string text) - can set the warning texts.
    test() - speak the defalt test texts.
    """
    #0: with mask 1: no mask 2: no proper mask

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.__language="en"
        self.__volume=0.7
        self.__with_texts={"en":"mask checked","zh-tw":"已戴上口罩"}
        self.__no_texts={"en":"please wear on your mask","zh-tw":"請戴上口罩"}
        self.__no_proper_texts={"en":"please wear on your mask properly","zh-tw":"請戴好口罩，遮住口鼻"}
    
    def speak_warning(self,situation):
        if situation==0:
            self.__speak(self.__with_texts.get(self.__language),self.__language)
        elif situation==1:
            self.__speak(self.__no_texts.get(self.__language),self.__language)
        elif situation==2:
            self.__speak(self.__no_proper_texts.get(self.__language),self.__language)

    def set_language(self,mylang):
        self.__language=mylang

    def set_volume(self,volume):
        self.__volume=volume/100

    def set_warning(self,situation,text):
        try:
            if situation==0:
                self.__with_texts[self.__language]=text
                print("set "+self.__language+' with_texts to '+text)
            elif situation==1:
                self.__no_texts[self.__language]=text
                print("set "+self.__language+' no_texts to '+text)
            elif situation==2:
                self.__no_proper_texts[self.__language]=text
                print("set "+self.__language+' no_proper_texts to '+text)
        except:
            print('Sound setup FAILED!')

    def test(self):
        print("start test")
        self.__speak("this is speaker test",'en')
        self.__speak("這是語音測試",'zh-tw')
        self.__speak("これは音声テストです",'ja')

    def __speak(self,mytext, mylang="en"):
        try:
            # print('make '+mylang+': '+mytext)
            tts = gTTS(text=mytext, tld="com", lang=mylang)
            filename = mylang+"_alarm_voice.mp3"
            tts.save(filename)
            self.__play(filename)
            os.remove(filename)
        except:
            print('error when speak '+mylang+': '+mytext)

    def __play(self,filename):
        try:
            # print('play '+filename)
            pygame.mixer.music.load('./'+filename)
            pygame.mixer.music.set_volume(self.__volume)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.music.unload()

        except:
            print('error when play '+filename)

'''
speaker =Speaker()
print("start")
# speaker.test()
speaker.set_language("zh-tw")
speaker.set_warning(2,"遮住口鼻")
speaker.set_volume(100)
speaker.speak_warning(2)
speaker.set_volume(30)
speaker.speak_warning(2)
'''

# according https://stackoverflow.com/a/64367776/17732660
# gTTS of gtts doc https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS