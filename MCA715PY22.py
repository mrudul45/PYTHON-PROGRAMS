#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fib(n):
    if(n<=1):
        return(n)
    elif n>0:
        return(fib(n-1)+fib(n-2))
l=int(input("enter the number :"))
for i in range(0,l):
        r=fib(i)
        print(r)


# In[ ]:




