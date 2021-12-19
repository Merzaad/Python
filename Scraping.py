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
print(a)

#df = pd.DataFrame(a,columns=['Titles'])
#df.to_csv('zoomg.csv' , index = False)
