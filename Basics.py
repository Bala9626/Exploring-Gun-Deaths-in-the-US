
# coding: utf-8

# In[1]:

import csv
data = list(csv.reader(open("guns.csv", 'r')))
data[0:5]


# In[2]:

headers = data[0]
headers


# In[3]:

data.remove(headers)
data[0:5]


# In[4]:

years = [row[1] for row in data]
year_counts = {}
for row in data:
    year = row[1]
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
year_counts


# In[5]:

import datetime
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
dates[0:5]                           


# In[6]:

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
date_counts


# In[7]:

sex_counts = {}
for row in data:
    sex = row[5]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
sex_counts


# From the **sex_counts** dictionary, it is clear that number of Male victims is very greater than that of female victims

# In[9]:

race_counts = {}
for row in data:
    race = row[7]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
race_counts


# **race_counts** dictionary depicts that Hispanic race victims are more than any other race, followed by White. And the race with least number victims is Native American/Native Alaskan

# In[10]:

census = list(csv.reader(open("census.csv", 'r')))
census


# In[22]:

mapping = {}
mapping['Asian/Pacific Islander'] = int(census[1][14]) + int(census[1][15])
mapping['Black'] = int(census[1][12])
mapping['Native American/Native Alaskan'] = int(census[1][13])
mapping['Hispanic'] = int(census[1][11])
mapping['White'] = int(census[1][10])
mapping


# In[23]:

race_per_hundredk = {}
for race,victims in race_counts.items():
    race_per_hundredk[race] = (victims/mapping[race])*100000
race_per_hundredk


# In[32]:

intents = [row[3] for row in data]


# In[33]:

races = [row[7] for row in data]


# In[34]:

homicide_race_per_hundredk = {}
for i,race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race] += 1
        else:
            homicide_race_per_hundredk[race] = 1


# In[31]:

for race,victims in homicide_race_per_hundredk.items():
    homicide_race_per_hundredk[race] = (victims/mapping[race])*100000
homicide_race_per_hundredk


# ##**Observations**:
#  - From the above dictionary, it is clear the race that faced more homicide gun deaths is **Black**
#  - After Black, **Hispanic** have the more homicide gun deaths
#  - As taken for the gender point of view, Male victims are more as compared with female victims
#  
# ##**Conclusion**:
#  - These observations are drawn just from race, gender and only one type of intent that is Homicide
#  - More detailed results can be obtained when **place** and **education** factors are taken into consideration
#  - Also we can make use of other intents to get bigger view of gun deaths
#     

# In[ ]:



