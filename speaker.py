import os
import time
import playsound # please use playsound==1.2.2 to avoid unexpected error
from gtts import gTTS # langulage code list: https://developers.google.com/admin-sdk/directory/v1/languages
    
class Speaker():
    """docstring for speaker. Speaker is for speaking waring."""
    __texts={"en":"please wear on your mask","zh-tw":"請戴上口罩","ja":"マスクをする"}
    """def __init__(self, arg):
        super(speaker, self).__init__()
        self.arg = arg"""

    def show_setting_GUI(self):
        end

    def speak_warning(self):
        for text in __texts.keys():
            __speak(text,__texts.get(text))

    def test(self):
        print("start test")
        self.__speak("this is speaker test",'en')
        self.__speak("這是語音測試",'zh-tw')
        self.__speak("これは音声テストです",'ja')

    def __speak(self,mytext, mylang="en"):
        try:
            print('make '+mylang+': '+mytext)
            time.sleep(1)
            tts = gTTS(text=mytext, tld="com", lang=mylang)
            filename = mylang+"_alarm_voice.mp3"
            tts.save(filename)
            __play(filename)
            os.remove(filename)
        except:
            print('error when make '+mylang+': '+mytext)

    def __play(self,filename):
        try:
            print('play '+filename)
            playsound.playsound('./'+filename)
        except:
            print('error when play '+filename)

'''
speaker =Speaker()
print("start")
speaker.test()
'''
# according https://stackoverflow.com/a/64367776/17732660
# gTTS of gtts doc https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS