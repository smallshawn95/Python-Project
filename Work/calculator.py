import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.iconbitmap("./Work/calculator.ico")

def calculate():
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))

def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)

def delete():
    equ.set(str(equ.get())[:-1])

def clear():
    equ.set("0")

equ = tk.StringVar()
equ.set("0")

lb = tk.Label(win, width = 25, height = 2, relief = "raised", anchor = "se", textvariable = equ)
lb.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

btn_clear = tk.Button(win, text = "C", width = 5, fg = "blue", command = clear)
btn_clear.grid(row = 1, column = 0)

tk.Button(win, text = "DEL", width = 5, command = delete).grid(row = 1, column = 1)
tk.Button(win, text = "%", width = 5, command = lambda:show("%")).grid(row = 1, column = 2)
tk.Button(win, text = "/", width = 5, command = lambda:show("/")).grid(row = 1, column = 3)
tk.Button(win, text = "9", width = 5, command = lambda:show("9")).grid(row = 2, column = 0)
tk.Button(win, text = "8", width = 5, command = lambda:show("8")).grid(row = 2, column = 1)
tk.Button(win, text = "7", width = 5, command = lambda:show("7")).grid(row = 2, column = 2)
tk.Button(win, text = "*", width = 5, command = lambda:show("*")).grid(row = 2, column = 3)
tk.Button(win, text = "6", width = 5, command = lambda:show("6")).grid(row = 3, column = 0)
tk.Button(win, text = "5", width = 5, command = lambda:show("5")).grid(row = 3, column = 1)
tk.Button(win, text = "4", width = 5, command = lambda:show("4")).grid(row = 3, column = 2)
tk.Button(win, text = "-", width = 5, command = lambda:show("-")).grid(row = 3, column = 3)
tk.Button(win, text = "3", width = 5, command = lambda:show("3")).grid(row = 4, column = 0)
tk.Button(win, text = "2", width = 5, command = lambda:show("2")).grid(row = 4, column = 1)
tk.Button(win, text = "1", width = 5, command = lambda:show("1")).grid(row = 4, column = 2)
tk.Button(win, text = "+", width = 5, command = lambda:show("+")).grid(row = 4, column = 3)
tk.Button(win, text = "0", width = 12, command = lambda:show("0")).grid(row = 5, column = 0, columnspan = 2)
tk.Button(win, text = ".", width = 5, command = lambda:show(".")).grid(row = 5, column = 2)
tk.Button(win, text = "=", width = 5, command = lambda:calculate()).grid(row = 5, column = 3)

win.mainloop()
