from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import urllib.request

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://id.noxinfluencer.com/youtube-channel-rank/top-100-id-all-youtuber-sorted-by-subs-weekly")

ytList = []
j = 0
temp = driver.find_element(By.XPATH, "//*[@id='table-body']").find_elements(By.CLASS_NAME, "table-line")
for i in temp:
    for img in i.find_elements(By.TAG_NAME, "img"):
        # print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(j) + ".png")
        j = j + 1
        ytList.append({"img": img.get_attribute("src"),
                   "name": i.find_element(By.CLASS_NAME, "rank-desc").find_element(By.CLASS_NAME, "title").text.strip(),
                   "category": i.find_element(By.CLASS_NAME, "rank-category").find_element(By.CLASS_NAME, "category").text.strip(),
                   "subs": i.find_element(By.CLASS_NAME, "rank-subs").find_element(By.CLASS_NAME, "number").text.strip()
                   })
    
HasilJSON = json.dumps(ytList)
JSONFile = open("ytber.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
driver.quit()