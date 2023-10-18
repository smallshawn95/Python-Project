import tkinter as tk

win = tk.Tk()
win.title('計數器')
win.geometry('250x150')
win.config(bg = 'white')

number = 0
def run_counter(lb):
    def counting():
        global number
        number += 1
        lb.config(text = str(number))
        lb.after(1000, counting)
    counting()

lb = tk.Label(bg = 'white', fg = 'pink')
lb.config(width = 8, height = 2)
lb.config(font = '微軟正黑體 30')
lb.pack()
run_counter(lb)

win.mainloop()
