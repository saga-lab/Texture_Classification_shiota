#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


# In[30]:


prepro_name = "3ch_normalized"
csv = np.loadtxt("train_" + prepro_name + "/ArtGrass01/ArtGrass01_01"+prepro_name+".csv",delimiter=",")
_,x,y,z = np.hsplit(csv,4)
time = list(range(0,len(x)))


# In[31]:


a = np.concatenate([x,y,z], axis=0)
amp_max = a.max()
amp_min = a.min()
cent = (amp_max-amp_min)/2
ave = (amp_max+amp_min)/2
nx = (x - ave)/cent
ny = (y - ave)/cent
nz = (z - ave)/cent


# In[32]:


fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(311,title=prepro_name+'_x', ylim=(-1, 1), xlabel='time(ms)')
ax2 = fig.add_subplot(312,title=prepro_name+'_y', ylim=(-1, 1), xlabel='time(ms)')
ax3 = fig.add_subplot(313,title=prepro_name+'_z', ylim=(-1, 1), xlabel='time(ms)')

# データのプロット
ax1.plot(nx,color="b")
ax2.plot(ny,color="r")
ax3.plot(nz,color="g")

plt.tight_layout()
ax1.grid(axis='y', c='gainsboro', zorder=9)
ax2.grid(axis='y', c='gainsboro', zorder=9)
ax3.grid(axis='y', c='gainsboro', zorder=9)

# pdfファイルの初期化
pp = PdfPages(prepro_name+'.pdf')

# figureをセーブする
pp.savefig()

# pdfファイルをクローズする。
pp.close()


# In[ ]:





# In[7]:





# In[ ]:




