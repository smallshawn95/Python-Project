import time, json, requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

with open("./IdentityV/wiki.json", "r", encoding = "utf8") as file:
    data = json.load(file)

for type_name in ["求生者", "監管者"]:
    for role_name in data[type_name]:
        driver.get(data[type_name][role_name])
        time.sleep(2)
        image_url = driver.find_element(By.XPATH, "//div[@class='poke-bg']//img").get_attribute("src")
        with open(f"./IdentityV/picture/{type_name}/{role_name}.png", "wb") as file:
            file.write(requests.get(image_url).content)
