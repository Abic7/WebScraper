# -*- coding: utf-8 -*-
"""
Importing library's'
"""
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request,urlopen

"""
Using the Request library to read the webpage
More info : https://docs.python-requests.org/en/latest/
"""
req=Request('https://www.passportindex.org/byRank.php',headers={'User-Agent':'Chrome/101.0.4951.64'})
webpage=urlopen(req).read()
print(webpage)

"""
Using BeautifuSoup to export the country names
More Info : https://g.co/kgs/2aPhTm
"""
soup=BeautifulSoup(webpage,'html')
country_name_html=[i for i in soup.find_all(class_='name_country')]
country_name=list()
for i in range (len(country_name_html)):country_name.append(country_name_html[i].text)
print(country_name)

"""
Using BeautifuSoup to export the passport ranking
"""
passportrank_html=[i for i in soup.find_all(class_='name_rank')]
passportrank=list()
for i in range (len(passportrank_html)): passportrank.append(passportrank_html[i].text)
print(passportrank)

"""
Export Visa Free travel
"""
visafreetravel_html=[i for i in soup.find_all(class_='rank vf')]
viasfreetravel=list()
for i in range(len(visafreetravel_html)):viasfreetravel.append(visafreetravel_html[i].text)
print(viasfreetravel)

"""
Export Visa on arrival
"""
visaonarrival_html=[i for i in soup.find_all(class_='rank voa')]
visaonarrival=list()
for i in range(len(visaonarrival_html)):visaonarrival.append(visaonarrival_html[i].text)
print(visaonarrival)

"""
Export Visa required for travel
"""
visarequired_html=[i for i in soup.find_all(class_='rank vr')]
visarequired=list()
for i in range(len(visarequired_html)):visarequired.append(visarequired_html[i].text)
print(visarequired)

"""
Concatning all the data together using the dictionary function
"""
dict1={'country':country_name
       ,'passportrank':passportrank
       ,'viasfreetravel':viasfreetravel
       ,'visaonarrival':visaonarrival
       ,'visarequired':visarequired}
print(dict1)

"""
Formatting the exported data into dataframe
"""
df=pd.DataFrame.from_dict(dict1)


"""
Printing the data to a csv file
"""
df.to_csv('country.csv')

"""
read scraped data from CSV file
"""
read=pd.read_csv('country.csv')

print('Reading data from csv file')

"""
Viewing the file
"""
print(read)










