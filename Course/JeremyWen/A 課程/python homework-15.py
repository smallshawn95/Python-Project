# 身份證字號驗證
print('驗證身分證字號是否符合標準OWO\n【格式：大寫英文字母+9個數字】')
ID = input('請輸入身分證字號：')
Taiwan_city = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,
               'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
frist = str(Taiwan_city.get(ID[0]))
ans = (int(frist[0])+int(frist[1])*9+int(ID[1])*8+int(ID[2])*7+int(ID[3])*6
      +int(ID[4])*5+int(ID[5])*4+int(ID[6])*3+int(ID[7])*2+int(ID[8])+int(ID[9]))%10
print('-'*30)
if ans == 0 :
    print('{} 身分證字號正確OUO'.format(ID))
    print('身分證檢查碼為{}'.format(ID[9]))
else :
    print('{} 身分證字號錯誤OUO'.format(ID))