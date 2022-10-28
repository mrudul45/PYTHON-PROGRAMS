#!/usr/bin/env python
# coding: utf-8

# In[9]:


year = int(input("enter a year "))
if(year%400==0):
    print(year," is a leap year")
elif(year%4==0 and year%100!=0):
    print(year,"is a leap year ")
else:
    print(year,"not a leap year")


# In[ ]:




