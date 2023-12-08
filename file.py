#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=open("siva.txt")
fi=a.readlines()
b=[i.strip() for i in fi]
print(b)


# In[28]:


a=open("siva.txt","r")
fi=a.readlines()
for i in range(0,len(fi)):
    if i%2==0:
        print(fi[i+1])


# In[ ]:





# In[ ]:




