# 面積計算工具
import math

def graphics_a(_) :
    print(_)
    r = float(input('請輸入圓半徑：'))
    ans = round((r**2)*math.pi,4)
    print('圓面積為{0}'.format(ans))

def graphics_b(_) :
    print(_)
    s = float(input('請輸入三角形邊長：'))
    ans = round(((3**0.5)/4)*(s**2),4)
    print('正三角形的面積為{0}'.format(ans))

def graphics_c(_) :
    print(_)
    s = float(input('請輸入正四邊形邊長：'))
    ans = round(s**2,4)
    print('正四邊形的面積為{0}'.format(ans))

def graphics_d(_) :
    print(_)
    s = float(input('請輸入正五邊形邊長：'))
    ans = round((s**2/4)*(25+10*(5**0.5))**0.5,4) 
    #(5*(s**2))/(4*math.tan(math.pi/5)) 正五邊形面積公式
    print('正五邊形的面積為{0}'.format(ans))

def graphics_e(_) :
    print(_)
    n = int(input('請輸入是正幾邊形：'))
    s = float(input('請輸入邊長：'))
    number = str(n)
    number1 = str(chinese_number.get(number[0]))
    number2 = str(chinese_number.get(number[1]))
    ans = round((n*(s**2))/(4*math.tan(math.pi/n)),4)
    print('正{0}邊形的面積為{1}'.format(number1+number2,ans))

print('計算面積小工具!!!')
print('【a】圓形【b】正三角形\n【c】正四邊形【d】正五邊形【e】其他正多邊形')
ans_graphics = input('請輸入要計算面積的圖形代號：')
chinese_number = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九','0':'十'}
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