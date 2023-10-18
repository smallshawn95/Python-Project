import random

number = int(random.randint(1,100))
print("1～100 猜一個數字！")
a = int(input("輸入數字："))
shawn = 1 ; wrong = 0
while shawn > 0 :
    if a > number :
        print("猜的數字太大!!")
        a = int(input("請再輸入一個數字："))
        shawn = 1
        wrong += 1
    elif a < number :
        print("猜的數字太小!!")
        a = int(input("請再輸入一個數字："))
        shawn = 1
        wrong += 1
    else:
        print("恭喜猜到了!!")
        print("總共猜錯",wrong,"次。")
        shawn = 0
        wrong = 0
    while shawn == 0:
        answer = input("再玩一次請按Y，結束遊戲請按N。\n輸入：")
        if answer == "N" or answer == "n" :
            print("感謝遊玩本遊戲～～")
            break
        elif answer == "Y" or answer == "y" :
            shawn = 1
            number = int(random.randint(1,100))
            print("1～100 猜一個數字！")
            a = int(input("輸入數字："))
