#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=int(input("enter a number :"))
def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
print("the sum is :",sum(num))


# In[ ]:




