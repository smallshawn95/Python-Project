import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'")

driver = webdriver.Chrome(options = options)
# 檢測反爬蟲的網站
driver.get("https://bot.sannysoft.com/")
time.sleep(5)

driver.quit()
