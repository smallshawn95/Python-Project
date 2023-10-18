import math

def graphics_a(_) :
    print(_)
    r = float(input('請輸入圓半徑：'))
    ans = (r**2)*math.pi
    print('圓面積為{:.4f}'.format(ans))

def graphics_b(_) :
    print(_)
    s = float(input('請輸入正三角形邊長：'))
    ans = ((3**0.5)/4)*(s**2)
    print('正三角形的面積為{:.4f}'.format(ans))

def graphics_c(_) :
    print(_)
    s = float(input('請輸入正四邊形邊長：'))
    ans = s**2
    print('正四邊形的面積為{:.4f}'.format(ans))

def graphics_d(_) :
    print(_)
    s = float(input('請輸入正五邊形邊長：'))
    ans = (s**2/4)*(25+10*(5**0.5))**0.5
    print('正五邊形的面積為{:.4f}'.format(ans))

def graphics_e(_) :
    print(_)
    n = int(input('請輸入是正幾邊形：'))
    s = float(input('請輸入邊長：'))
    if n < 10 :
        number = str(n)
        number1 = chinese_number.get(number[0])
        ans = (n*(s**2))/(4*math.tan(math.pi/n))
        print('正{}邊形的面積為{:.4f}'.format(number1,ans))
    elif n == 10 :
        ans = (n*(s**2))/(4*math.tan(math.pi/n))
        print('正十邊形的面積為{:.4f}'.format(ans))
    elif n >= 100 :
        print('目前只支援計算小於正一百邊形的面積OUO')
    else :
        number = str(n)
        number1 = str(chinese_number2.get(number[0]))
        number2 = str(chinese_number.get(number[1]))
        ans = (n*(s**2))/(4*math.tan(math.pi/n))
        print('正{}邊形的面積為{:.4f}'.format(number1+number2,ans))

print('計算面積小工具!!!')
print('【a】圓形【b】正三角形\n【c】正四邊形【d】正五邊形【e】其他正多邊形')
ans_graphics = input('請輸入要計算面積的圖形代號：')
chinese_number = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九','0':''}
chinese_number2 = {'1':'十','2':'二十','3':'三十','4':'四十','5':'五十','6':'六十','7':'七十','8':'八十','9':'九十'}
_ = '-'*30
if ans_graphics == 'a' :
    graphics_a(_)
elif ans_graphics == 'b' :
    graphics_b(_)
elif ans_graphics == 'c' :
    graphics_c(_)
elif ans_graphics == 'd' :
    graphics_d(_)
elif ans_graphics == 'e' :
    graphics_e(_)
else :
    print('輸入錯誤代號OUO')