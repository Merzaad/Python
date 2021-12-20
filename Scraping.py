import requests
import pandas as pd 
from bs4 import BeautifulSoup 

url = 'https://news.yahoo.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id="YDC-Stream")
job_elements = results.find_all("div", class_="Cf")

a= []
for job_element in job_elements:
    title_element = job_element.find("h3")
    a.append(title_element.text.strip())

yahoo_news = pd.DataFrame(a,columns=['Titles'])
yahoo_news.to_csv('yahoo_news.csv' , index = False)


corona = results.find_all(
    "h3", string=lambda text: "corona" in str(text).lower()
)

for i in corona:
    i.find_all("h3")
    print(i.text)
