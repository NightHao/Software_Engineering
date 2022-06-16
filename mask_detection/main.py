import argparse
import detect_mask as mask
import show
import speaker 
import tkinter as tk
from tkinter import ttk
class DetectMain:
    def __init__(self):
        self.image_model=mask.DetectImage()
        self.camera_model=mask.DetectCamera()
        self.screen = show.ShowOnMonitor() 
        self.audio = speaker.Speaker()
        self.create_window()
        
    def execute(self, window):
        window.destroy()
        self.detect()
        self.create_window()
        
    def showsetting(self,window):
        window.destroy()
        self.screen.setting()
        self.create_window()

    def soundsetting(self,window):
        window.destroy()
        
        soundwindow = tk.Tk()
        soundwindow.title('sound')
        soundwindow.geometry('1280x720')
        label1 = tk.Label(soundwindow,text='Sound Setting',font=('Arial','24')).grid(column=1,row=0)
        label2 = tk.Label(soundwindow,text='Language',font=('Arial','20')).grid(column=1,row=1)
        
        languages = ["en","zh-tw"]
        self.language = ttk.Combobox(soundwindow, state='readonly')
        self.language['values'] = languages
        self.language.grid(column=1,row=2)
        self.language.current(0)
        self.language_button=tk.Button(soundwindow, text='Change', command=self.choose_language)
        self.language_button.grid(column=2,row=2)
        
        label3 = tk.Label(soundwindow,text='volume',font=('Arial','20')).grid(column=1,row=3)
        font = ('Arial', 20)
        select = tk.IntVar()
        scale = tk.Scale(label='Scale Widget', font=font, orient=tk.HORIZONTAL, showvalue=False, tickinterval=20, length=400, width=30,troughcolor='white', variable=select, command=self.audio.set_volume)
        scale.set(self.audio.get_volume()*100)
        scale.grid(column=1,row=4)
        self.label = tk.Label(text='', width=40, font=font)
        self.label.grid(row=2, column=4)
        
        soundwindow.mainloop()
        self.create_window()
        
    def choose_language(self):
        self.audio.set_language(self.language.get())
        
    def detectsetting(self,window):
        window.destroy()
        detectwindow = tk.Tk()
        detectwindow.title('model setting')
        detectwindow.geometry('800x800')
        label1 = tk.Label(detectwindow,text='Detect Setting',font=('Arial','24')).grid(column=1,row=0)
        label2 = tk.Label(detectwindow,text='Model',font=('Arial','20')).grid(column=1,row=1)
        models = ['keras_model_strong.h5','keras_model.h5']
        self.model_select = ttk.Combobox(detectwindow, state='readonly')
        self.model_select['values'] = models
        self.model_select.grid(column=1,row=2)
        self.model_select.current(0)
        self.model_button=tk.Button(detectwindow, text='Change', command= self.choose_model)
        self.model_button.grid(column=2,row=2)
        detectwindow.mainloop()
        self.create_window()
        
    def choose_model(self):
        self.camera_model.change_model(self.model_select.get())

    def create_window(self):
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        #detect_button = tk.Button(window, text='開始偵測',font=('Arial','24'),command = lambda: self.execute(window))
        imgBtn = tk.PhotoImage(file='start.png')
        #imgBtn=imgBtn.resize(imgBtn.width//3,imgBtn.height//3)
        detect_button = tk.Button(window,image=imgBtn,command = lambda: self.execute(window))
        detect_button.pack()
        setting_button = tk.Button(window, text='顯示設定',font=('Arial','24'),command = lambda: self.showsetting(window))
        setting_button.pack()
        setting_button = tk.Button(window, text='聲音設定',font=('Arial','24'),command = lambda: self.soundsetting(window))
        setting_button.pack()
        setting_button = tk.Button(window, text='模組設定',font=('Arial','24'),command = lambda: self.detectsetting(window))
        setting_button.pack()
        window.mainloop()
        
    def opt(self):
        parser = argparse.ArgumentParser()
        print(parser)
        parser.add_argument('-s','--source', type=str, default='test.jpg', help='image path')
        self.opt = parser.parse_args()
        
    def detect(self):
        #self.opt()
        Input="test.jpg"
        if(Input=="image"):
            self.image_model.opt(Input)
            res, res_image=self.image_model.image_processing()
            self.audio.speak_warning(res)
            self.screen.show(res, res_image)
        else:
            res, res_image = self.camera_model.image_processing()
            self.audio.speak_warning(res)
            self.screen.show(res, res_image)
            
detector=DetectMain()