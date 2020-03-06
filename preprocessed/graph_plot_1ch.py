#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


# In[11]:


prepro_name1 = "soc321"
csv1 = np.loadtxt("train_" + prepro_name1 + "/ArtGrass01/ArtGrass01_01_"+prepro_name1+".csv",delimiter=",")
_,soc321 = np.hsplit(csv1,2)

prepro_name2 = "mag321"
csv2 = np.loadtxt("train_" + prepro_name2 + "/ArtGrass01/ArtGrass01_01_"+prepro_name2+".csv",delimiter=",")
_,mag321 = np.hsplit(csv2,2)

prepro_name3 = "PCA"
csv3 = np.loadtxt("train_" + prepro_name3 + "/ArtGrass01/ArtGrass01_01_"+prepro_name3+".csv",delimiter=",")
_,PCA = np.hsplit(csv3,2)

prepro_name4 = "dft321_co50"
csv4 = np.loadtxt("train_" + prepro_name4 + "/ArtGrass01/ArtGrass01_01_"+prepro_name4+".csv",delimiter=",")
_,dft321 = np.hsplit(csv4,2)

time = list(range(0,len(soc321)))


# In[12]:


fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(411,title=prepro_name1, xlabel='time(ms)')
ax2 = fig.add_subplot(412,title=prepro_name2, xlabel='time(ms)')
ax3 = fig.add_subplot(413,title=prepro_name3, xlabel='time(ms)')
ax4 = fig.add_subplot(414,title=prepro_name4, xlabel='time(ms)')

# データのプロット
ax1.plot(soc321,color="b")
ax2.plot(mag321,color="r")
ax3.plot(PCA,color="g")
ax4.plot(dft321,color="C1")

plt.tight_layout()
ax1.grid(axis='y', c='gainsboro', zorder=9)
ax2.grid(axis='y', c='gainsboro', zorder=9)
ax3.grid(axis='y', c='gainsboro', zorder=9)
ax4.grid(axis='y', c='gainsboro', zorder=9)

# pdfファイルの初期化
pp = PdfPages('1ch_4.pdf')

# figureをセーブする
pp.savefig()

# pdfファイルをクローズする。
pp.close()


# In[ ]:





# In[7]:





# In[ ]:




