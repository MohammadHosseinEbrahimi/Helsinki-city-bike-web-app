# -*- coding: utf-8 -*-
"""
Written by Mohammadhossein Ebrahimi
17 July 2022
"""

#importing the modules
import pandas as pd

    #Validating the file
def read_file():
    #df = pd.read_csv('2021-05.csv')
    df = pd.read_csv('https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv')
    Address = pd.read_csv('https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv')
    if(df.empty):
        print ('CSV file is empty')
    else:
        print ('CSV file is not empty')
    return df


#Reading the data
data=read_file()


#Cleaning the data by Removing non-reasonable data points
#'Covered distance (m)' is positive
data=data[data['Duration (sec.)']>0]
#Removing 'Covered distance (m)' that are so big that does not make sense
data=data[data['Covered distance (m)']<1e5]
#removing less than 10 sec or less tahn 10 meter
data=data[data['Duration (sec.)']>10]
#removing less than 10 meter
data=data[data['Covered distance (m)']>10]
#removing dublicates in the data
data=data.drop_duplicates(keep='first')
#resetting the index
data.reset_index(drop=True)

#Journey list view, from 0 to 1000
import codecs
Journeyy = data[0:1000]
#resetting the index
Journeyy.reset_index(inplace=True, drop=True)
#getting the relevant columns
Journey=Journeyy[['Departure station name','Return station name', 
                  'Covered distance (m)','Duration (sec.)']]
#coverting to km and minutes
Journey['Covered distance (m)']=Journey['Covered distance (m)']/1000
Journey['Duration (sec.)']=Journey['Duration (sec.)']/60
Journey.rename(columns = {'Covered distance (m)':'Covered distance (km)', 
                          'Duration (sec.)':'Duration (min.)'}, inplace = True)
#wrting an html file
html_jor = Journey.to_html()
text_file = codecs.open("part1.html", "w","utf-8")
text_file.write(html_jor)
text_file.close()


#Station list
Station_Adress = Address [['Nimi', 'Osoite']]
html = Station_Adress.to_html()
text_file = codecs.open("part2.html", "w","utf-8")
text_file.write(html)
text_file.close()

#Single station view,Station name, Station address
#Total number of journeys starting from the station
#Total number of journeys ending at the station 
import numpy as np
#e=np.count_nonzero(Station["Departure station name"][0]==data["Departure station name"])
i = 0
a={}
e={}
f={}
g={}
h={}
k={}
l={}
for s in Address ['Nimi']:
    a[s]=Address ['Osoite'][i]
    e[s]=np.count_nonzero(Address ['Nimi'][i]==data["Departure station name"])
    f[s]=np.count_nonzero(Address ['Nimi'][i]==data["Return station name"])
    g[s]=np.mean(data[Address ['Nimi'][i]==data["Departure station name"]]['Covered distance (m)']) #newly added, modify below
    h[s]=np.mean(data[Address ['Nimi'][i]==data["Return station name"]]['Covered distance (m)'])
    k[s]= list(data[Address ['Nimi'][i]==data["Departure station name"]]['Return station name'].value_counts()[0:5].index)
    l[s]= list(data[Address ['Nimi'][i]==data["Return station name"]]['Departure station name'].value_counts()[0:5].index)
    i += 1

q=pd.DataFrame([a, e, f, g,h,k,l])
Single_station_view=pd.DataFrame.transpose(q)
Single_station_view.columns=['Address', 'Total number of journeys starting from the station',
            'Total number of journeys ending at the station',
            'The average distance of a journey starting from the station',
            'The average distance of a journey ending at the station',
            'Top 5 most popular return stations for journeys starting from the station',
            'Top 5 most popular departure stations for journeys ending at the station']
html = Single_station_view.to_html()
text_file = codecs.open("part3.html", "w","utf-8")
text_file.write(html)
text_file.close()

