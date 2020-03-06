#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


# In[ ]:





# In[42]:


prepro_name = "soc321"
csv = np.loadtxt("train_" + prepro_name + "/ArtGrass01/ArtGrass01_01_"+prepro_name+".csv",delimiter=",")
# _,x,y,z = np.hsplit(csv,4)
_,x = np.hsplit(csv,2)
time = list(range(0,len(x)))


# In[43]:


# a = np.concatenate([x,y,z], axis=0)
# amp_max = a.max()
# amp_min = a.min()
# cent = (amp_max-amp_min)/2
# ave = (amp_max+amp_min)/2
# nx = (x - ave)/cent
# ny = (y - ave)/cent
# nz = (z - ave)/cent


# In[44]:


# prepro_name="dft321"
fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(311,title=prepro_name+'_x', xlabel='time(ms)')
# ax2 = fig.add_subplot(312,title=prepro_name+'_y', xlabel='time(ms)')
# ax3 = fig.add_subplot(313,title=prepro_name+'_z', xlabel='time(ms)')
ax1 = fig.add_subplot(111,title=prepro_name, xlabel='time(ms)')
# ax2 = fig.add_subplot(312,title=prepro_name+'_y', xlabel='time(ms)')
# ax3 = fig.add_subplot(313,title=prepro_name+'_z', xlabel='time(ms)')

# データのプロット
ax1.plot(x,color="b")
# ax2.plot(y,color="r")
# ax3.plot(z,color="g")

plt.tight_layout()
ax1.grid(axis='y', c='gainsboro', zorder=9)
# ax2.grid(axis='y', c='gainsboro', zorder=9)
# ax3.grid(axis='y', c='gainsboro', zorder=9)

# pdfファイルの初期化
# pp = PdfPages(prepro_name+'.pdf')

# figureをセーブする
# pp.savefig()

fig.savefig(prepro_name+'_1.png')

# pdfファイルをクローズする。
# pp.close()


# In[ ]:





# In[7]:





# In[ ]:




