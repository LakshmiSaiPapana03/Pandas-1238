#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd


# In[16]:


ser1 = pd.Series([i for i in range(200,99,-2)])
ser1


# In[18]:


ser2 = pd.Series([i for i in range(200,99,-2)],index = [i for i in range(100,151)])
ser2


# In[20]:


df = pd.DataFrame(np.random.randn(8,6),index = [i for i in range(1,9)],columns = 'a b c d e f'.split())
df


# In[21]:


df.loc[[3,4],['b','e']]


# In[22]:


df.iloc[[2,3],[1,4]]


# In[23]:


branch = ['CSE','CSE','CSE','CSE','CSE','CSE','IT','IT','IT','IT','IT','IT']
members = [1,2,3,4,5,6,1,2,3,4,5,6]
hier_index = list(zip(branch,members))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[24]:


df = pd.DataFrame(np.random.randn(12,2),index=hier_index,columns=['A','B'])
df


# In[25]:


df.loc['CSE'].loc[4]


# In[26]:


df.loc['IT'].loc[[3,5]]


# In[27]:


df2=pd.DataFrame(np.random.randn(5,3),index = 'A B C D E'.split(),columns = 'X Y Z'.split())
df2


# In[28]:


df2.reset_index()

