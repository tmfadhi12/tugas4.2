
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import json

driver = webdriver.Firefox(executable_path="geckodriver")
driver.get("https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=99YW55CQ221HNXKV5Z3J&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2")

movielist = []
i = 1
j = 1
while i <= 100:
    for movie in driver.find_elements(By.XPATH, "//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr["+str(i)+"]"):
        # print(movie.text)
        i = i + 1
        for img in movie.find_elements(By.TAG_NAME, "img"):
            # print(img.get_attribute("src"))
            # urllib.request.urlretrieve(img.get_attribute("src"), str(j) + ".png")
            j = j + 1
            try:
                movielist.append({
                "Movie Title (Years Launched)": movie.text.split("\n")[0],
                "Velocity": movie.text.split("\n")[1],
                "Rating": movie.text.split("\n")[2],
                "Image": img.get_attribute("src")
            })
            except:
                movielist.append({
                "Movie Title (Years Launched)": movie.text.split("\n")[0],
                "Velocity": movie.text.split("\n")[1],
                "Rating": "",
                "Image": img.get_attribute("src")
            })

# print(movielist)

HasilJSON = json.dumps(movielist)
JSONFile = open("res.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
driver.quit()