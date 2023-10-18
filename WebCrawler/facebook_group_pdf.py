#pip install selenium
#pip install webdriver_manager
#pip install pyautogui
#pip3 install beautifulsoup4
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui
import time

email = "Email"
password = "Password"

#防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
}
chrome_options.add_experimental_option("prefs", prefs)

#方法一
#開啟 chromedriver
#下載網址 https://sites.google.com/chromium.org/driver/
#driver = webdriver.Chrome("./chromedriver")

#方法二
#使用 ChromeDriverManager 自動開啟 chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)

#最大化視窗
driver.maximize_window()
#進入 Facebook 登入畫面
driver.get("https://www.facebook.com/")

#填入帳號密碼並送出
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.NAME, "login").click()
time.sleep(5)

driver.get("https://www.facebook.com/groups/946185189309101")
for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

root = BeautifulSoup(driver.page_source, "html.parser")

fileUrls = root.find_all("a", class_ = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1lliihq")
time.sleep(10)
pyautogui.hotkey("ctrl", "t", interval = 0.1)
driver.switch_to.window(driver.window_handles[1])
for data in fileUrls:
    url = data.get("href")
    driver.get(url)
    time.sleep(5)

#關閉瀏覽器
driver.quit()
