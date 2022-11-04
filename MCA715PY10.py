#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("enter a value for num"))
sum=0
temp=num
i=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"the number is armstrong ")
else:
    print(num,"the number is not armstrong")


# In[ ]:




