import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'")

driver = webdriver.Chrome(options = options) 
# 檢測反爬蟲是否通過
driver.get("https://bot.sannysoft.com/")
time.sleep(3)
driver.get("https://www.wantgoo.com/stock/etf/00900")
time.sleep(10)

price_data = driver.find_element(By.XPATH, "//div[@class='quotes-info']").text.splitlines()
for data in price_data:
    print(data)

driver.quit()