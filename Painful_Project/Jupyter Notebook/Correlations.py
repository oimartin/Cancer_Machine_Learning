#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


cancertype = "Larynx"
pollution = "CO"
state = "IL"


# In[3]:


cancer_new = pd.read_csv("../Data/Data_for_Graphing/ARcancer.csv")
cancer_old = pd.read_csv("../Data/cancer.csv")
pollution_new = pd.read_csv("../Data/Data_for_Graphing/ARpollution.csv")
pollution_old = pd.read_csv("../Data/pollution.csv")


# In[4]:


cancer_new_clean = cancer_new.drop('Unnamed: 0', axis =1)
cancer_new_clean = cancer_new_clean.replace("NaN", 0)

cancer_new_clean


# In[5]:


cancer_old_clean = cancer_old.drop(['Unnamed: 0', "States Code", "Year Code", "Race Code", "Cancer Sites Code", 'Count', "Population"], axis=1)
cancer_old_clean=cancer_old_clean.replace("Lung and Bronchus", "Lung")
cancer_old_clean=cancer_old_clean.replace("Nose, Nasal Cavity and Middle Ear", "Nasal")
cancer_old_clean=cancer_old_clean.replace("Trachea, Mediastinum and Other Respiratory Organs", "Trachea")
cancer_old_clean = cancer_old_clean.replace("Not applicable", 0)
cancer_old_clean["Crude Rate"] = pd.to_numeric(cancer_old_clean["Crude Rate"], errors='coerce')

cancer_old_clean


# In[6]:


pollution_new_clean= pollution_new.drop('Unnamed: 0', axis =1)


# In[7]:


pollution_old_clean = pollution_old.drop(['Unnamed: 0', 'County Code'], axis =1)


# In[8]:


years_old = cancer_old_clean["Year"].unique()
years_new = cancer_new_clean["Year"].unique()


# In[9]:


cancer_old_rates = []
for year in years_old:
    rate = cancer_old_clean.loc[(cancer_old_clean["Cancer Sites"]==cancertype) & (cancer_old_clean["State"]==state)&(cancer_old_clean["Year"]==year)]["Crude Rate"].sum()
                                                                                                                                                
    cancer_old_rates.append(rate)                                                                      
                                                                                                                                                
                                                                          


# In[10]:


cancer_new_rates = []
for year in years_new:
    rate = cancer_new_clean.loc[(cancer_new_clean["Cancer"]==cancertype)&(cancer_new_clean["State"]==state)&(cancer_new_clean["Year"]==year)][cancertype].sum() 
    cancer_new_rates.append(rate)


# In[11]:


poll_old = pollution_old_clean.loc[(pollution_old_clean["State"]==state)][pollution]
poll_new = pollution_new_clean.loc[(pollution_new_clean["State"]==state)][pollution]


# In[12]:


old_corr = pd.DataFrame({"Year":years_old, pollution: poll_old, "Cancer Rates": cancer_old_rates})


# In[13]:


len(cancer_new_rates)


# In[14]:


new_corr = pd.DataFrame({"Year":years_new, pollution: poll_new, "Cancer Rates": cancer_new_rates})


# In[15]:


old_corr.plot.scatter(x=pollution, y="Cancer Rates")
plt.show()


# In[16]:


new_corr.plot.scatter(x=pollution, y="Cancer Rates")
plt.show()


# In[17]:


old_df = pd.DataFrame(old_corr[[pollution, "Cancer Rates"]])
new_df = pd.DataFrame(old_corr[[pollution, "Cancer Rates"]])


# In[18]:


old_df.corr(method = "pearson")
old_df.corr(method = "kendall")
old_df.corr(method = "spearman")


# In[19]:


new_df.corr(method = "pearson")
new_df.corr(method = "kendall")
new_df.corr(method = "spearman")

