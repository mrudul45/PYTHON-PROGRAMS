#!/usr/bin/env python
# coding: utf-8

# In[4]:


w=input("enter the string :")
a=[]
str=w.split()
for i in str:
    if i not in a:
        a.append(i)
print("list",a)
count=0
for i in range (len(w)):
    if(w[i]=='a'):
        count=count+1
print("the occurrences of a :",count)


# In[ ]:




