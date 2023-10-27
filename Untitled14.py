#!/usr/bin/env python
# coding: utf-8

# In[4]:


fname=[]
ba=0
print("enter 3 name")
for i in range(0,3):
    a=input()
    fname.append(a)
print(fname)
for i in fname:
    ba=ba+i.count('a')
print("total no of a in names are",ba)


# In[8]:


s=input("enter word")
a=s[0]+s[1:].replace(s[0],'$')
print("after changing",a)


# In[ ]:


q

