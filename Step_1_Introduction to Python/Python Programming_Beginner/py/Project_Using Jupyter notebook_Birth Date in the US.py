
# coding: utf-8

# ## Birth Dates in The United States
# The raw data behind the story __Some People Are Too Superstitious To Have A Baby On Friday The 13th__, which you can read [here](https://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/)
# 
# We'll be working with the data set from the Centers for Disease Control and Prevention's National National Center for Health Statistics. The data set has the following structure:
# 
# - `year` - Year
# - `month` - Month
# - `date_of_month` - Day number of the month
# - `day_of_week` - Day of week, where 1 is Monday and 7 is Sunday
# - `births` - Number of births

# In[1]:


f = open('births.csv', 'r')


# In[2]:


text = f.read()


# In[3]:


# print(text)


# In[4]:


line_list = text.split('\n')


# In[5]:


line_list[:5]


# In[6]:


births = [] 
for each in line_list:
    births.append(each.split(','))


# In[7]:


births[:3]


# In a new code cell, add code that returns a dictionary containing the total number of births for each unique day of the week.
# - The result should be a dictionary where the keys are the unique `day_of_week` values and the associated values are the total number of births. 

# In[9]:


days_counts = {}
birth = births[1:len(births)]
for each in birth:
    if each[3] in days_counts.keys():
        days_counts[each[3]] += int(each[4])
    else:
        days_counts[each[3]] = int(each[4])
days_counts


# Create a function named `read_csv()` that:
# - Takes a single, required argument, a string representing the file name of the CSV file.
# - Reads the file into a string, splits the string on the newline character (`"\n"`), and removes the header row. Assign this list to `string_list` and create an empty list named `final_list`.

# In[23]:


def read_csv(filename):
    stringdata = open(filename).read()
    stringlist = stringdata.split('\n')[1:]
    final_list = []
    
    for row in stringlist:
        string_fields = row.split(',')
        int_fields = []
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list


# In[24]:


data_list = read_csv('births.csv')


# In[28]:


data_list[:5]


# Create a function named `counting()` that:
# 
# Takes two, required parameters:
# - `data`: a list of lists
# - `column`: the column number we want to calculate the totals for

# In[25]:


def counting(data,index):
    counts = {}
    for each in birth:
        if each[index] in counts.keys():
            counts[each[index]] += int(each[4])
        else:
            counts[each[index]] = int(each[4])
    return counts


# __Calculating number of births each month__

# In[26]:


counting(data_list,1)


# __Calculating number of births each year__

# In[27]:


counting(data_list,0)


# __Calculating number of births each day of week__

# In[29]:


counting(data_list, 3)

