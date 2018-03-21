
# coding: utf-8

# __Expressions__

# In[1]:


print(1288)


# In[2]:


print(1288 + 639)


# In[3]:


1288 + 639


# __Operators__

# In[4]:


# Calcualtes the average
(749 + 371 + 828 + 503 + 1379)/5


# __Variables__

# In[5]:


albuquerque = 749


# In[6]:


anaheim = 371


# In[7]:


anchorage = 828


# In[8]:


arlington = 503


# In[9]:


atlanta = 1379


# In[10]:


print(anaheim)


# __Data Types__

# In[11]:


atlanta_string = 'Atlanta'


# In[12]:


atlanta_float = 1379.5


# In[13]:


print(atlanta_string)


# __The `type` function__
# 
# The `type()` statement won't display anything. Instead, it will return the data type as a value.
# ```python
# hello = 'Hello'
# print(type(hello))
# ```

# In[14]:


type(atlanta_string)


# In[15]:


type(atlanta_float)


# __List__
# 
# To add values to a list object, use the `list.append()` __method__

# In[16]:


# Create two empty lists
cities = []
crime_rates = []


# In[17]:


cities.append('Albuquerque')
cities.append('Anaheim')
cities.append('Anchorage')
cities.append('Arlington')
cities.append('Atlanta')


# In[18]:


crime_rates.append(749)
crime_rates.append(371)
crime_rates.append(828)
crime_rates.append(503)
crime_rates.append(1379)


# In[19]:


cities


# In[20]:


crime_rates


# In[21]:


# Create the list with values
months = [1,2,3,4,5,6,7,8,9,10,11,12]


# In[22]:


months


# __Accessing elements in a list__

# In[23]:


# The third element from the list `cities`
anchorage_str = cities[2]


# In[24]:


anchorage_str


# In[25]:


# The third element from the list `crime_rates`
anchorage_cr = crime_rates[2]


# In[26]:


anchorage_cr


# __Retrieving the length of a list__

# In[27]:


last_index = len(crime_rates) - 1
last_value = crime_rates[last_index]


# In[28]:


last_value


# In[29]:


# Add the lengths of the `cities` and `crime_rates` list objects and assign the sum to `two_sum`
two_sum = len(cities) + len(crime_rates)


# In[30]:


two_sum


# __Slicing lists__

# In[31]:


# Values at index 2, 3, 4
ending_index = len(crime_rates)
two_to_end = crime_rates[2:ending_index]


# In[32]:


two_to_end


# In[35]:


cities_slice = cities[1:4]


# In[36]:


cities_slice


# In[37]:


# Select the last two elements in `crime_rates` and assign to `cr_slice`
starting_index = len(crime_rates) - 2
cr_slice = crime_rates[starting_index:ending_index]


# In[38]:


cr_slice

