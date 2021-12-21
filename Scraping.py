import requests
import pandas as pd 
from bs4 import BeautifulSoup 

url = 'https://news.yahoo.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id="YDC-Stream")
job_elements = results.find_all("li", class_="js-stream-content Pos(r)")

a= []
for job_element in job_elements:
    title_element = job_element.find("h3")
    a.append(title_element.text.strip())

yahoo_news = pd.DataFrame(a,columns=['Titles'])
yahoo_news.to_csv('yahoo_news.csv' , index = False)



def keyword(tag):
    result = soup.find_all("a" ,string=lambda text: tag in str(text).lower())
    a=0
    for i in result:
        a+=1
        print(i.text)
        

while True:
    try:
        tag = input("tag? or exit ")
        if tag.lower() == exit:
            break
        else:
            keyword(tag)
    except:
        print("some thing is wrong")
        pass
    else:
        break
