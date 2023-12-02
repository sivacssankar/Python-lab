#!/usr/bin/env python
# coding: utf-8

# In[1]:


square=[]
initial=int(input("Enter initial number:"))
final=int(input("Enter final number:"))
for i in range(initial,final+1):
    sqr=i*i
    d=sqr
    while(d>0):
        digit=d%10
        if digit%2==0:
            d//=10
            if d==0:
                square.append(sqr)
        else:
            break
print(square)


# In[21]:


n=int(input("enter number of rows"))

for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("\n")
        


# In[ ]:





# In[19]:


n=input("enter word")
a=len(n)
print(a)


# In[23]:


n=input("enter word")
if n.endswith("ing"):
    a=n+("ly")
else:
    a=n+("ing")
print(a)


# In[34]:


list=[]

i=1
for i in range(4):
    n=input("enter word")
    list.append(n)
print(list)
for i in list:
    j=len(list[0])
    current=len(i)
    if current>j:
        j=current
print(j)
    


# In[ ]:




