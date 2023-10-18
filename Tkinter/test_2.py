import tkinter as tk
#處理隨機數生成的模組
import random
#處理複製功能的模組
import pyperclip

win = tk.Tk()
win.title("Shawn")
win.geometry("500x250")
win.config(background="pink")
win.attributes("-topmost",1)
# win.iconbitmap("C:\python\Shawn.ico")

title_text = tk.Label(text="Random X,Y Generator")
title_text.config(background="pink",foreground="white")
title_text.config(font="微軟正黑體 15")
title_text.pack()

min_range = tk.Label(text="Min range")
min_range.config(background="pink",foreground="blue",font="微軟正黑體 12")
min_range.pack()
min_entry = tk.Entry()
min_entry.pack()

max_range = tk.Label(text="Max range")
max_range.config(background="pink",foreground="blue",font="微軟正黑體 12")
max_range.pack()
max_entry = tk.Entry()
max_entry.pack()

x_show = tk.Label(text="")
x_show.config(background="pink",foreground="blue",font="微軟正黑體 13")
x_show.pack()

y_show = tk.Label(text="")
y_show.config(background="pink",foreground="blue",font="微軟正黑體 13")
y_show.pack()

def gen_xy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    x = str(random.randint(min_val,max_val)) #設定隨機數的範圍
    y = str(random.randint(min_val,max_val))
    x_show.config(text="X：" +x)
    y_show.config(text="Y：" +y)

def copy():
    xy = x_show.cget("text") + "\n" + y_show.cget("text")
    pyperclip.copy(xy)


generate_btn = tk.Button(text="Generate",command=gen_xy)
generate_btn.config(background="white",foreground="orange",font="微軟正黑體 8")
generate_btn.config(width=10,height=1)
generate_btn.pack()

copy_btn = tk.Button(text="Copy",command=copy)
copy_btn.config(background="white",foreground="orange",font="微軟正黑體 8")
copy_btn.config(width=10,height=1)
copy_btn.pack()

win.mainloop()
