import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://wiki.biligame.com/dwrg/%E8%A7%92%E8%89%B2")
time.sleep(2)

data = {
    "求生者": {},
    "監管者": {}
}

num = True
table_button = driver.find_element(By.CLASS_NAME, "wikitable")
table_button_trs = table_button.find_elements(By.TAG_NAME, "tr")
for li in table_button_trs[-1].find_elements(By.TAG_NAME, "li"):
    li.click()
    time.sleep(2)
    table_role = driver.find_element(By.ID, "CardSelectTr")
    table_role_trs = table_role.find_elements(By.TAG_NAME, "tr")
    del table_role_trs[0]
    for tr in table_role_trs:
        tds = tr.find_elements(By.TAG_NAME, "td")
        name = tds[1].text
        url = tds[1].find_element(By.TAG_NAME, "a").get_attribute("href")
        if name == "":
            continue
        if num:
            type_name = "求生者"
        else:
            type_name = "監管者"
        data[type_name][name] = url
    num = False
    li.click()
    time.sleep(2)

with open("./IdentityV/wiki.json", "w", encoding = "utf8") as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)

driver.quit()
