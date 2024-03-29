# 計算二元一次方程式的解
import cmath # 一個計算複雜數學的模組 
print("輸入a、b、c，算出x的兩個解。")
print("二元一次方程式：「ax**2+bx+c」")
a = float(input("輸入a:")) 
b = float(input("輸入b:")) 
c = float(input("輸入c:")) 
xyz = (b**2)-(4*a*c) 
ans1 = (-b-cmath.sqrt(xyz))/(2*a) 
ans2 = (-b+cmath.sqrt(xyz))/(2*a) 
print("兩個Ｘ解為{0}和{1}".format(ans1,ans2))