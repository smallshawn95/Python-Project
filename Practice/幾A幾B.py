import random

print('歡迎遊玩"Bulls and Cows"OWO')
print('遊戲規則：\n輸入數字，會告訴您幾A幾B\
\n「A」代表數字位置都正確，「B」代表數字正確但位置不正確')
print('【a】二位數【b】三位數【c】四位數【d】更多位數')
x = input('請輸入要玩的代號：')
if x == 'a' :
    n = 2
elif x == 'b' :
    n = 3
elif x == 'c' :
    n = 4
elif x == 'd' :
    n = int(input('請輸入自訂位數：'))
shawn = 0
wrong = 1
computer_number = list(random.sample('123456789',n))
while shawn == 0 :
    player_number = list(input('請輸入數字：'))
    A = 0
    B = 0
    if len(player_number) == n :
        for ans in range(n) :
            if player_number[ans] == computer_number[ans] : 
                A += 1
            else :
                for ans_ in range(n) :
                    if player_number[ans_] == computer_number[ans] :
                        B += 1
    else :
        print('輸入錯誤數字位數!!!')
        continue  
    if A < n :
        print('{}A{}B'.format(A,B))
        wrong += 1
    else :
        print('{}A0B'.format(n))
        print('-'*30)
        print('恭喜您猜對OWO，您總共猜了{}次'.format(wrong))
        break