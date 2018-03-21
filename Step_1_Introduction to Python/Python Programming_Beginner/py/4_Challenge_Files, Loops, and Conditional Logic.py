
# coding: utf-8

# In[1]:


import pandas as pd


# __Unisex Names__<br>
# - Read the File into a String

# In[2]:


r = open('dq_unisex_names.csv', 'r')


# In[3]:


names = r.read()


# __Convert the string to a list__

# Use the `split()` method that _strings_ have to split on the new-line delimiter (`"\n"`), and assign the resulting _list_ to `names_list`.

# In[4]:


names_list = names.split('\n')


# Select the first five elements in `names_list`, and assign them to `first_five`.

# In[5]:


first_five = names_list[:5]


# In[6]:


first_five


# __Convert the List to Strings to a List of Lists__<br>
# - Split each element in `names_list` on the comma delimiter (`,`) and append the resulting list to `nested_list`.

# In[7]:


nested_list = []
for value in names_list:
    comma_list = value.split(',')
    nested_list.append(comma_list)
nested_list[0:5]


# __Convert Numerical Values__<br>
# Create a new list of lists called `numerical_list` where:
# 
# - The element at index `0` for each list is the unisex name (as a string)
# - The element at index `1` for each list is the number of people who share that name (as a float)

# In[8]:


numerical_list = []
for value in nested_list:
    strings = value[0]
    floats = float(value[1])
    new_list = [strings,floats]
    numerical_list.append(new_list)
numerical_list[:5]


# __Filter the List__<br>
# Create a new list of strings called `thousand_or_greater` that only contains the names shared by 1,000 people or more.

# In[9]:


len(numerical_list)


# In[10]:


numerical_list[497]


# In[11]:


thousand_or_greater = []
for value in numerical_list:
    if value[1] >= 1000:
        thousand_or_greater.append(value)
thousand_or_greater[:5]

