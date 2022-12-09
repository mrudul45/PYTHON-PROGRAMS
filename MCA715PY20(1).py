#!/usr/bin/env python
# coding: utf-8

# In[4]:


def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b;
def div(a,b):
    return a/b;
print("__MENU__")
print("1. ADDITION")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
while True:
    choice= int(input("enter your choice : "))
    num1= float(input("enter your 1st number : "))
    num2= float(input("enter your 2nd number : "))
    if choice==1:
      print(num1,"+",num2,"=",add(num1,num2))
    elif choice==2:
      print(num1,"-",num2,"=",sub(num1,num2))
    elif choice==3:
      print(num1,"*",num2,"=",mul(num1,num2))
    elif choice==4:
      print(num1,"/",num2,"=",div(num1,num2))
    else:
      print("invalid choice")
    x=input("do you want to continue ")
    if x=="no":
        break


# In[ ]:




