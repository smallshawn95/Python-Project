print('歡迎使用BMI計算工具＞～＜')
height = float(input("請輸入身高(公分)："))
weight = float(input("請輸入體重(公斤)："))
bmi = round(weight/(height/100)**2,1)
print("-"*20)
print("您的BMI值為{0}".format(bmi))
if bmi < 18.5 :
    print("過輕030")
elif bmi <= 18.5 or bmi < 24 :
    print("正常030")
elif bmi <=24 or bmi < 28 :
    print("超重030")
else :
    print("肥胖030")
print("-"*20)
print("BMI指數對照表：")
print("過輕：BMI < 18.5")
print("正常：BMI < 24  BMI >= 18.5")
print("超重：BMI < 28  BMI >= 24")
print("肥胖：BMI >= 28")