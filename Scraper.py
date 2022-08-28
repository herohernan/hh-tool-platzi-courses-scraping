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
    print(str(i+1) + '. ' + categoryName)

    # schools
    schools = category.find_all('div',class_='School')
    for j, school in enumerate(schools):
        schoolName = school.find('h3').getText()   
        print("  " + str(i+1) + '.' + str(j+1) + '. ' + schoolName)

        # courses
        courses = school.find_all('a',class_='Course')
        for k, course in enumerate(courses):
            courseName = course.find('h4').getText()
            print("    " + str(i+1) + '.' + str(j+1) + '.' + str(k+1) + '. ' + courseName)