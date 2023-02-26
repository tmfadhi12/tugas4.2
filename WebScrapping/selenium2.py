from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Firefox(executable_path="geckodriver")
driver.get("https://id.noxinfluencer.com/youtube-channel-rank/top-100-id-all-youtuber-sorted-by-subs-weekly")

ytList = []
temp = driver.find_element(By.XPATH, "//*[@id='table-body']").find_elements(By.CLASS_NAME, "table-line")
for i in temp:
    ytList.append({"img": i.find_element(By.CLASS_NAME, "rank-desc").find_element(By.CLASS_NAME, "avatar").get_attribute("src"),
                   "name": i.find_element(By.CLASS_NAME, "rank-desc").find_element(By.CLASS_NAME, "title").text.strip(),
                   "category": i.find_element(By.CLASS_NAME, "rank-category").find_element(By.CLASS_NAME, "category").text.strip(),
                   "subs": i.find_element(By.CLASS_NAME, "rank-subs").find_element(By.CLASS_NAME, "number").text.strip()
                   })
    
HasilJSON = json.dumps(ytList)
JSONFile = open("ytber.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
driver.quit()