
# coding: utf-8

# __Types of Errors__
# <p style='text-align: justify;'> As we begin to take greater advantage of functions to organize our code, it can become more complex. We need to better understand the kinds of mistakes we can make when writing it. We've talked briefly about errors, or mistakes that prevent our code from working as we expect, in previous missions. Now it's time to learn more about them. 
# 
# The two main types of errors are:
# - Syntax errors
# - Runtime errors

# __Syntax Errors__

# ```python
# # Missing ending quotes.
# the_answer = '42
# 
# # 'def' keyword misspelled as 'de'
# de find():
#     print('42')
# 
# def find():
#     print("42")
#      print("what, really?")
# ```

# In[1]:


def first_elts(input_lst):
    elts = []
    for each in input_lst:
        elts.append(each[0])
    return elts


# In[2]:


animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]


# In[3]:


first_elts(animals)


# __Runtime Errors__
# - <p style='text-align: justify;'> Runtime errors are very common. While code often works in predictable situations, runtime errors occur when it fails at handling a case the programmer didn't account for.
# 
# - <p style='text-align: justify;'>Because runtime errors occur when our code is running and can't be detected during parsing, they're more difficult to prevent than syntax errors. As you become more proficient in programming, however, you'll learn to identify potential runtime errors beforehand and prevent them from occurring. Python and most other programming languages include tools like error handling and automated tests that help you manage and reduce runtime errors. As your code becomes more complex, you'll learn how to incorporate errors into the functions you write to so that they fail gracefully, and prevent certain negative behavior from occurring.

# __TypeError and ValueError__
# ```python
# forty_two = 42
# forty_two + '42'
# 
# float('guardians')
# ```

# __IndexError and AttributeError__

# In[4]:


lives = [1,2,3]


# In[5]:


lives[0]


# In[6]:


f = open('story.txt')


# In[7]:


story = f.read()

