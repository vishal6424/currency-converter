
# coding: utf-8

# In[1]:


import pandas as pd

rates = pd.read_csv("country_name.csv")


# In[34]:


rate = rates.copy()


# In[35]:


# rate.head()


# In[36]:


rate = rate.rename(columns={"Unnamed: 0":"serial"})


# In[37]:


# rate.head()


# In[52]:


rate['new'] = rate.serial.astype(str) + ' ' + rate['US Dollar']


# In[53]:


# rate.head()


# In[57]:


country_name = " \n".join(rate.new.values)


# In[58]:


