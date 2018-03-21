
# coding: utf-8

# In[1]:


import pandas as pd
crime_rates = pd.read_csv('crime_rates.csv', names=['city','rate'])


# __Booleans__

# In[2]:


cat = True
dog = False


# In[3]:


type(cat)


# In[4]:


type(dog)


# __Boolean Operators__

# In[5]:


first_alb = crime_rates.city[0] == "Albuquerque"


# In[6]:


first_alb


# In[7]:


second_alb = crime_rates.city[1] == "Albuquerque"


# In[8]:


second_alb


# In[9]:


last = len(crime_rates.city)
crime_rates.city[0] == crime_rates.city[last - 1]


# __Booleans with "Greater Than"__

# In[10]:


first_500 = crime_rates.rate[0] > 500


# In[11]:


first_500


# In[12]:


first_749 = crime_rates.rate[0] >= 749


# In[13]:


first_749


# In[14]:


crime_rates.rate[0] >= crime_rates.rate[last - 1]


# __Booleans with "Less Than"__

# In[15]:


second_500 = crime_rates.rate[1] < 500


# In[16]:


second_500


# In[17]:


second_371 = crime_rates.rate[1] <= 371


# In[18]:


second_371


# In[19]:


crime_rates.rate[1] <= crime_rates.rate[last - 2]


# __If statements__

# In[20]:


result = 0
if crime_rates.city[2] == "Anchorage":
    result = 1
result


# __Nesting If Statements__

# In[21]:


both_conditions = False
if crime_rates.rate[0] > 500:
    if crime_rates.rate[1] > 300:
        both_conditions = True
both_conditions


# __If Statements and For Loops__

# In[22]:


found = False
for city in crime_rates.city:
    if city == "Washington":
        found = True
found


# In[23]:


counter = 0
index = 0
for city in crime_rates.city:
    if city == "Washington":
        index = counter
    counter += 1
index


# In[24]:


five_hundred_list = []
for rate in crime_rates.rate:
    if rate > 500:
        five_hundred_list.append(rate)
five_hundred_list


# __Find the Highest Crime Rate__

# In[25]:


crime_rates.loc[crime_rates['rate'].idxmax()]


# In[26]:


crime_rates['rate'].idxmax()


# In[27]:


crime_rates[crime_rates['rate'] == crime_rates['rate'].max()]


# In[28]:


highest = crime_rates.rate[0]
for rate in crime_rates.rate:
    if rate > highest:
        highest = rate
highest

