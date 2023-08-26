'''
Jessica Wen
Colgate summer research 2023
use this before divide_numpy 
sort the mod3_love.mod file to be the same as mod3.mod file, so the format is the same before 
calculating radial anisotropy ratios
order of file is long lat depth velocity
                -145   51 10-500
                -145.5 51 10-500
                ...
                -168    51 10-500
                -145 51.5 10-500
                ...
                168    65  10-500
'''
import pandas as pd

df = pd.read_csv("mod3_lovezeros.mod", delimiter = r"\s+", names = ('Long', 'Lat', 'Depth', 'Velocity'))

long_max = df['Long'].max() #-145
long_min = df['Long'].min() #-168

lat_min = df['Lat'].min() #51
lat_max = df['Lat'].max() #65

long = long_max
long_lst = [] #list to hold sorted lines
while long >= long_min: #sort longitude
    for i in range(len(df)):
        if df['Long'][i] == long:
            long_lst.append(([df['Long'][i], df['Lat'][i], df['Depth'][i], df['Velocity'][i]])) #add line to list
    long -= 0.5
long_df = pd.DataFrame(long_lst, columns =['Long', 'Lat', 'Depth', 'Velocity']) #convert list with sorted lines into dataframe

lat = lat_min
lat_lst = [] #list to hold sorted lines
while lat <= lat_max: # sort latitude from the sorted longitude df
    for i in range(len(long_df)):
        if long_df['Lat'][i] == lat:
            lat_lst.append(([long_df['Long'][i], long_df['Lat'][i], long_df['Depth'][i], long_df['Velocity'][i]]))
    lat += 0.5
lat_df = pd.DataFrame(lat_lst, columns =['Long', 'Lat', 'Depth', 'Velocity'])

lat_df.to_csv('love_sort_test.csv', index = False, header = False) #export to csv