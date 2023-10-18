import tkinter as tk

win = tk.Tk()
win.title('Relief style')
win.geometry('300x150')

lb_1 = tk.Label(text = 'flat', relief = 'flat')
lb_1.pack()
lb_2 = tk.Label(text = 'groove', relief = 'groove')
lb_2.pack()
lb_3 = tk.Label(text = 'raised', relief = 'raised')
lb_3.pack()
lb_4 = tk.Label(text = 'ridge', relief = 'ridge')
lb_4.pack()
lb_5 = tk.Label(text = 'solid', relief = 'solid')
lb_5.pack()
lb_6 = tk.Label(text = 'sunken', relief = 'sunken')
lb_6.pack()

win.mainloop()
