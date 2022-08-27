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
soup = soup.section

# categories
categories = soup.find_all('div',class_='Categories-item')
for i, category in enumerate(categories):
    categoryName = category.find('span').getText()
    print(categoryName)

# schools
schools = soup.find_all('div',class_='School')
for i, school in enumerate(schools):
    schoolName = school.find('h3').getText()
    print(schoolName)

# courses
courses = soup.find_all('a',class_='Course')
for i, course in enumerate(courses):
    courseName = course.find('h4').getText()
    print(courseName)