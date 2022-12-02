num=int(input("enter a number :"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=(10*rev)+dig
    num=num//10
if(temp==rev):
    print(temp,"- is a palindrome number")
else:
    print(temp,"- is not a palindrome number")
