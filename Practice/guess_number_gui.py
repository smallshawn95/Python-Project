import random
import tkinter as tk

win = tk.Tk()
win.title("Guess Number")
win.geometry("300x300")
win.config(background = "skyblue")
win.resizable(0, 0)
win.attributes("-topmost",1)

num = random.randint(1, 1000)
min = 1
max = 1000
times = 0

def renew():
    global min, max, times
    key = int(en.get())
    if key < min or key > max:
        lb_2.config(text = "範圍錯")
        lb_2.pack(pady = 10)
    elif key > num:
        max = key
        times += 1
        lb_2.config(text = "太大了")
        lb_2.pack(pady = 10)
        lb_1.config(text = "猜{:0>4d}到{:0>4d}數字".format(min, max))
    elif key < num:
        min = key
        times += 1
        lb_2.config(text = "太小了")
        lb_2.pack(pady = 10)
        lb_1.config(text = "猜{:0>4d}到{:0>4d}數字".format(min, max))
    elif key == num:
        times += 1
        lb_2.config(text = "猜到了")
        lb_2.pack(pady = 10)
        lb_3.config(text = "總共猜了{:0>3d}次".format(times))
        lb_3.pack()
        lb_1.config(text = num)
    en.delete(0, tk.END)

lb_1 = tk.Label(text = "猜{:0>4d}到{:0>4d}數字".format(min, max), font = "微軟正黑體 14 bold")
lb_1.config(background = "skyblue", padx = 5, pady = 5)
lb_1.pack()
lb_2 = tk.Label(font = "微軟正黑體 20 bold")
lb_2.config(background = "pink", foreground = "blue")
lb_2.config(height = 3, width = 10)
lb_2.pack_forget()
lb_3 = tk.Label(font = "微軟正黑體 12 bold")
lb_3.config(height = 2, width = 20)
lb_3.pack_forget()

en = tk.Entry()
en.pack(pady = 5)

but = tk.Button(text = "送出", command = renew)
but.pack(pady = 5)

win.mainloop()
