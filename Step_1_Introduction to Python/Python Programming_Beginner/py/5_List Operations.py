
# coding: utf-8

# __Introduction to the Data Set__<br>
# - In this mission, we'll look at daily weather data for Los Angeles (L.A.) during 2014. Here's a look at the beginning of `la_weather.csv`, the data set we'll be working:

# In[1]:


r = open('la_weather.csv', 'r')


# In[2]:


weather = r.read()


# - `Day` - A number from `1` to `365` indicating the day of the year. January 1st is `1`, and December 31st is `365`.
# - `Type of Weather` - The type of weather experienced on that day. The values that may appear here include `Rain`, `Sunny`, `Fog`, `Fog-Rain`, or `Thunderstorm`.
# 
# Our ultimate goal is to count how many times each type of weather occurred over the course of the year. During this mission, we'll learn how to manipulate the data with lists, and make good progress towards that goal. In the next mission, we'll fit all the pieces together and tally up the data.

# __Parsing the File__

# In[3]:


rows = weather.split('\n')
rows.pop(0) # Delete the first element (names)


# In[4]:


# Create an empty list `weather_data`
weather_data = []
for row in rows:
    split_row = row.split(',')
    weather_data.append(split_row)
weather_data[:5]


# __Getting a Single Column From the Data__<br>
# 
# - The first value in each _column_ is from the header _row_; it labels the data that appears in the column. While not all data sets include headers, they're helpful to have.
# - Since we'll be counting the total number of times each type of weather occurred during the year, we don't need the `Day` column.

# In[5]:


weather = []
for value in weather_data:
    type_of = value[1]
    weather.append(type_of)
weather[:7]


# __Counting the Items in a List__

# In[6]:


count = 0
for item in weather:
    count += 1
count


# __Removing the item in List__
# ```python
# del list_name[index]
# list_name.pop(index)
# ```

# __The In Statement__
# ```python
# animals = ['cat','dog','rabbit']
# for animal in animal:
#     if animal == 'cat':
#         print('Cat found')
# ```
# - More quickly
# ```python
# animals = ['cat','dog','rabbit']
# if 'cat' in animals:
#     print('Cat found')
# ```
# - We can directly assign the result to a variable as well
# ```python
# animals = ['cat','dog','rabbit']
# cat_found = 'cat' in animals
# ```

# In[7]:


animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]


# In[8]:


cat_found = 'cat' in animals


# In[9]:


cat_found


# In[10]:


space_monster_found = 'space_monster' in animals
space_monster_found


# __Weather Types__

# In[11]:


weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]


# In[12]:


weather_type_found = []
for item in weather_types:
    found = item in weather
    weather_type_found.append(found)
weather_type_found


# In this mission, we covered _list slicing, columns,_ and the _in statement._ We also formatted the weather data correctly so it will be ready for further analysis. In the next mission, we'll count up how many times each type of weather occurred in our data.
