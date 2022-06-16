import os
import time
import pygame
import tkinter as tk
from tkinter import ttk
from gtts import gTTS # langulage code list: https://developers.google.com/admin-sdk/directory/v1/languages
    
class Speaker():
    """
    docstring for speaker.
    Speaker is for speaking waring.
    speak_warning(), set_language(), set_volume() and set_warning() is public func can be called.
    speak_warning(int situation) - speak the setted warning texts.0: with mask 1: no mask 2: no proper mask.
    set_language(string mylang) - set the language.
    set_volume(int volume) - set the volume from 0-100.
    set_warning(int situation, string text) - can set the warning texts.
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
        
    def setting(self):
        soundwindow = tk.Tk()
        soundwindow.title('sound')
        soundwindow.geometry('1280x720')
        label1 = tk.Label(soundwindow,text='Sound Setting',font=('Arial','24'),bg='white').grid(column=1,row=0)
        label2 = tk.Label(soundwindow,text='Language',font=('Arial','20'),bg='white').grid(column=1,row=1)
        languages = ["en","zh-tw"]
        self.language = ttk.Combobox(soundwindow, state='readonly')
        self.language['values'] = languages
        self.language.grid(column=1,row=2)
        self.language.current(0)
        self.language_button=tk.Button(soundwindow, text='Change', command= self.choose_language)
        self.language_button.grid(column=2,row=2)
        
        label3 = tk.Label(soundwindow,text='volume',font=('Arial','20'),bg='white').grid(column=1,row=3)
        font = ('Arial', 20)
        select = tk.IntVar()
        scale = tk.Scale(label='Scale Widget', font=font, orient=tk.HORIZONTAL, showvalue=False,bg='green', fg='white', tickinterval=20, length=800, width=30,troughcolor='blue', variable=select, command=self.set_volume)
        scale.grid(column=1,row=4)
        self.label = tk.Label(text='', width=40, font=font)
        self.label.grid(row=2, column=4)
        
        soundwindow.mainloop()
        

    def choose_language(self):
        self.set_language(self.language.get())


    def speak_warning(self,situation):
        if situation==0:
            mytext=self.__with_texts.get(self.__language)
            mylang=self.__language

        elif situation==1:
            mytext=self.__no_texts.get(self.__language)
            mylang=self.__language

        elif situation==2:
            mytext=self.__no_proper_texts.get(self.__language)
            mylang=self.__language
        
        try:#try to make tts mp3 file
            tts = gTTS(text=mytext, tld="com", lang=mylang)
            filename = mylang+"_alarm_voice.mp3"
            tts.save(filename)
            try:#try to play file
                pygame.mixer.music.load('./'+filename)
                pygame.mixer.music.set_volume(self.__volume)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                pygame.mixer.music.unload()
            except:
                print('error when play '+filename)
            os.remove(filename)
        except:
            print('error when speak '+mylang+': '+mytext)
        

    def set_language(self,mylang):
        self.__language=mylang


    def set_volume(self,volume):
        self.__volume=int(volume)/100


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

    def test_show(self):
        print("language: "+self.__language)
        print("situation 0: "+self.__with_texts[self.__language])
        print("situation 0: "+self.__no_texts[self.__language])
        print("situation 0: "+self.__no_proper_texts[self.__language])
        print("volume: "+self.__volume)


if __name__=='__main__':
    speaker =Speaker()
    print("start")
    speaker.set_language("zh-tw")
    speaker.set_warning(2,"遮住口鼻")
    speaker.set_volume(100)
    speaker.speak_warning(2)
    speaker.set_volume(30)
    speaker.speak_warning(2)
    print("聲音測試結束，呼叫設定視窗，請按任意鍵繼續")
    os.system("pause")
    speaker.setting()
    speaker.speak_warning(2)


# according https://stackoverflow.com/a/64367776/17732660
# gTTS of gtts doc https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS