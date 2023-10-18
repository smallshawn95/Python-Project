# 公式：攝氏*1.8 = 華氏-32
print("溫度轉換工具!!")
print("要「攝氏」轉「華氏」請按 ==> 1\n要「華氏」轉「攝氏」請按 ==> 2")
CF = input("請輸入：")
if CF == '1' :
    C = float(input("請輸入攝氏溫度："))
    c = round(C*1.8+32,1)
    print("華氏溫度為{}°F".format(c))
elif CF == '2' :
    F = float(input("請輸入華氏溫度："))
    f = round((F-35)/1.8,1)
    print("攝氏溫度為{0}°C".format(f))
else :
    print("輸入錯誤代號！！！")
# round( )函數 --> 控制小數點四捨五入到第幾位