
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.worldatlas.com/aatlas/ctycodes.htm'
response = requests.get(url) #get information from website
html = response.content #load inforamtion as string

soup = BeautifulSoup(html) #convert string to beautifulsoup format (required to parse html)
#soup = BeautifulSoup(response.text) 
table = soup.findAll('table') #there is only one table -> use Find. For multiple tables -> findAll (returns a list)
#table = soup.table
#there are 2x tables -> American League, National League 

#Can grab headers usign the following code
#head = table[0].find('thead')
#list_of_names = []
#for colnames in head.findAll('th'):
#    text = colnames.find(text=True)
#    list_of_names.append(text)

#Extract information from table
# NOTE: do not need to make reference to <tbody> tag within a table
list_of_names = ['country', 'a2', 'a3', 'num', 'dia' ]
total_list = []
for i in range(1):
    league = table[i]
    list_of_rows = []
    for rows in league.findAll('tr'):
        list_of_cells = []
        for element in rows.findAll('td'):
            text = element.find(text = True)
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    total_list.append(list_of_rows)

#Concatinate both elements of the list above and create a single dataframe using pandas
final =  total_list[0]

import pandas as pd
df = pd.DataFrame(final, columns = list_of_names)
#Save as a .csv for futher manupulation 
df.to_csv("./isocode.csv", sep=',')
