# 攝氏華氏溫度轉換
# 公式：攝氏*1.8 = 華氏-32
print("溫度轉換工具!!")
print("要「攝氏」轉「華氏」請按 ==> 1\n要「華氏」轉「攝氏」請按 ==> 2")
CF = int(input("請輸入："))
# [round]函數控制小數點四捨五入到第幾位
if CF == 1 :
    C = float(input("請輸入攝氏溫度："))
    c = float(C*1.8+32)
    print("華氏溫度為：",round(c,1),"°F")
elif CF == 2 :
    F = float(input("請輸入華氏溫度："))
    f = float((F-35)/1.8)
    print("攝氏溫度為：",round(f,1),"°C")
else :
    print("輸入錯誤代號！！！")