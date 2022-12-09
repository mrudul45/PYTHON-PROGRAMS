#!/usr/bin/env python
# coding: utf-8

# In[5]:


def rec(n):
    if(n==1):
        return 1
    else:
        return n*rec(n-1)
num=int(input("enter the number :"))
if (num<0):
    print("factorial does not exist !")
elif(num==0):
        print("factorial is 1 ")
else:
    print("Factorial of",num,"=",rec(num))


# In[ ]:




