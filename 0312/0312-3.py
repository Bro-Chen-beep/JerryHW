
# coding: utf-8

# In[1]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text


# In[2]:


book1[:]


# In[4]:


book1[0:]


# In[5]:


book1[:87]


# In[6]:


book1[87:8787]


# In[7]:


book1[87:8787:87]


# In[8]:


book1[:87:3]


# In[9]:


book1[0::87]


# In[10]:


book1[::87] 

