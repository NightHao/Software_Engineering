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
    def choose_label_bg(self):
        modified_label_bg_color=self.label_bg_color.get().split(' ')
        self.modify_label_bg(modified_label_bg_color)
        
    def choose_font(self):
        self.modify_font(self.font.get())
        
    def choose_text(self):
        modified_text=self.text.get().split(' ')
        self.modify_text(modified_text)
        
    def modify_text(self,new_text):
        self.text=new_text
        
    def modify_bg(self,new_bg):
        self.bg=new_bg
        
    def modify_label_bg(self,new_label_bg):
        self.label_bg=new_label_bg
        
    def modify_fg(self,new_fg):
        self.fg=new_fg
        
    def modify_font(self,new_font):
        self.font=new_font,50
        
    def setting(self):
        
        
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        window.configure(bg=self.bg)
        
        label1 = tk.Label(window,text='Monitor Setting',font=('Arial','24'),bg='white').grid(column=1,row=0)
        
        label2 = tk.Label(window,text='Background',font=('Arial','20'),bg='white').grid(column=1,row=1)
        
        bg_colors = ['purple','green','orange','yellow','red','white']
        self.bg_color = ttk.Combobox(window, state='readonly')
        self.bg_color['values'] = bg_colors
        self.bg_color.grid(column=1,row=2)
        self.bg_color.current(0)
        self.bg_button=tk.Button(window, text='Change', command= self.choose_bg)
        self.bg_button.grid(column=2,row=2)
        
        label2 = tk.Label(window,text='Font color',font=('Arial','20'),bg='white').grid(column=1,row=3)
        
        fg_colors = ['blue','green','orange','yellow','red','white']
        self.fg_color = ttk.Combobox(window, state='readonly')
        self.fg_color['values'] = fg_colors
        self.fg_color.grid(column=1,row=5)
        self.fg_color.current(0)
        self.fg_button=tk.Button(window, text='Change', command= self.choose_fg)
        self.fg_button.grid(column=2,row=5)
        
        label3 = tk.Label(window,text='Label background color',font=('Arial','20'),bg='white').grid(column=1,row=6)
        
        label_bg_colors=[["blue",'red','yellow'],['green','purple','yellow']]
        self.label_bg_color = ttk.Combobox(window, state='readonly')
        self.label_bg_color['values'] = label_bg_colors
        self.label_bg_color.grid(column=1,row=7)
        self.label_bg_color.current(0)
        self.label_bg_button=tk.Button(window, text='Change', command= self.choose_label_bg)
        self.label_bg_button.grid(column=2,row=7)
        
        label4 = tk.Label(window,text='Font',font=('Arial','20'),bg='white').grid(column=1,row=8)
        
        fonts=['Arial','italic','Stencil']
        self.font = ttk.Combobox(window, state='readonly')
        self.font['values'] = fonts
        self.font.grid(column=1,row=9)
        self.font.current(0)
        self.font_button=tk.Button(window, text='Change', command= self.choose_font)
        self.font_button.grid(column=2,row=9)
        
        label4 = tk.Label(window,text='Text',font=('Arial','20'),bg='white').grid(column=1,row=10)
        
        texts=[['pass','fail','incorrect'],['通過','失敗','沒戴好'],['合格','不合格','正しくない']]
        self.text = ttk.Combobox(window, state='readonly')
        self.text['values'] = texts
        self.text.grid(column=1,row=11)
        self.text.current(0)
        self.text_button=tk.Button(window, text='Change', command= self.choose_text)
        self.text_button.grid(column=2,row=11)
        
        window.mainloop()
        
    def show(self,result,img):
        #self.mybutton.destroy()
        window = tk.Tk()
        window.title('window')
        window.geometry('1280x720')
        window.configure(bg=self.bg)
        lbl_1 = tk.Label(window, text=self.text[result], bg=self.label_bg[result], fg=self.fg, font=(self.font,'30'))
        #lbl_1.grid(column=0, row=2)
        lbl_1.pack()
        self.img=img
        self.img = self.img.resize((self.img.width*2,self.img.height*2))
        imgtk=ImageTk.PhotoImage(self.img)
        lb=tk.Label(window,image=imgtk)
        lb.image = imgtk
        #lb.grid(column=0,row=3)
        lb.pack()
        window.mainloop()

#img = Image.open('test.jpg')
#warn=ShowOnMonitor()
#warn.setting()
#warn.show(0,img)
#warn.show(0,img)