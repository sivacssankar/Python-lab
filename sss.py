#!/usr/bin/env python
# coding: utf-8

# In[2]:


list=[]
for i in range(0,5):
    n=int(input("enter integer"))
    list.append(n)
print(list)
list=[i for i in list if i>0]
print("positive no. of the list",list)


# In[4]:


list=[]
for i in range(0,3):
    n=int(input("enter number"))
    list.append(n)
list=[(i*i) for i in list if i>0]
print("square is",list)


# word=[]
# vaov=

# In[7]:


vov=['a','e','i','o','u','A','E','I','O','U']
word=input("enter word")

vo=[i for i in word if i in vov]
print("the word is",word)
print("the vowel is",vo)


# In[11]:


wordsss=input("enter word")

vo=[ord(i) for i in wordsss]
print("ordinal value is",vo)


# In[ ]:




