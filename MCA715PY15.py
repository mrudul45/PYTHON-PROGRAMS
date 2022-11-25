#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("conversion from binary to decimal")
a=(input("enter the binary number :"))
n=len(a)
x=int(a)
def btod(x,n):
    temp=0
    for i in range(0,n):
        dec1=x%10
        temp+=dec1*(2**i)
        x//=10
    return temp
z=btod(x,n)
print("decimal=",z)


# In[ ]:




