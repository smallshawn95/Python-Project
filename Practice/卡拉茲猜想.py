def yes(even,odd,number):
    while (number > 1):
        print(number,end = ' ')
        if number % 2 == 0:
            number = number // 2
            even += 1
        elif number % 2 == 1:
            number = number * 3 + 1
            odd += 1
    print('1')
    print('執行偶數步驟總共{}次'.format(even))
    print('執行奇數步驟總共{}次'.format(odd))

def no(even,odd,number):
    while (number > 1):
        if number % 2 == 0:
            number = number // 2
            even += 1
        elif number % 2 == 1:
            number = number * 3 + 1
            odd += 1
    print('執行偶數步驟總共{}次'.format(even))
    print('執行奇數步驟總共{}次'.format(odd))

_ = '-' ; even = 0 ; odd = 0
print('卡拉茲猜想OWO')
print('規則：\n輸入一個正整數，\n如果是奇數須乘以三加一，\n如果是偶數需除以二，\n如此循環，最後任何數都會變成一030')
print(_*30)
number = int(input('請輸入正整數：'))
ans = input('是否呈現過程中的數字(Y/N)：')
print(_*30)
if ans == 'Y' or ans == 'y' :
    yes(even,odd,number)
elif ans == 'N' or ans == 'n' :
    no(even,odd,number)
