import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@YuYu_0103/videos")
time.sleep(1)

videos = driver.find_elements(By.XPATH, "//ytd-rich-item-renderer[@class='style-scope ytd-rich-grid-row']")
for video in videos:
    title = video.find_element(By.TAG_NAME, "h3").text
    image = video.find_element(By.TAG_NAME, "img").get_attribute("src")
    print(title, image)

driver.quit()
