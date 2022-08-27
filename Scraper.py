#!"C:\Python310\python3.exe"
from bs4 import BeautifulSoup
import requests
import pandas as pd 

# Get the html content from a URL 
url = 'https://platzi.com/cursos/'
page = requests.get(url)
if(page.status_code != 200): 
    pass
soup = BeautifulSoup(page.content,'html.parser')

# categories
soup = soup.section
categories = soup.find_all('div',class_='Categories-item')
for i, category in enumerate(categories):
    titulo = category.find('span').getText()
    print(titulo)



#soup = soup.attrs
#print(soup['id'])
#print(soup.next_sibling['id'])
#print(soup['id'])




#schoolsRaw = soup.find_all('h3')
#schools = list()
#for schoolRaw in schoolsRaw:  
#    schools.append(schoolRaw.text)
#print(schools)


