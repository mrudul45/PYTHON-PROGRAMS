#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fibonacci(x):
    n1=0
    n2=1
    count=0
    if x==1:
        print("fibonacci series upto ",x,": ")
        print(n1)
    else:
        print("fibonacci series :")
        while(count<x):
            print(n1)
            y=n1+n2
            n1=n2
            n2=y
            count=count+1
x=int(input("enter the limit x :"))
fibonacci(x)


# In[ ]:





# In[ ]:




