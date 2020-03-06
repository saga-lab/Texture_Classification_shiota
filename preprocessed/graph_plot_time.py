#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages


# In[19]:


csv = pd.read_csv("../logs/time_table.csv", index_col=0)


# In[20]:


csv


# In[21]:


plt.figure()
csv.plot.bar(y=['training_time','preprocess_time'], stacked=True, alpha=1, grid=True,figsize=(15,8)).legend(loc='lower right')
# plt.ylim([0.65,1.0]) 
plt.title('process time', size=16)
plt.ylabel("time(s)",size=12)
# plt.ylim([1000,1750]) 
# figureをセーブする
plt.savefig('process_time.png',bbox_inches='tight')


# In[ ]:




