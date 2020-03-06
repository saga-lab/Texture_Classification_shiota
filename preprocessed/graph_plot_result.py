#!/usr/bin/env python
# coding: utf-8

# In[83]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages


# In[84]:


csv = pd.read_csv("../logs/result_table.csv", index_col=0)


# In[85]:


csv


# In[90]:


plt.figure()
plt.rcParams["font.size"] = 28
csv.plot.bar(y=['accuracy', 'precision', 'recall', 'F-measure'], alpha=1, grid=True,figsize=(15,8)).legend(loc='upper left',fontsize=14)
plt.ylim([0.65,1.0]) 
plt.title('result', size=16)


# figureをセーブする
plt.savefig('result.png',bbox_inches='tight')


# In[76]:



plt.figure()
ax = csv.plot.bar(y=['accuracy'], alpha=1, grid=True,figsize=(15,8)).legend(loc='upper left')
plt.ylim([0.65,1.0]) 
plt.title('accuracy', size=16)
# figureをセーブする
plt.savefig('accuracy.png',bbox_inches='tight')


# In[77]:


plt.figure()
csv.plot.bar(y=['precision'], alpha=1, color='orange', grid=True,figsize=(15,8)).legend(loc='upper left')
plt.ylim([0.65,1.0]) 
plt.title('precision', size=16)

# figureをセーブする
plt.savefig('precision.png',bbox_inches='tight')


# In[78]:


plt.figure()
csv.plot.bar(y=['recall'], alpha=1, color='g', grid=True,figsize=(15,8)).legend(loc='upper left')
plt.ylim([0.65,1.0]) 
plt.title('recall', size=16)

# figureをセーブする
plt.savefig('recall.png',bbox_inches='tight')


# In[79]:


plt.figure()
csv.plot.bar(y=['F-measure'], alpha=1, color='r', grid=True,figsize=(15,8)).legend(loc='upper left')
plt.ylim([0.65,1.0]) 
plt.title('F-measure', size=16)

# figureをセーブする
plt.savefig('F-measure.png',bbox_inches='tight')


# In[ ]:




