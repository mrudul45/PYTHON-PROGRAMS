#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=int(input("enter a number :"))
sum=0
for i in range(1,num):
    if (num%i==0):
        sum+=i
if num==sum:
    print(num,"is a perfect number")
else:
    print(num,"is a not a perfect number")


# In[ ]:




