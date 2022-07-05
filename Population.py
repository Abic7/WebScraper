
 
from bs4 import BeautifulSoup
import pandas as pd
import pathlib as pl
import numpy as np
from urllib.request import Request,urlopen

req2=Request('https://worldpopulationreview.com/countries',headers={'User-Agent':'Chrome/101.0.4951.64'})
webpage1=urlopen(req2).read()

soup1=BeautifulSoup(webpage1,'html')

#Country Data
country_name_html1=[i for i in soup1.find_all(class_='md-crosslink')]
country_name1=list()
for i in range (len(country_name_html1)):country_name1.append(country_name_html1[i].text)
print(country_name1)

countrydict1={'country':country_name1}
print(countrydict1)

countrydf1=pd.DataFrame.from_dict(countrydict1)
countrydf1.to_csv('country.csv')
read=pd.read_csv('country.csv')
print('Reading data from csv file')
print(read)
#End Country Data

# Population Data
population_html1=[i for i in soup1.find_all(class_='jsx-2006211681')]
population1=list()
for i in range (len(population_html1)): population1.append(population_html1[i].text)
print(population1)

populationdict1={'population':population1}
print(populationdict1)

populationdf1=pd.DataFrame.from_dict(populationdict1)
populationdf1.to_csv('population.csv')
read=pd.read_csv('population.csv')
print('Reading data from csv file')
print(read)
# End population data

"""



# Testing

from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import Request,urlopen

webpage1 = requests.get('https://worldpopulationreview.com/countries').text

soup1=BeautifulSoup(webpage1,'html')

population_html1=[i for i in soup1.find_all(class_='jsx-2006211681')]
population1=list()
for i in range (len(population_html1)): population1.append(population_html1[i].text)
#print(population1)

for item in population1:
 #split the element string into a list of words
 itemWords = item.split('%')
 #extend newlist to include all itemWords
 population1.extend(itemWords)
print(population1)



#populationdict1={'population':population1}
#print(populationdict1)



""" 
webpage = requests.get('https://worldpopulationreview.com/countries').text
#print(f)

soup1=BeautifulSoup(webpage,'html.parser')
#print(soup1.prettify())

print(soup1.p('column is-12 is-clearfix py-6'))
 """
""" 
for manga in soup1.select('.line'):
    title = manga.select('jsx-2006211681')
    for t in title:
        print(t.text)
 """
# for manga in soup1.select('.line'):
 #   title = manga.select('.jsx-2006211681 a')
 #   for t in title:
  #      print(t.text) 
#
# for i in manga.findAll('href="/countries/', class_='jsx-2006211681'):
   #     img = i['src']
    #    print(img) 
    #    """
   # """ for l in manga.findAll('p', class_='manga-list-1-item-title'):
    #    link = l.a['href']
   #     link = link[1:]
    #    print(f'http://fanfox.net/{link}') """


#for a in soup1.findAll(attrs={'class':'jsx-2006211681'}):name=a.find('%', attrs={'class':'jsx-2006211681'})



#print(soup1.get_text())

#for i in soup1.findAll('tbody',{'class':'jsx-2006211681'}):print((i.find('span',{'class':'text'})).text)



#req2=Request('https://worldpopulationreview.com/countries',headers={'User-Agent':'Chrome/101.0.4951.64'})
#webpage1=urlopen(req2).read()

#soup1=BeautifulSoup(webpage1,'html')

#population_html1=[i for i in soup1.find_all(class_='jsx-2006211681')]

#population1=list()
#for i in range (len(population_html1)): population1.append(population_html1[i].text)
#print(population1) 



#mylist=[population1]
#mylist=list(mylist['%'])
#print(mylist)





#DICTIONRY - Storing the output of population1 into a variable(mydict1) to write into a file
#mydict1={'data': population1}
#file=open("population.txt","w")
#str_dict1=repr(mydict1)
#print(mydict1)
#print(str_dict1)

#DATAFRAME -  creating a dataframe to format the data based on %

#populationdf1=pd.DataFrame.from_dict(mydict1,orient='index',
#                                                columns=['Rank','Country',  '2022 Population',  '2021 Population',  'Growth Rate',  'Area' , 'Density (km²)'])
#print(populationdf1)
#dfsplit=populationdf1.['country'].str.split('%',1)
#print(dfsplit)

#file.write("mydict1 = " + str_dict1 + "\n") #"\n" creates newline for next write to file.
#file.close()


#populationdict1={'population':population1}
"""print(populationdict1)

populationdf1=pd.DataFrame.from_dict(populationdict1)
populationdf1.to_csv('population.csv')
read=pd.read_csv('population.csv')
print('Reading data from csv file')
print(read) """

#--words = population_html1.split(",") 
#--print(words)

#spliting population data into appropiate columns so it is in seperate rows and columns

# actual code populationdf1=pd.DataFrame.from_dict(populationdict1)

#df_out = df.explode(populationdf1)
#print(df_out)

#dfsplit=df5.['country'].str.split('.)',1)

#populationdfsplit1 = populationdf1.['countryname'].str.split('.)',1)

#populationdfsplit1=pd.DataFrame.(population1.['countryname'].str.split('.)'),1)