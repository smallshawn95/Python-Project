import tkinter as tk

#建立視窗
win = tk.Tk()
#標題
win.title("Windows")
#大小(寬x高)
win.geometry("500x250")
#最小大小
win.minsize(width=100,height=50)
#最大大小
win.maxsize(width=500,height=250)
#是否可更改視窗大小
win.resizable(0, 0) #1=True 0=False
#標題圖標
win.iconbitmap("./Tkinter/panda.ico")
#背景顏色
win.config(background="pink")
#透明度
win.attributes("-alpha",0.875) #1~0 1=100% 0=0%
#置頂
win.attributes("-topmost",1) #1=True 0=False

win.mainloop()
