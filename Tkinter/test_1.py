import tkinter as tk
win = tk.Tk()
win.title("Shawn")
win.geometry("500x250")
win.config(background="pink")
win.attributes("-topmost",1)

def Shawn():
    text = en.get()
    lb.config(text=text)

#標籤製作
lb = tk.Label(text="請輸入：")
lb.config(background="skyblue",foreground="white")
lb.config(font="cavorting 15")  # 更改字體
lb.pack()

#輸入對話框
en = tk.Entry()
en.pack()

btn = tk.Button(text="送出",command=Shawn)
btn.pack()

win.mainloop()
