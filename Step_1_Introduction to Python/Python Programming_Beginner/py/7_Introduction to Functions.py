
# coding: utf-8

# ### Overview
# In this mission, we will work with a data set consisting of high-grossing movies, according to the Internet Movie Database(IMDb). IMDb is an online extensive database for films, television programs and video games. Our end goal is to create a dictionary that stores useful statistics from this data set, named `movie_metadata`. In order to do this, we will:
# 
# - Clean data to make the information useful to us more easily accessible
# - Practice using dictionaries in more complex functions
# - Learn how to write our own functions!

# In[1]:


o = open('movie_metadata.csv','r')


# In[2]:


r = o.read()


# In[3]:


rows = r.split('\n')


# In[4]:


movie_data = []
for row in rows:
    element = row.split(',')
    movie_data.append(element)
movie_data[:3]


# In[5]:


movie = movie_data[:100]


# __Motivating Functions__

# If we had a __`parser()`__ function, the code for the last instructions would be as concise as this:
# ```python
# movie_data = parser(movie_metadata)
# print(movie_data[:2])
# [['color',
#   'director_name',
#   'duration',
#   'actor_1_name',
#   'movie_title',
#   'language',
#   'country',
#   'title_year',
#   'imdb_score'],
#  ['Color',
#   'James Cameron',
#   '178.0',
#   'CCH Pounder',
#   'Avatar\xa0',
#   'English',
#   'USA',
#   '2009.0',
#   '7.9']]
# ```
# Other than reusability, there are 3 main advantages of using functions:
# 
# - They allow us to use other people's code without the necessity to have a deep understanding of how it was written (e.g., we use the `print()` function without reading the code inside it). We call this information hiding.
# - They break down complex logic into smaller components or modules. Instead of writing very lengthy and complicated code, we can progress function by function. For example, if we were writing a larger piece of code, `parser()` as a function would be easier to manage rather than the code that executes the same behavior. This would make testing easier as well. We refer to this as modularity, which is especially important when working on teams. Modularity makes it easier for someone else to read, understand, use, and build upon our code.
# - They streamline our code and make it easier to maintain. Programmers reuse the same functions in multiple situations across a project. This means that they generalize the function as much as possible to maximize its usefulness. we call this process abstraction, which is an important part of reducing our code's complexity, especially for larger projects.

# __Writing our own functions__<br>
# - Write a function, with a definition, name, argument(s), body and return value, that returns a list containing the names of the movies in `movie_data`.

# In[6]:


def call_name(input_lst):
    movie_names = []
    for each in input_lst:
        movie_names.append(each[4])
    return movie_names


# In[7]:


movie_name = call_name(movie)
movie_name[:5]


# In[8]:


new_movie = []
for each in movie:
    add = [s.replace('\xa0','') for s in each]
    new_movie.append(add)


# In[9]:


new_movie[:4]


# __Functions with Multiple Return Paths__

# In[10]:


def is_usa(movie):
    num_usa = 0
    for item in movie:
        if item[6] == 'USA':
            num_usa += 1
        else:
            num_usa
    print(num_usa)


# In[11]:


is_usa(new_movie)


# In[12]:


new_movie[2][6]


# In[13]:


wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]


# In[14]:


def us_found(input_lst):
    if input_lst[6] == 'USA':
        return True
    else:
        return False


# In[15]:


us_found(wonder_woman)


# __Functions with Multiple Arguments__

# In[16]:


def index_equals_str(lst, index, strs):
    if lst[index] == strs:
        return True
    else:
        return False


# In[17]:


index_equals_str(wonder_woman, 2, 'color')


# __Optional Arguments__

# In[18]:


def feature_counter(lst, index, strs, header_row = False):
    num_elt = 0
    if header_row == True:
        lst = lst[1:len(lst)]
    for each in lst:
        if each[index] == strs:
            num_elt += 1
    return num_elt


# In[19]:


feature_counter(new_movie, 6, 'UK')


# In[20]:


def count_entries(lst, index, header = False):
    feature_count = {}
    if header == True:
        lst = lst[1:len(lst)]
    for each in lst:
        if each[index] in feature_count.keys():
            feature_count[each[index]] += 1
        else:
            feature_count[each[index]] = 1
    return feature_count


# In[21]:


count_entries(new_movie, 6, True)


# __Calling a Function inside another Function__
# - Write a `summary_statistics()` function that will take `movie_data` as input, and output a dictionary that will give useful numbers from the data.
# - Call the function with `movie_data` as its input, and store its value in `summary`.

# In[22]:


# Define summary_statistic() with one argument, an input list.
def summary_statistic(lst):
    # Use the feature_counter()
    num_japan_films = feature_counter(lst, 6, 'Japan', True)
    num_color_films = feature_counter(lst, 0, 'Color', True)
    num_films_in_english = feature_counter(lst, 5, 'English', True)
    # Create a dictionary that associates the keys
    summary_dict = {"japan_films" : num_japan_films, "color_films" : num_color_films, "films_in_english" : num_films_in_english}
    return summary_dict


# In[23]:


summary_statistic(new_movie)


# Congratulations! In this mission, we explored how we can write our own functions, how we can use multiple paths, multiple and optional arguments, and call functions inside one another. Meanwhile, we built a counter, and ultimately a dictionary that uses this counter to store useful statistics from IMDb's high-grossing movies data set. Next, we will see what can go wrong when we are writing a function and learn the meanings of the most common errors.
