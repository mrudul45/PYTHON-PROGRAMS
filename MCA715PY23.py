#!/usr/bin/env python
# coding: utf-8

# In[5]:


def pow(x,n):
    if n==0:
        return 1
    else:
        return(x*pow(x,n-1))
a=int(input("enter the number :"))
b=int(input("enter the power :"))
r= pow(a,b)
print(r)


# In[ ]:




