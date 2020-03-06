#!/usr/bin/env python
# coding: utf-8

# In[116]:


import matplotlib.pyplot as plt
import numpy as np


# In[124]:


prepro_name = "3ch"
csv = np.loadtxt("train_" + prepro_name + "/ArtGrass01/ArtGrass01_01_3ch.csv",delimiter=",")
_,x,y,z = np.hsplit(csv,4)
time = list(range(0,len(nx)))


# In[118]:


a = np.concatenate([x,y,z], axis=0)
amp_max = a.max()
amp_min = a.min()
cent = (amp_max-amp_min)/2
ave = (amp_max+amp_min)/2
nx = (x - ave)/cent
ny = (y - ave)/cent
nz = (z - ave)/cent


# In[ ]:





# In[ ]:





# In[7]:


p1 = plt.plot(left, height, linewidth=2)
p2 = plt.plot(left, height/2, linewidth=2, linestyle="dashed")
plt.legend((p1[0], p2[0]), ("Class 1", "Class 2"), loc=2)


# In[ ]:




