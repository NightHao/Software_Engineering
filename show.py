import tkinter as tk
from PIL import Image, ImageTk
class ShowOnMonitor:
    def __init__(self,text,img):
        self.text=text
        self.img = img
    def show(self):
        window = tk.Tk()
        window.title('window')
        window.geometry('800x600')
        lbl_1 = tk.Label(window, text=A, bg='yellow', fg='#263238', font=('Arial', 24))
        lbl_1.grid(column=10, row=0)
        imgTk=ImageTk.PhotoImage(img)
        lb=tk.Label(window,image=imgTk)
        lb.image = imgTk
        lb.grid(column=10,row=100)
        window.mainloop()
A="幹你娘機掰"
img = Image.open('IMG_4338.jpg')
img = img.resize((img.width//5,img.height//5))
warn=ShowOnMonitor(A,img)
warn.show()