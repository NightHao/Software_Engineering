import os
import time

try:
    import tkinter as tk
    import tkinter.messagebox  # Python 3.x
except:
    import Tkinter as tk
    import Tkinter.messagebox # Python 2.x

import playsound # please use playsound==1.2.2 to avoid unexpected error
from gtts import gTTS # langulage code list: https://developers.google.com/admin-sdk/directory/v1/languages
    
class Speaker():
    """docstring for speaker. Speaker is for speaking waring."""
    
    __texts={"en":"please wear on your mask","zh-tw":"請戴上口罩","ja":"マスクをする"}
    
    def __init__(self):
        pass

    def show_setting_GUI(self):
        window=tk.Tk()
        window.title("Sound Warning Setting")
        window.geometry("800x400+250+150")
        
        en_label = tk.Label(window,text="英文警告內容")
        en_label.pack()
        en_entry=tk.Entry(window,width=90)
        en_entry.insert(0,self.__texts["en"])
        en_entry.pack()

        zh_label = tk.Label(window,text="中文警告內容")
        zh_label.pack()
        zh_entry=tk.Entry(window,width=90)
        zh_entry.insert(0,self.__texts["zh-tw"])
        zh_entry.pack()

        ja_label = tk.Label(window,text="日文警告內容")
        ja_label.pack()
        ja_entry=tk.Entry(window,width=90)
        ja_entry.insert(0,self.__texts["ja"])
        ja_entry.pack()

        user_test_button=tk.Button(window,text="測試目前警告音效",command=self.speak_warning)
        user_test_button.pack()

        apply_button=tk.Button(window,text="套用",command=lambda: self.__on_apply_button(en_entry.get(),zh_entry.get(),ja_entry.get()) )
        apply_button.pack()

        window.mainloop()

    def __on_apply_button(self,en_text,zh_text,ja_text):
        self.__texts["en"]=en_text
        self.__texts["zh-tw"]=zh_text
        self.__texts["ja"]=ja_text
        print("設定為:")
        print(en_text)
        print(zh_text)
        print(ja_text)
        tkinter.messagebox.showinfo(title = '設定完成',message = "語音設定完成")

    def speak_warning(self):
        for language in self.__texts:
            self.__speak(self.__texts.get(language),language)

    def test(self):
        print("start test")
        self.__speak("this is speaker test",'en')
        self.__speak("這是語音測試",'zh-tw')
        self.__speak("これは音声テストです",'ja')

    def __speak(self,mytext, mylang="en"):
        try:
            #print('make '+mylang+': '+mytext)
            tts = gTTS(text=mytext, tld="com", lang=mylang)
            filename = mylang+"_alarm_voice.mp3"
            tts.save(filename)
            time.sleep(0.5)
            self.__play(filename)
            os.remove(filename)
        except:
            print('error when make '+mylang+': '+mytext)

    def __play(self,filename):
        try:
            #print('play '+filename)
            playsound.playsound('./'+filename)
        except:
            print('error when play '+filename)

'''
speaker =Speaker()
print("start")
#speaker.test()
#speaker.speak_warning()
speaker.show_setting_GUI()
speaker.speak_warning()
'''
# according https://stackoverflow.com/a/64367776/17732660
# gTTS of gtts doc https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS