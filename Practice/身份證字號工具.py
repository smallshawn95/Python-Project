import random

Taiwan_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Taiwan_number = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,
               'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
Taiwan_city = {'A':'台北市','B':'台中市','C':'基隆市','D':'台南市','E':'高雄市','F':'台北縣','G':'宜蘭縣','H':'桃園市',
               'I':'嘉義市','J':'新竹縣','K':'苗栗縣','L':'台中縣','M':'南投縣','N':'彰化縣','O':'新竹市','P':'雲林縣',
               'Q':'嘉義縣','R':'台南縣','S':'高雄縣','T':'屏東縣','U':'花蓮縣','V':'台東縣','W':'金門縣','X':'澎湖縣','Y':'陽明山','Z':'連江縣'}

def tool_1() :
    letter = random.choice(Taiwan_letter)
    city_number = str(Taiwan_number.get(letter))
    city_letter = str(Taiwan_city.get(letter))
    number = str(random.randint(1,2))
    if number == '1' :
        gender = '男'
    elif number == '2' :
        gender = '女'
    else :
        gender = 'None'
    for a in range(7):
        number += str(random.randint(0,9))
    ID = city_number + number
    ans = (int(ID[0])+int(ID[1])*9+int(ID[2])*8+int(ID[3])*7+int(ID[4])*6+int(ID[5])*5+int(ID[6])*4+int(ID[7])*3+int(ID[8])*2+int(ID[9]))%10
    ID = letter + number + str(10 - ans)
    print('產生的身分證字號 --> {}'.format(ID))
    print("出生戶籍地 --> {0}\n性別 --> {1}".format(city_letter,gender))
    print('產生出來的身分證字號請勿拿來使用030')

def tool_2() :
    ID = input('請輸入身分證字號：')
    city_number = str(Taiwan_number.get(ID[0]))
    ans = (int(city_number[0])+int(city_number[1])*9+int(ID[1])*8+int(ID[2])*7+int(ID[3])*6
          +int(ID[4])*5+int(ID[5])*4+int(ID[6])*3+int(ID[7])*2+int(ID[8])+int(ID[9]))%10
    if ans == 0 :
        print('--> 身分證字號正確OUO')
    else :
        print('--> 身分證字號錯誤OUO')

def tool_3() :
    ID = input('請輸入身分證字號：')
    city_letter = Taiwan_city.get(ID[0])
    if ID[1] == '1' :
        gender = '男'
    elif ID[1] == '2' :
        gender = '女'
    else :
        gender = 'None'
    print("出生戶籍地 --> {0}\n性別 --> {1}".format(city_letter,gender))

print('身分證字號工具OWO')
print('【a】隨機產生【b】判斷是非【c】查詢資訊')
shawn = input('請輸入代號：')
_ = '-'*30
if shawn == 'a' :
    print(_)
    tool_1()
elif shawn == 'b' :
    print(_)
    tool_2()
elif shawn == 'c' :
    print(_)
    tool_3()
else :
    print('輸入錯誤代號～～')
