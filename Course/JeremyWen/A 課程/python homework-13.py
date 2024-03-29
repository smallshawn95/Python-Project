# 找出五個數中最大值
def arrayMax(shawn) :
    shawn = max(shawn)
    print('-'*30)
    print('五個數中最大的數 --> {}'.format(shawn))

print('輸入五個數字，本程式將列出最大值OUO\n(心理OS:其實你們自己算不就知道了)')
a = float(input('第一個數字：'))
b = float(input('第二個數字：'))
c = float(input('第三個數字：'))
d = float(input('第四個數字：'))
e = float(input('第五個數字：'))
shawn = [a,b,c,d,e]
arrayMax(shawn)