# 找出最大公因數
print("輸入兩個數字找出最大公因數!!")

def gcd(a,b) :
    return a if b==0 else gcd(b,a%b)

#[gcd]函數是計算最大公因數
a = int(input("X："))
b = int(input("Y："))
print("Gcd:",gcd(a,b))