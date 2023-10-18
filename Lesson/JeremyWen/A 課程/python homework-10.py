# 十進位轉二進位
print("輸入一個數字將會轉換成二進位制表示!!")
number = int(input("請輸入："))
answer = format(number, "b") 
# "b"是[format]函數中將數值轉換為二進位制的代號
print(answer)