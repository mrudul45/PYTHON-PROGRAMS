#!/usr/bin/env python
# coding: utf-8

# In[5]:


str=input("enter a string : ")
s=str[0]
for i in range (len(str)):
    str=str.replace(str[0],'$')
    str1=s+str[1:]
print(str)


# In[ ]:




