import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
class ShowOnMonitor:
    def __init__(self):
        self.text=['pass','fail','incorrect']   #偵測結果
        self.img=None
        self.bg='white'
        self.label_bg=['green','red','yellow']   #字體背景顏色
        self.fg='#263238'   #字體顏色
        self.font=('Arial', 24)   #字體以及大小
        #self.window = tk.Tk()
        #self.window.title('window')
        #self.window.geometry('1280x720')
        #self.mybutton = tk.Button(self.window, text='button', command= lambda img=self.img,result=0:self.show(result,img))
        #self.mybutton.grid(column=200,row=200)
        #self.window.mainloop()
    def choose_bg(self):
        self.modify_bg(self.bg_color.get())
        
    def choose_fg(self):
        self.modify_fg(self.fg_color.get())
        
    def modify_text(self,new_text):
        self.text=new_text
        
    def modify_bg(self,new_bg):
        self.bg=new_bg
        
    def modify_label_bg(self,new_label_bg):
        self.label_bg=new_label_bg
        
    def modify_fg(self,new_fg):
        self.fg=new_fg
        
    def modify_font(self,new_font):
        self.font=new_font
        
    def setting(self):
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        window.configure(bg=self.bg)
        bg_colors = ['purple','green','orange','yellow','red','white']
        self.bg_color = ttk.Combobox(window, state='readonly')
        self.bg_color['values'] = bg_colors
        self.bg_color.grid(column=0,row=0)
        self.bg_color.current(0)
        self.a=tk.Button(window, text='change background', command= self.choose_bg)
        self.a.grid(column=0,row=1)
        fg_colors = ['blue','green','orange','yellow','red','white']
        self.fg_color = ttk.Combobox(window, state='readonly')
        self.fg_color['values'] = fg_colors
        self.fg_color.grid(column=0,row=2)
        self.fg_color.current(0)
        self.e=tk.Button(window, text='change font color', command= self.choose_fg)
        self.e.grid(column=0,row=4)
        window.mainloop()
        
    def show(self,result,img):
        #self.mybutton.destroy()
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        window.configure(bg=self.bg)
        lbl_1 = tk.Label(window, text=self.text[result], bg=self.label_bg[result], fg=self.fg, font=self.font)
        lbl_1.grid(column=0, row=2)
        self.img=img
        self.img = self.img.resize((self.img.width*2,self.img.height*2))
        imgtk=ImageTk.PhotoImage(self.img)
        lb=tk.Label(window,image=imgtk)
        lb.image = imgtk
        lb.grid(column=0,row=3)
        window.mainloop()
#img = Image.open('IMG_4338.jpg')
#warn=ShowOnMonitor()
#warn.show(0,img)