#!/usr/bin/env python
# coding: utf-8

# In[3]:


def swap(string):
    start=string[0]
    end=string[-1]
    swap_string=end+string[1:-1]+start
    print(swap_string)
a=input("enter string  : \n")
swap(a)


# In[ ]:




