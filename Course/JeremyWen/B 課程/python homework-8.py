# 輸入要顯示幾個費氏數列的數
print('費氏數列!!!')
n = int(input('請輸入正整數：'))
number_a = 0
number_b = 1
if n == 1 :
    print('0')
elif n == 2 :
    print('0 1')
else:
    print('0',end=' ')
    for x in range(n-1):
        ans = number_a+number_b
        print(ans,end=' ')
        number_b = number_a
        number_a = ans