import tkinter as tk

win = tk.Tk()
win.title('Label')
win.geometry('300x150')

#建立標籤
lb = tk.Label(text = 'I am Shawn 030')
#fg 文字顏色 bg 背景顏色
lb.config(foreground = 'Blue',background = 'Pink' )
#height 高度 width 寬度
lb.config(height = 80,width = 100)
#文字輸出換行(像素)
lb.config(wraplength = 55)
#文字和標籤間距(padx左右 pady上下)
lb.config(padx = 5,pady = 10)
#框框樣式
lb.config(relief = 'flat')
#增加位元圖
lb.config(bitmap = 'hourglass')
'''
#增加圖片
shawn = tk.PhotoImage(file = 'C:\程式語言\Python\Tkinter\成績判斷.png')
lb.config(image = shawn)
'''
#最後一行對齊位置(left/center/right)
lb.config(justify = 'center')
#圖像對文字的相對位置(left/right/top/bottom/center)
lb.config(compound = 'left')
#字型 字型大小(像素) bold/normal(粗體) italic/roman(斜體) underline(底線) overstrike(劃線)
lb.config(font='Helvetica 12 bold italic')
#文字對齊位置
#nw    n       ne
#w     center  e
#sw    s       se
lb.config(anchor = 'center')
lb.pack()

win.mainloop()
