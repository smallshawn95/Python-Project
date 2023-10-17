class Banks():
    def __init__(self, username):        #初始化
        self.__name = username           #私有存款者姓名
        self.__balance = 0               #私有開戶金額
        self.bank__name = "Shawn Bank"   #公有銀行名稱
        self.__rate = 30                 #預設美金和新台幣的匯率
        self.__service_charge = 0.01     #換匯的服務費

    def save_money(self, money):         #設計存款方式
        self.__balance += money          #執行存款
        print(f"存款 {money} 完成")

    def withdraw_money(self, money):     #設計提款方式
        self.__balance -= money          #執行提款
        print(f"提款 {money} 完成")

    def get_balance(self):               #輸出存款餘額
        print(f"{self.__name.title()} 存款餘額：{self.__balance}")

    def usa_to_taiwan(self, USD):        #美金兌換新台幣
        self.result = self.__cal_rate(USD)
        return self.result

    def __cal_rate(self, USD):           #計算匯率公式(私有方法)
        return USD * self.__rate * (1 - self.__service_charge)

Shawn_bank = Banks("Shawn")              #定義物件
print("目前開戶銀行：" + Shawn_bank.bank__name)
Shawn_bank.get_balance()
Shawn_bank.save_money(1000)
Shawn_bank.get_balance()
Shawn_bank.withdraw_money(500)
Shawn_bank.get_balance()
USD = 50
print(USD, "美元可以兌換", Shawn_bank.usa_to_taiwan(USD), "新台幣")
