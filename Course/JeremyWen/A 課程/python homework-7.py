# 列出1000以內的費氏數列
print('列出1000以內的費氏數列OWO')
number_a = 0
number_b = 1
print(number_a,number_b,end=' ')
while number_a+number_b < 1000 :
    ans = number_a+number_b
    print(ans,end=' ')
    number_a = number_b
    number_b = ans