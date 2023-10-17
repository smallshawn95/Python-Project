import random

shawn = [5,2,0,34,417]

#列表中隨機選一個資料
#random.choice(列表資料)
ans = random.choice(shawn)
print(ans)

#列表中隨機選n個資料
#random.sample(列表資料,n)
ans = random.sample(shawn,2)
print(ans)

#列表的資料隨機調換順序
#random.shuffle(列表資料)
ans = shawn
random.shuffle(ans)
print(ans)

#取得浮點數0.0~1.0之間的隨機亂數
#random.random()
#random.uniform(0.0,1.0)
ans = random.random()
print(ans)
ans = random.uniform(0.0,1.0)
print(ans)

#取得整數n~m之間的隨機亂數
#random.randint(n,m)
ans = random.randint(1,100)
print(ans)

#取的平均數n、標準差m的常態分配亂數，數字大多在【n-m】~【n+m】之間
#random.normalvariate(n,m)
ans = random.normalvariate(100,10)
print(ans)
