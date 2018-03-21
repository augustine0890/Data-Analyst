
# coding: utf-8

# __The Data Set__

# In[1]:


r = open('la_weather.csv', 'r')


# In[2]:


w = r.read()


# In[3]:


w_list = w.split('\n')


# In[4]:


weather = []
for w in w_list:
    wt = w.split(',')
    weather.append(wt)
weather[:5]


# In[5]:


del weather[0]


# In[6]:


col_weather = []
for w in weather:
    col_weather.append(w[1])
col_weather[:5]


# - Assign the first element of `col_weather` to `first_element` and display it using the `print()` function.
# - Assign the last element of `col_weather` to `last_element` and display it using the `print()` function.

# In[7]:


first_element = col_weather[0]
first_element


# In[8]:


last_element = col_weather[len(col_weather) - 1]
last_element


# __Dictionaries__

# In[9]:


students = ['Tom','Jim','Sue','Ann']
scores = [70,80,85,75]


# In[10]:


indexes = [0,1,2,3]
name = 'Sue'
score = 0
for i in indexes:
    if students[i] == name:
        score = scores[i]
print(score)


# In[11]:


# Make an empty dictionary like this:
scores = {'Tom':70,'Jime':80,'Sue':85,'Ann':75}


# In[12]:


scores['Tom']


# __Practice populating a Dictionary__

# In[13]:


superhero_ranks = {'Aquaman':1, 'Seperman':2}


# In[14]:


president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]


# __Defining a Dictionary with Values__

# In[15]:


random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}


# In[16]:


random_values


# In[17]:


# Create a dictionary named `animals`
animals = {7:'raven',
           8:'goose',
           9:'duck'}


# In[18]:


animals


# In[19]:


# Create a dictionary named `times` 
times = {'morning': 8,
         'afternoon': 14,
         'evening': 19,
         'night': 23}
times


# __Modifying Dictionary Values__

# In[20]:


students = {
    "Tom": 60,
    "Jim": 70
}


# In[21]:


# Add the key `Ann` and value 85 to the dictionary students
students['Ann'] = 85


# In[22]:


students


# In[23]:


# Replace the value for the key Tom with 80
students['Tom'] = 80


# In[24]:


# Add 5 to the value for the key Jim
students['Jim'] = students['Jim'] + 5


# In[25]:


students


# __The In Statement and Dictionaries__

# In[26]:


planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}


# In[27]:


# Check whether `jupiter` is a key in `planet_numbers`
jupiter_found = 'jupiter' in planet_numbers


# In[28]:


jupiter_found


# In[29]:


earth_found = 'earth' in planet_numbers


# In[30]:


earth_found


# __The Else Statement__
# ```python
# if temperature > 50:
#     print("It's hot!")
# else:
#     print("It's cold!")
# ```

# __Practicing with the Else Statement__

# In[31]:


scores = [80, 100, 60, 30]
high_scores = []
low_scores = []
for score in scores:
    if score > 70:
        high_scores.append(score)
    else:
        low_scores.append(score)


# In[32]:


high_scores


# In[33]:


low_scores


# In[34]:


planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for name in planet_names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)


# In[35]:


short_names


# In[36]:


long_names


# __Counting with Dictionaries__

# In[37]:


pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]


# In[38]:


pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] += 1
    else:
        pantry_counts[item] = 1


# In[39]:


pantry_counts


# In[40]:


#print key and values
for key, value in pantry_counts.items():
    print(key, value)


# __Counting the Weather__
# 
# - Count how many times each type of weather occurs in the `col_weather` list, and store the results in a new dictionary called `weather_counts`.
# - When finished, `weather_counts` should contain a key for each different type of weather in the `weather` list, along with its associated frequency. Here's a preview of how the result should format the `weather_counts` dictionary.

# In[41]:


weather_counts = {}
for weather in col_weather:
    if weather in weather_counts:
        weather_counts[weather] += 1
    else:
        weather_counts[weather] = 1


# In[42]:


weather_counts

