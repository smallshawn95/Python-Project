import tkinter as tk
from tkinter.constants import HORIZONTAL
win = tk.Tk()
win.title("Shawn")
win.geometry("500x250")
win.config(background="skyblue")
win.attributes("-topmost",1)

def change(self):
    s_value = s.get()
    win.attributes("-alpha",s_value/100)
    
s = tk.Scale(orient=HORIZONTAL) #直變橫
s.config(width=10,length=200,background="pink")
s.config(from_=50,to=100)
s.config(showvalue=1,tickinterval=50)
s.config(resolution=10,digits=4)
s.config(command=change)
s.set(100)
s.pack()

win.mainloop()