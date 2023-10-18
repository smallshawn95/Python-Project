print("輸入民國年份獲取當年十二生肖!!!")
year = int(input("請輸入："))
year -= 1
animal = year % 12
if animal == 0 :
    print("那一年是鼠年!!!")
elif animal == 1 :
    print("那一年是牛年!!!")
elif animal == 2 :
    print("那一年是虎年!!!")
elif animal == 3 :
    print("那一年是兔年!!!")
elif animal == 4 :
    print("那一年是龍年!!!")
elif animal == 5 :
    print("那一年是蛇年!!!")
elif animal == 6 :
    print("那一年是馬年!!!")
elif animal == 7 :
    print("那一年是羊年!!!")
elif animal == 8 :
    print("那一年是猴年!!!")
elif animal == 9 :
    print("那一年是雞年!!!")
elif animal == 10 :
    print("那一年是狗年!!!")
else :
    print("那一年是豬年!!!")