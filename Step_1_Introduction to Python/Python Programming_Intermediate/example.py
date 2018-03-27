
# coding: utf-8

# __Modules__
# <p style='text-align: justify;'>In programming, a module is a piece of software that has specific functionality. For example, when building a ping pong game, one module would be responsible for the game logic, and another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited seperately.

# __Writing modules__<br>
# - Modules in Python are simply Python files with a `.py` extension. The name of the module will be the name of the file. A Python module can have a set of functions, classes or variables defined and implemented.
# - A file containing Python code, for e.g.: `example.py`, is called a module and its module name would be `example`.
# - We can define our most used functions in a module and import it, instead of copying their definitions into different programs.
# - Let us create a module. Type the following and save it as `example.py`.

# In[1]:


# Python Module example
def add(a, b):
    """This program adds two numbers and return result"""
    
    result = a + b
    return result

