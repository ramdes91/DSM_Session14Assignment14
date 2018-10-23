
# coding: utf-8

# Problem Statement 1:
# You survey households in your area to find the average rent they are paying. Find the
# standard deviation from the following data:
# $1550, $1700, $900, $850, $1000, $950.

# In[1]:


import pandas as pd
# Area Rent data from the given list
areaRent = [1500,1700,900,850,1000,950]
# Let the data frame be df
df = pd.DataFrame(areaRent)
display(df)


# In[2]:


display(df.describe())


# In[3]:


display(df.std())


# 357.770876

# Problem Statement 2:
# Find the variance for the following set of data representing trees in California (heights in
# feet):
# 3, 21, 98, 203, 17, 9

# In[4]:


import pandas as pd

height = [3,21,98,203,17,9]

df = pd.DataFrame(height)

df.var()


# In[5]:


df.iloc[:,0].var()


# Problem Statement 3:
# In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7
# failed in two subjects and 3 failed in three subjects. Find the probability distribution of
# the variable for number of subjects a student from the given class has failed in.

# In[6]:


# Percentage and Probablity of the data Total Students = 100 => 100% Passed = 80 => 80% =>80/100 => 80% 0.8 Probability 
# 1 Subject Failed = 10 => 10% 0.1 Probability 
# 2 Subjects Failed = 7 => 7% 0.07 Probability 
# 3 Subjects Failed = 3 => 3% 0.03 Probability

import numpy as np
import pandas as pd
import scipy.stats as stats
list=[0.1,0.03,0.07,0.8]
df = pd.DataFrame(list)
display(df.describe())


# In[7]:


mean = 0.250000
standard_deviation = 0.367786
# For accurate values * 100
# 25.00 & 36.7786


# In[8]:


# Cummilative Denisty Function
stats.norm(25.00,36.7786).cdf(80)


# In[10]:


# Probability Denisity Function
stats.norm(25.00,36.7786).pdf(80)

