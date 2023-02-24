import requests
import json
from bs4 import BeautifulSoup as bs

URL = "https://food.detik.com/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")
news = soup.find(class_="section nhl").find(class_="list-content")

card = news.find_all(class_="ph_newsfeed_d")
result = []
for i in range(len(card)):
    try:
        result.append({"id":i+1, 
                       "subtitle": card[i].find("h2").text.strip(), 
                       "judul": card[i].find(class_="media__title").find("a", class_="media__link").getText().strip(), 
                       "date": card[i].find(class_="media__date").find("span").getText().strip()})
    except AttributeError:
        result.append({"id":i+1, 
                       "subtitle": "", 
                       "judul": card[i].find(class_="media__title").find("a", class_="media__link").getText().strip(), 
                       "date": card[i].find(class_="media__date").find("span").getText().strip()})
    
resultJSON = json.dumps(result)
JSONFile = open("Latest News.json", "w")
JSONFile.write(resultJSON)
JSONFile.close()