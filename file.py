#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=open("siva.txt")
fi=a.readlines()
b=[i.strip() for i in fi]
print(b)


# In[28]:


a=open("siva.txt")
z=open("dd.txt","w")
fi=a.readlines()
for i in range(len(fi)):
    if i%2!=0:
        z.write(fi[i])
        
z.close()
z=open("dd.txt")
cj=z.readlines()
cj=[x.strip() for x in cj]
print(cj)
a.close()
z.close()



# In[ ]:





# In[ ]:




