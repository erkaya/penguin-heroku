#!/usr/bin/env python
# coding: utf-8

# In[6]:


#penguins
import pandas as pd
penguins = pd.read_csv('penguins_cleaned.csv')


# In[7]:


df = penguins.copy()


# In[8]:


df.head()


# In[9]:


target = 'species'
encode = ['sex', 'island']


# In[11]:


for col in encode:
    dummy = pd.get_dummies(df[col], prefix = col)
    df = pd.concat([df, dummy], axis = 1)
    del df[col]


# In[12]:


df.head()


# In[13]:


target_mapper = {'Adelie':0, 'Chinstrap': 1, 'Gentoo': 2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)


# In[14]:


df.head()


# In[17]:


#separating independent and dependent variables
X = df.drop('species', axis=1)
Y = df['species']


# In[18]:


X.head()


# In[19]:


Y


# In[20]:


#build random forst model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X,Y)


# In[22]:


#saving the model
import pickle
pickle.dump(clf,open('penguins_clf.pkl', 'wb'))


# In[ ]:




