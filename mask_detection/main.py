import argparse
from multiprocessing import parent_process
import detect_mask as mask
import show
import time
#import speaker 
import tkinter as tk
class DetectMain:
    def __init__(self):
        self.image_model=mask.DetectImage()
        self.camera_model=mask.DetectCamera()
        self.screen = show.ShowOnMonitor() 
        self.create_window()
        
    def now_start(self, window):
        window.destroy()
        self.detect()
        self.create_window()
    
    def create_window(self):
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        detect_button = tk.Button(window, text='開始偵測', command = lambda: self.now_start(window))
        detect_button.grid()
        setting_button = tk.Button(window, text='設定')
        setting_button.grid()
        window.mainloop()
        
    def opt(self):
        parser = argparse.ArgumentParser()
        print(parser)
        parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')
        self.opt = parser.parse_args()
        
    def detect(self):
        #self.opt()
        Input="test.jpg"
        if(Input=="cam"):
            res, res_image = self.camera_model.image_processing()
            #self.audio.speak_warning(res)
            self.screen.show(res, res_image)
        else:
            self.image_model.opt(Input)
            res, res_image=self.image_model.image_processing()
            #self.audio.speak_warning(res)
            self.screen.show(res, res_image)
detector=DetectMain()