# 海龍公式 計算三角形面積
triangle = 0
print("計算三角形面積，請輸入三個邊長。")
while triangle == 0 or p <= 0 :
    a = float(input("第一邊："))
    b = float(input("第二邊："))
    c = float(input("第三邊："))
    s = 0.5*(a+b+c)
    p = s*(s-a)*(s-b)*(s-c)
    if p <= 0 :
        print("三角形不存在，請重輸入一遍！")
    triangle+=1
else:
    print("三角形面積為：",p**0.5) # **0.5 相當於開根號 