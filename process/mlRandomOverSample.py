#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing required Library
import pandas as pd


# In[13]:


import numpy as np
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


# In[14]:


from __future__ import division


# In[15]:


from collections import Counter


# In[16]:


import numpy as np
from sklearn.utils import check_random_state


# In[17]:


# import library
from imblearn.over_sampling import RandomOverSampler


# In[ ]:


from collections import Counter


# In[ ]:


from sklearn.datasets import make_classification


# In[ ]:


from imblearn.over_sampling import RandomOverSampler # doctest: +NORMALIZE_WHITESPACE


# In[ ]:


X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=3,
                           n_clusters_per_class=1,
                           weights=[0.01, 0.05, 0.94],
                           class_sep=0.8, random_state=0)


# In[ ]:


print('Original dataset shape {}'.format(Counter(y)))
    Original dataset shape Counter({1: 900, 0: 100})


# In[ ]:


ros = RandomOverSampler(random_state=42)


# In[ ]:


X_res, y_res = ros.fit_sample(X, y)


# In[ ]:


print('Resampled dataset shape {}'.format(Counter(y_res)))
    Resampled dataset shape Counter({0: 900, 1: 900})


# In[ ]:


def __init__(self, ratio='auto', random_state=None):
        super(RandomOverSampler, self).__init__(
            ratio=ratio, random_state=random_state)


# In[ ]:


def _sample(self, X, y):


# In[ ]:


random_state = check_random_state(self.random_state)
        target_stats = Counter(y)


# In[ ]:


X_resampled = X.copy()
        y_resampled = y.copy()


# In[ ]:


for class_sample, num_samples in self.ratio_.items():
            index_samples = random_state.randint(
                low=0, high=target_stats[class_sample], size=num_samples)


# In[ ]:


X_resampled = np.concatenate((X_resampled,
                                          X[y == class_sample][index_samples]),
                                         axis=0)


# In[ ]:


y_resampled = np.concatenate((y_resampled,
                                          y[y == class_sample][index_samples]),
                                         axis=0)


# In[12]:


return X_resampled, y_resampled

