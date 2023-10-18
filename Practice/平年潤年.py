print("輸入年份可判斷是否為潤年!!!")
year = int(input("請輸入年份："))
a = year % 4
b = year % 100
c = year % 400
if a == 0 :
    if b != 0 or c == 0 :
        print("輸入的年份是潤年喔OWO")
    else :
       print("輸入的年份不是潤年喔OWO")  
else :
    print("輸入的年份不是潤年喔OWO") 