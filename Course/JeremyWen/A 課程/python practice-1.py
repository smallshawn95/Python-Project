# 判斷奇數或偶數
for t in range(5):
    print("第",t+1,"次")
    a=int(input("請輸入:"))
    print(type(a))

    if a % 2 == 0 :
        print("偶數(even)")
    else:
        print("奇數(odd)")