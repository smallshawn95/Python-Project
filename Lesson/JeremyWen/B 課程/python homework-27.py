import random

print('歡迎遊玩"Bulls and Cows"遊戲OWO')
print('是一款益智遊戲，接下來該展現您真正的實力了')
print('遊戲規則：\n輸入四個不一樣的數字，會告訴您幾A幾B\
\nA代表數字位置都正確，B代表數字正確但位置不正確')
print('遊戲開始OAO')
print('-'*50)

shawn = 0
wrong = 1
computer_number = list(random.sample('123456789',4))
while shawn == 0 :
    player_number = list(input('請輸入數字：'))
    A = 0
    B = 0
    if len(player_number) == 4 :
        for ans in range(4) :
            if player_number[ans] == computer_number[ans] : 
                A += 1
            else :
                for ans_ in range(4) :
                    if player_number[ans_] == computer_number[ans] :
                        B += 1
    else :
        print('輸入錯誤數字位數!!!')
        continue  
    if A < 4 :
        print('{}A{}B'.format(A,B))
        wrong += 1
    else :
        print('4A0B')
        print('-'*30)
        print('恭喜您猜對OWO，您總共猜了{}次'.format(wrong))
        break