# 單位轉換工具
def a(_) :
    print('要「公分」轉「英吋」請按 ==> 1\n要「英吋」轉「公分」請按 ==> 2')
    long = input('請輸入：')
    print(_)
    if long == '1' :
        centimeter = float(input("請輸入公分："))
        cm = round(centimeter/2.54,2)
        print('等於 {0}英吋'.format(cm))
    elif long == '2' :
        inch = float(input('請輸入英吋：'))
        in_ = round(inch*2.54,2)
        print('等於 {0}公分'.format(in_))
    else :
        print('輸入錯誤代碼ＱＱ')    

def b(_) :
    print('要「攝氏」轉「華氏」請按 ==> 1\n要「華氏」轉「攝氏」請按 ==> 2')
    CF = input('請輸入：')
    print(_)
    if CF == '1' :
        C = float(input('請輸入攝氏溫度：'))
        c = round(C*1.8+32,1)
        print('華氏溫度為{}°F'.format(c))
    elif CF == '2' :
        F = float(input('請輸入華氏溫度：'))
        f = round((F-35)/1.8,1)
        print('攝氏溫度為{0}°C'.format(f))
    else :
        print('輸入錯誤代號ＱＱ')

def c(_) :
    print('計程車費率計算(不包含延滯時間計費)')
    print('▶ 等於或少於1.25公里 --> 70元')
    print('▶ 每多0.2公里 --> +5元')
    m = float(input('請輸入里程數(公里)：'))*1000
    money = ((m-1250)//200)*5+75
    print(_)
    if m <= 1250 :
        print('此趟費用為70.0元030')
    else :
        print('此趟費用為{0}元030'.format(money))
     
print('單位換算小工具030')
print('【a】長度轉換【b】溫度轉換【c】計程車費率')
_ = '-'*30
abc = input('請輸入代碼：')
print(_)
if abc == 'a' :
    a(_)
elif abc == 'b' :
    b(_)
elif abc == 'c' :
    c(_)
else :
    print('輸入錯誤代碼ＱＱ')