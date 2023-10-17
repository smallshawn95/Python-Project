import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.identityvgame.com/tw/character/index.html?type=survivors")
time.sleep(2)

data = {
    "求生者": {},
    "監管者": {}
}

num = True
type_buttons = driver.find_elements(By.XPATH, "//div[@class='types']//a")
for type_button in type_buttons:
    type_button.click()
    images = driver.find_elements(By.XPATH, "//div[@class='img']/img")
    next_button = driver.find_element(By.XPATH, "//a[@class='btnRight']")
    sum_page_num = int(driver.find_element(By.XPATH, "//span[@class='sumPage']").text)
    for i in range(sum_page_num):
        time.sleep(2)
        name = driver.find_element(By.XPATH, "//h2[@class='roleName']").text
        name = name.replace("“", "\"")
        name = name.replace("”", "\"")
        alias = driver.find_element(By.XPATH, "//h5[@class='alias']").text.split("：")[1]
        story = driver.find_element(By.XPATH, "//div[@class='bgstory']").text
        story = story.replace("“", "\"")
        story = story.replace("”", "\"")
        setting = driver.find_elements(By.XPATH, "//ul[@class='settings']//li")
        avatar_url = images[i].get_attribute("src")
        if num:
            type_name = "監管者"
        else:
            type_name = "求生者"
        data[type_name][name] = {
            "姓名": alias,
            "故事背景": story,
            "紀念日": setting[0].text.split("：")[1],
            "興趣": setting[1].text.split("：")[1],
            "擅長": setting[2].text.split("：")[1],
            "喜歡": setting[3].text.split("：")[1],
            "頭像": avatar_url
        }
        if i == sum_page_num - 1:
            num = False
            break
        next_button.click()

with open("./IdentityV/role.json", "w", encoding = "utf8") as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)

driver.quit()
