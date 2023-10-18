print("判斷輸入字元類別!!!")
ans = input("請輸入單一個字元：")
if ord(ans) >= ord("A") and ord(ans) <= ord("Z") :
    print("這是大寫字元!!!")
elif ord(ans) >= ord("a") and ord(ans) <= ord("z") :
    print("這是小寫字元!!!")
elif ord(ans) >= ord("0") and ord(ans) <= ord("9") :
    print("這是數字字元!!!")
else :
    print("這是特殊字元!!!")
# ord( )函數 --> 輸入字元，回傳對應的 Unicode 字元。
# Unicode --> 一種在電腦上使用的字元編碼，為每種語言中的每個字元設定了唯一的二進制編碼。