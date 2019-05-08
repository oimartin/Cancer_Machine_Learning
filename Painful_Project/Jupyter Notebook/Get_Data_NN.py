#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


state = "GA"
race = "Other Races and Unknown combined"
gender = "Male"
year = 2018.0

statelist = pd.Series(data=('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI','IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI','MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV','NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX','UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
racelist =pd.Series(data=("White", "Other Races and Unknown combined", "American Indian or Alaska Native", "Asian or Pacific Islander", "Black or African American"))     
genderlist =pd.Series(data=("Male", "Female"))
    


# In[3]:


state_dummies=pd.get_dummies(statelist)
race_dummies=pd.get_dummies(racelist)
gender_dummies=pd.get_dummies(genderlist)


# In[4]:


state_dummies_select = state_dummies[state].values
race_dummies_select = race_dummies[race].values
gender_dummies_select = gender_dummies[gender].values


# In[5]:


state_dummy = state_dummies_select.tolist()
race_dummy = race_dummies_select.tolist()
gender_dummy = gender_dummies_select.tolist()


# In[6]:


data_cancer = gender_dummy + race_dummy + state_dummy


# In[7]:


pollution_data = pd.read_csv("../Data/Data_for_Graphing/ARpollution.csv")
pollution_data_clean= pollution_data[["State", "Year", "CO", "Lead", "NO2", "Ozone", "PM10", "PM2_5", "SO2"]]


# In[8]:


data_poll = pollution_data_clean.loc[(pollution_data_clean['Year']==year) & (pollution_data_clean["State"]==state)]


# In[9]:


data_pollution_dropped = data_poll.drop(["State", "Year"], axis = 1)
data_pollution = data_pollution_dropped.values[0]
data_pollution_list = data_pollution.tolist()


# In[10]:


data = data_pollution_list + data_cancer


# In[12]:


data

