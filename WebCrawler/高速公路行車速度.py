import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://1968.freeway.gov.tw/n_speed")
time.sleep(5)

select = Select(driver.find_element(By.ID, "freeway"))
button = driver.find_element(By.XPATH, "//button[@class='button_ctrl go_btn']")
for option in select.options:
    if option.text == "請選擇國道":
        continue
    print(option.text)
    select.select_by_visible_text(option.text)
    button.click()
    time.sleep(2)
    table = driver.find_element(By.XPATH, "//table[@class='table_normal spd_table']")
    trs = table.find_elements(By.CLASS_NAME, "tbody")
    for tr in trs:
        print(tr.text)
    time.sleep(2)

driver.quit()
