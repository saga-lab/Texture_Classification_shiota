#!/usr/bin/env python
# coding: utf-8

# In[135]:


from sklearn.metrics import classification_report,log_loss
import numpy as np


# In[136]:


IN_DIR_PATH = "3ch_normalized"
csv = np.loadtxt("../logs/"+IN_DIR_PATH+"/cm.csv").astype(np.uint8)


# In[137]:


csv


# In[138]:


texture_name = ["ArtLeather","GreenTile","ArtGrass","CorkSheet","EnbiPunch","Luncheon01","Luncheon02","Luncheon03","Carpet01"]


# In[139]:


actual_label = []
predicted_label = []

for i in range(csv.shape[0]):
    for j in range(csv.shape[1]):
        for k in range(csv[i,j]):
#             print('k:',k)
#             print('i,j',i,j)
            predicted_label.append(i)
            actual_label.append(j)


# In[140]:


cr=classification_report(actual_label, predicted_label,target_names=texture_name,digits=4)
#ll=log_loss(actual_label, predicted_label)
print(cr)
#print(ll)


# In[134]:


f = open('../logs/'+IN_DIR_PATH+'/cr.txt','w')
f.write(cr)
#f.write(ll)
f.close()


# In[ ]:




