
# coding: utf-8

# __Opening Files__<br>
# To open a file in Python, we use the `open()` function. This function accepts two different arguments (inputs) in the parentheses, always in the following order:
# - The name of the file (as a string)
# - The mode of working with the file (as a string) 
# 
# We'll learn about the various modes in a later mission. For now, we'll just use `"r"`, the mode for reading in files.

# In[1]:


a = open('story.txt', 'r')


# In[2]:


print(a)


# In[3]:


f = open('crime_rates.csv', 'r')


# In[4]:


print(f)


# __Reading in Files__<br>
# File objects have a `read()` method that returns a string representation of the text in a file.

# In[5]:


g1 = a.read()


# In[6]:


print(g1)


# In[7]:


data = f.read()


# In[8]:


print(data)


# __Splitting__<br>
# In Python, we can use the `split()` method to turn a _string_ object into a _list_ of _strings_, like so:
# ```python
# ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
# ```

# In[9]:


# We can split a string into a list.
sample = 'john,plastic,joe'
split_list = sample.split(',')


# In[10]:


print(split_list)


# In[11]:


# Here's another example
string_two = 'How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?'
split_string_two = string_two.split('\n')


# In[12]:


print(split_string_two)


# In[13]:


rows = data.split('\n')


# In[14]:


print(rows)


# __Loops__

# In[16]:


# The variable `ten_rows` contains the first 10 elements in `rows`
ten_rows = rows[0:10]


# In[17]:


for row in ten_rows:
    print(row)


# __List of Lists__

# In[18]:


three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []

for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)


# In[19]:


print(final_list[0])


# In[20]:


print(final_list[1])


# In[21]:


print(final_list[2])


# __Practice-Splitting elements in a list__

# In[24]:


final_data = []
for data_row in rows:
    split_data = data_row.split(',')
    final_data.append(split_data)
print(final_data)


# In[25]:


print(rows[0:5])


# In[26]:


print(final_data[0:5])


# __Accessing elements in a list of lists: The manual way__

# In[27]:


# `five_elements` contains the first five elements from `final_data`
five_elements = final_data[0:5]


# In[33]:


cities_list = []
cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])
print(cities_list)


# __Looping through a list of lists__

# In[31]:


cities_list = []
for element in five_elements:
    cities_list.append(element[0])
print(cities_list)


# In[34]:


crime_rates = []
for row in five_elements:
    crime_rate = row[1]
    crime_rates.append(crime_rate)
print(crime_rates)


# ### Challenge

# In[37]:


int_crime_rates = []
for row in rows:
    elements = row.split(',')
    int_crime_rates.append(int(elements[1]))
print(int_crime_rates)

