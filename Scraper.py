#!"C:\Python310\python3.exe"
from bs4 import BeautifulSoup
import requests
import pandas 

# Get the html content from a URL 
url = 'https://platzi.com/cursos/'
page = requests.get(url)
if(page.status_code != 200): 
    pass
soup = BeautifulSoup(page.content,'html.parser')
soup = soup.section

# Lists to append later on panda data frame
NumberOfCoursesFound = 0
categoryList = list()
schoolList = list()
courseList = list()

# categories
categories = soup.find_all('div',class_='Categories-item')
for i, category in enumerate(categories):
    categoryName = str(category.find('span').getText())
    print(str(i+1) + '. ' + categoryName)

    # schools
    schools = category.find_all('div',class_='School')
    for j, school in enumerate(schools):
        schoolName = str(school.find('h3').getText())
        print("  " + str(i+1) + '.' + str(j+1) + '. ' + schoolName)

        # courses
        courses = school.find_all('a',class_='Course')
        for k, course in enumerate(courses):
            courseName = str(course.find('h4').getText())
            print("    " + str(i+1) + '.' + str(j+1) + '.' + str(k+1) + '. ' + courseName)
            
            # append into the lists 
            NumberOfCoursesFound += 1
            categoryList.append(categoryName)
            schoolList.append(schoolName)
            courseList.append(courseName)
print('Number of courses found = ' + str(NumberOfCoursesFound))

# Create a panda data frame and append the data from lists
pandaDF = pandas.DataFrame({'category':categoryList, 
                            'schools':schoolList, 
                            'courses':courseList},
                            index=list(range(0,NumberOfCoursesFound)))

pandaDF.to_csv(r'ListOf_PlatziCourses.csv')