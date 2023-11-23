#!/usr/bin/env python
# coding: utf-8

# In[10]:


d1={}
d2={}
for i in range(0,2):
    key1=int(input("enter key of dict 1:"))
    value1=input("enter value of dict 1");
    d1[key1]=value1;
for i in range(0,2):
    key2=int(input("enter key of dict 2:"))
    value2=input("enter value of dict 2");
    d2[key2]=value2;
d1.update(d2);
print("the merged dict :",d1)


# In[ ]:


n=int(input("enter number"))
if(n<=0):
    print("The factorial is : 0")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("The factorial is : ",fact)


# In[ ]:





# In[ ]:




